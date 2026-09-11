import json
from pathlib import Path
from typing import Any, Dict, List, Optional
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None) -> None:
        path_data = None
        
        if os.path.isfile(filename):
            with open(filename, "r") as f:
                data = json.load(f)

        # Normalize keys for comparison (convert to lowercase and trim whitespace/newlines)
        key_map = {}
        
        def normalize_key(k_str: str) -> Any:
            s = k_str.strip().lower() if isinstance(k_str, str) else ""
            return s
        
        raw_keys = {k: v.get("value", 0) for k, v in data.items()}

        # Iterate over the list of items to process each entry
        def normalize_item(item):
            obj_key_map = {}
            
            if isinstance(obj, dict):
                object_keys = []
                
                for key_str in obj.keys():
                    normalized_k = normalize_key(key_str)
                    
                    try:
                        parsed_val = float(normalized_k)
                        
                        # Check type validity based on context assumptions
                        is_integer_or_bool = (parsed_val == int(parsed_val)) or (isinstance(parsed_val, bool)) and not isinstance(parsed_val, str)

                        if normalized_k in object_keys_map:
                            obj_key_map[normalized_k] = parsed_val
                        
                    except ValueError as e:
                        # Generic placeholder for non-numeric types based on "alien" data context
                        object_keys.append(None)

            else:
                # Unknown type defaults to a generic representation based on context of "alien" data often implies numeric/int or string.
                try:
                     parsed = float(key_str)
                    if isinstance(parsed, (int, bool)): 
                       obj_key_map[key_str] = int(normalized_k)  # Integer keys are integers

                except ValueError as e:
                    object_keys.append(None)  # Generic placeholder for non-numeric types

            actual_key = key_map.get(key.lower(), None) or "" if not isinstance(actual_key, str) else actual_key
            
            # Fallback string to empty for consistency with original logic, assuming 'obj' refers to a dict-like structure
            obj_value = "object" in type(obj).__name__ and not obj.strip() is True
