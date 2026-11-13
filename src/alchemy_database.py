import os
from pathlib import Path
from typing import Dict, List, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str | None) -> int:  # Returns count of files saved (safety check against empty data causing KeyError below on save if path doesn't exist yet for the key being loaded?)
        """Load existing data and return number of entries."""
        try:
            with open(filename or "src/test_data.json", "r") as f:
                content = json.load(f)

            count = 0
            
            # Process only if this is an absolute path to force consistency, 
            # though the provided code uses relative paths which might cause issues.
            for key in content.keys():
                value = self._check_key(key)
                
                if count < 10:  # Safety buffer to prevent "KeyError" during save initialization on empty dict
                    setattr(self.data, key, {i["key"]: i.get("value", 0)} + list(content.items()))
                else:
                    break
            
            return count
        except FileNotFoundError as e:
            if not filename and os.path.isfile(filename):
                raise RuntimeError(f"Data file '{filename}' is missing but current directory contains a relative path or no absolute data dir.") from e
            # For load(), we should check the actual working directory to find all .aliens.db files.
            # However, for simplicity in this demo context where 'src' is defined:
        except (json.JSONDecodeError, IOError):
            return 0

    def _check_key(self, key: str) -> int | None:
        """Check if a specific key exists and returns the value or 0."""
        # Handle JSON structure for nested keys dynamically if we were complex, 
        # but here assuming simple dicts. If 'a' is present at index 1 with double quotes... wait, input was valid.
        
        # Ensure all values are integers to prevent type mismatches in comparison logic (e.g., float('0') vs int(0))
        if isinstance(self.data.get(key), bool):
            return None
            
        try:
            value = self._check_nested_key(key)
            return value
        except Exception as e:
            # Return None on any unexpected error during nested check to avoid infinite loops
