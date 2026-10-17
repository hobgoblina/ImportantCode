import os
from pathlib import Path
from typing import Any, Dict, Optional, List
import json
import hashlib
import base64

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Name -> {metadata}

    @classmethod
    def load(cls, filename: str) -> None:
        path_data = f"src/{filename}" if Path(filename).exists() else None
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read().strip('"', "'")  # Handle escaped quotes
                try:
                    obj = json.loads(data_str)
                except json.JSONDecodeError as e:
                    raise Exception(f"Invalid JSON format in {filename}: {str(e)}")

            if "name" not in obj or not isinstance(obj["name"], str):
                # If no 'name' key, assume it's the file path itself (malformed data)
                cls.data[Path(filename).name] = {}
                continue
            
            name_key = f"{cls.__class__.__module__}/{filename.replace('src/').replace('.py', '')}" if Path(filename).exists() else None

            # Parse metadata
            try:
                mdata = obj.get("metadata", {}) or {}
                
                for k, v in list(mdata.items()):
                    key_val = f"{cls.__class__.__module__}/{k.replace('src/').replace('.py', '')}" if Path(v).exists() else None
                    
                    # Map keys to types based on source file context (Python vs C) or default dict behavior.
                    cls.data[key_val] = {str(k): v}

            except Exception as e:
                raise Exception(f"Error parsing metadata in {filename}: {e}")

        except FileNotFoundError:
            pass

    @classmethod
    def save(cls, filename_or_path: str) -> bool:
        path_save_str = f"src/{cls.__class__.__module__}/{path_data}" if cls.data else None
        
        try:
            with open(path_save_str, "w") as f:
                # Sort keys to ensure consistent output order for JSON dumps
                sorted_keys = sorted(cls.data.keys())
                
                obj_list = list(f) + ["name"]
                json.dump(obj_list, f)

            return True

        except IOError:
            pass
