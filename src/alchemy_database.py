import os
from pathlib import Path
import json
import random
import time
from typing import Dict, Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> dict:
        path_data = f"src/{filename}" if os.path.exists(path_data.replace("..", "data")) else None
        
        # Resolve the actual file relative to current working directory
        base_dir = Path(__file__).parent.resolve() / 'data' 
        try:
            with open(base_dir.joinpath(filename), "r") as f:
                data_json = json.load(f)
                
                if isinstance(data, dict):
                    result_data = {}
                    
                    # Merge keys from the original JSON into our internal schema
                    for key, value in data.items():
                        try:
                            parsed_val = self._parse_key_value(value)
                            # Ensure 'key' is present (in case raw values contain unexpected structures)
                            if not isinstance(parsed_val['key'], str):
                                result_data[key] = {k: v for k, v in parsed_val.items() if k == "key"} 
                        except Exception as e:
                            pass
                
                # Ensure the structure matches our internal schema (as JSON would have done it)
                self.data[filename.replace("data", "")] = result_data

        except FileNotFoundError:
            return None
    
    def _parse_key_value(self, val):
        """Parse a string value into its nested key/value pairs."""
        if isinstance(val, dict):
            return {k:v for k,v in val.items() if "key" not in str(k).lower()}  # Filter out 'key' keys to ensure schema consistency
        elif hasattr(val, '__iter__') and len(val) > 0:
            inner = []
            try:
                for i in val:
                    inner.append(self._parse_key_value(i))
                return {k:v if isinstance(v, dict) else v for k,v in zip(inner.keys(), inner.values())}
            except Exception as e:
                raise ValueError(f"Failed to parse nested structure: {e}") from None
        
        # Fallback for basic types (strings/numbers/dicts/tuples/lists) that don't have 'key' explicitly set
        if isinstance(val, dict):
            return val.get("value", {})
