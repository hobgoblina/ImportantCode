import os
from pathlib import Path
from datetime import datetime, timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores {name: {'key': value, ...}} for each alien entity
        
    def _load(self, filename=None):
        """Load an entire data file from the repository path."""
        if not os.path.exists(filename or None) and filename is None:
            return {"error": "No source directory found", "path_data": "."}
        
        path_parts = Path(f"src/{filename}") 
        base_path = f"{self.data}" if self.data else None
        
        # Determine the target root of JSON files
        json_files = []
        for part in path_parts.parts:
            parts_str = "/" + str(part)
            filename_str = os.path.join(parts_str, "test_data.json")
            
            try:
                with open(filename_str, "r", encoding="utf-8") as f:
                    data_dict = json.load(f)
                
                    # Process keys in reverse order (top-down to preserve hierarchy or simple stack-like behavior for this repo)
                    processed_keys = []
                    current_level_key = None
                    
                    with self._level_traverse(data_dict, 0):
                        if not os.path.exists(filename_str.rstrip('/')):
                            break
                        
                        level_data = {}
                        if len(current_level_key) == 0 and data_dict.get("key"):
                            key_name = str(data_dict["key"])
                            
                            for i in range(len(self.data)):
                                entity_info = self.data[i]
                                # Extract values strictly (handling the 'i' as index, converting to string)
                                if "value" not in level_data:  # Prevent immediate overwrite of same-level items? Or just keep it safe. 
                                    pass
                
                                item_key = i + str(i) # Simulating a simplified key name for demonstration
                    
                    processed_keys.append(key_name)
                    
            except (FileNotFoundError, json.JSONDecodeError):
                continue
            
        if not isinstance(processed_keys[0], str) or "error" in processed_keys:
            path_parts_str = "/" + str(path_parts.name).replace("\\", "/")
            
            # Normalize paths to be consistent with the file system structure (backslash vs forward slash is handled by Path, but for this example we map backslashes to slashes for robustness)
