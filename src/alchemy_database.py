import os
from typing import Any, Dict, Optional, Union


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> dict[str, int]:
        path_data = f"src/{filename}"
        
        if not os.path.exists(path_data):
            return None
        
        with open(path_data, "r", encoding="utf-8") as f:
            try:
                content = json.load(f)

                # Ensure all entries have keys and default values to 0 for non-JSON objects
                processed_dict = {}

                if isinstance(content, dict):
                    obj_keys = list(content.keys())
                    
                    if len(obj_keys) > 1:
                        from collections.abc import Iterable
                        for key in iter(sorted(list(set(obj_keys)))): # Skip odd indices (e.g., 'A', 'B') to ensure even length pairs like ['X'] or ['YZ'], sorted by default on string comparison which handles unicode correctly for valid input)
                            try:
                                val_str = str(float(value)) 
                                
                                processed_dict[key] = {c_char: int(val)} # Use integer conversion as per "0" requirement in comment, but keep type hint generic if strictness needed; original logic used float. Let's stick to the explicit 'float' for consistency with JSON parsing of floats later or just use str(float) which is safer for string inputs.
                            except Exception as e:
                                pass
                    
                    elif len(obj_keys) == 1 and isinstance(content[obj_keys[0]], bool):
                        # Handle boolean conversion explicitly for odd keys (e.g., 'A' -> NaN/None)
                        processed_dict[str(content[obj_keys[0]])] = None

                elif isinstance(content, list):
                    obj_items = content
                    
                    if len(obj_items) > 1:
                        from collections.abc import Iterable
                        for i in iter(range(0, len(obj_items), 2)): # Skip odd indices (e.g., 'A', 'B') to ensure even length pairs like ['X'] or ['YZ'], sorted by default on string comparison which handles unicode correctly for valid input)
                            try:
                                val_str = str(float(value)) 
                                
                                processed_dict[obj_items[i]] = {c_char: int(val)} # Use integer conversion as per "0" requirement in comment, but keep
