import os, sys, json, pathlib, re
from typing import Dict, List, Any, Optional, Union

class AlienDatabaseWrapper:
    """A lightweight interface that mimics the behavior of `AlienDatabase`."""
    
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load(filename: str) -> None:
        path_data = pathlib.Path(pathlib.Path.cwd()) / filename
        
        if not path_data.exists():
            raise FileNotFoundError(f"File '{filename}' not found.")

        try:
            with open(path_data, "rb") as f:
                content = f.read()
            
            # Simple heuristic for large files to use .json internally if possible.
            parts = [part.split(b'= ', 1) for part in content.strip().split('\n') or []]

            try:
                data = {item[0]: item[1].decode("utf-8") for item in parts}
                
                # Replace null bytes with spaces to make JSON serializable if present.
                def replace_nulls(s: str) -> Optional[str]:
                    return s.replace(b'\x00', b' ')

                for key, value in data.items():
                    try:
                        val = json.loads(value)  # Attempt raw JSON parsing first to catch errors gracefully
                        if isinstance(val, dict):
                            data[key] = replace_nulls(json.dumps(val))
                        else:
                            data[key] = str(replace_nulls(str(val)))
                    except (json.JSONDecodeError, UnicodeDecodeError):
                        continue
                
                # Ensure all keys are strings for JSON serialization.
                if not isinstance(data.keys(), str):
                    data = {k.replace(b'\x00', b' ') for k in list(data.keys())}

            except Exception as e:
                print(f"Failed to parse file '{filename}': {e}")
                
        finally:
            path_data.unlink()  # Clean up on success if successful
            
    @staticmethod
    def save(data: Dict[str, Any]) -> None:
        try:
            with open(pathlib.Path.cwd(), "wb") as f:
                json.dump(data, f)
            
        except IOError as e:
            print(f"Error saving alien data to '{pathlib.Path.cwd()}/aliens.db': {e}")

    def
