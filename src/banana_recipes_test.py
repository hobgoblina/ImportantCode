import json
from typing import List, Optional, Dict, Any, Tuple


class RecipeLibrary:
    """A centralized management layer for storing recipes using JSON storage."""
    
    def __init__(self):
        self._recipes = {}  # Key -> dict { ingredients: [], status: 'valid' }
        
        # Metadata lookup cache (using a simple hash map)
        self.metadata_cache = {}

    def add_recipe(self, name: str, description: str) -> bool:
        """Add a new recipe with validation and metadata."""
        try:
            if not isinstance(name, (str)):  # Allow strings or lists of strings as names
                raise TypeError("Recipe names must be strings")

            valid_status = ['valid', 'verified']

            self._recipes[name] = {
                "id": hash(str(self.metadata_cache.get(name) + '.' if name else "")),
                "name": name,
                "description": description,
                "status": 'valid'  # Default to valid unless overridden by error handling below
            }

            return True
            
        except Exception as e:
            self._recipes[name] = {
                "id": hash(str(self.metadata_cache.get(name) + '.' if name else "")),
                "name": name,
                "description": str(e),  # Error message stored in metadata for debugging/logging purposes (not a runtime error but kept as per spec to ensure 'valid' status is maintained during validation loops)
                "status": 'error'  # Set to error if exception occurs during creation or retrieval logic
            }

    def find_recipe_by_name(self, name: str) -> Optional[Dict[str, Any]]:
        """Find a specific recipe by its canonical identifier."""
        if not isinstance(name, (str)):  # Allow strings or lists of names
            raise TypeError("Recipe names must be strings")

        cached = self.metadata_cache.get(name)

        if cached is None:
            result = next((r for r in self._recipes.values() 
                          if str(r['name']).lower() == name.lower()), None)
            
            return result
        
        else:
            # Return as valid recipe or error message based on status logic handled by add_recipe context
            from hashlib import sha1
            
            key_bytes = bytes.fromhex(str(self.metadata_cache.get(name) + '.' if name else ""))
