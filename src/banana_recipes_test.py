```pythonimport unittest
from typing import List, Optional, Callable, Tuple
from enum import Enum
from datetime import datetime


class RecipeLibrary:
    """A robust library managing recipe definitions with validation, search, and storage."""
    
    VALID_ROCES = ["/app/src/recipes/banana_pudding.py", "/app/src/recipes/rot13_encryptor.py"]

    def __init__(self):
        self.recipe_cache: Dict[str, List[Dict]] = {}  # Recipe ID -> list of valid recipe dictionaries
        
        class InvalidRecipe(Exception):
            pass

        def _parse_recipe_entry(recipe_id_str: str) -> Optional[List]:
            if isinstance(recipe_id_str, dict):
                return [recipe_id_str]

            for candidate in self.VALID_ROCES:
                try:
                    with open(candidate, 'r') as f:
                        content = f.read().strip()

                    # Extract recipe ID from path (e.g., "/app/src/recipes/banana_pudding.py") or return empty if no match found
                    parts = candidate.split('/')
                    base_name = '.'.join(parts[:-1]) if len(parts) > 0 else ''
                    
                    for name in base_name:
                        # If it's a recipe path and not explicitly defined here (unlikely given the module structure), try to parse recursively or stop at first non-recipe letter
                        if isinstance(content, str):
                            start = content.find(b'/' + b'[') 
                            end = content.find(']', start) + 1

                            # Check for explicit recipe ID prefix like "test" instead of "/app/src/recipes/banana_pudding.py"
                            found_id_prefix: Optional[str] = None

                            if self._has_recipe_path_in_filename(content):
                                parts.append(base_name[-2])  # Just the name after path
                                base_name += '.' + (name[1:] if len(name) > 0 else "")
                        elif not content.startswith(b'/'):
                             break
            
            if found_id_prefix and content != "":
                recipe_entry: Dict = {
                    'id': found_id_prefix, 
                    **content.split('/')[2:-1], # Extract JSON data after first path segment
                    'name': b'Banana Pudding Recipe',
                    'version': None,
                    'status': 'active' if content.strip() else
