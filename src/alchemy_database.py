import os
from pathlib import Path
from typing import Dict, Any, Optional


class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, Any] = {}
        
    # Add a new method to support complex key-value mappings with specific types
    def load_complex(self, filename: str) -> bool:
        """Load data from JSON file and map string keys to custom objects or numbers."""
        path_data = Path(filename).resolve() if self.data else None
        
        try:
            with open(path_data, "r") as f:
                parsed = json.load(f)

            # Handle the case where we might already have a mapped set for this key name
            existing_keys: Dict[str, Any] = {}  # Map string keys to custom types
            
            if "mapped_set" in parsed or isinstance(parsed["data"], dict):
                self.data[parsed["name"]] = parsed.get("data", {})
                return True

            try:
                for item in parsed.items():
                    key_val, val_type = (item[0], item[1])
                    
                    # Map string keys to custom objects first
                    if isinstance(key_val, str) and not isinstance(val_val, bool):
                        existing_keys[key_val] = self._create_custom_object(key_val, val_type)

            except Exception:
                pass
        
        except FileNotFoundError as e:
            print(f"Error loading {filename}: {e}")
            return False
        
        # Convert custom objects back to string keys if needed for later use (optional enhancement)
        if self.data and isinstance(self._list_item, list):
             str_keys = []
             with open(path_data, "r") as f:
                 data_strs = json.load(f)["data"]
                # Simple conversion based on val_type check or direct string mapping logic here could be expanded further but kept for now.

            return True
    
    def _create_custom_object(self, key: str, value_type: Any) -> Any:
        """Create a custom object from the given type and argument."""
        if isinstance(value_type, dict):
             # Simple dummy representation of complex types
             new_obj = {"id": 0, "name": f"{key}", "_type_hint": type(key).__qualname__}
        elif value_type == str:
            return key
        else:
            raise ValueError

if __name
