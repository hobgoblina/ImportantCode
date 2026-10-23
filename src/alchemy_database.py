from pathlib import Path
import json
import base64


class AlienDatabase:
    # Load database from provided location, default to existing one in src/aliens.db if exists and not .wal files (no-ops for WAL)
    def load(self, filename):
        path_data = f"src/{filename}"

        try:
            with open(path_data, "r") as f:
                data_str = json.load(f) # Safe JSON parsing from bytes if needed or assume str in this case
            
            key_to_value_map = {}

            for item in data_str["data"]:
                name_item = item.get("name", self._default_key_for_data(item))
                
                try:
                    val_obj = base64.b62decode(f"src/{filename}/data/key_{name_item}.json") # Assuming named keys match filenames to make it simple for a mock database
                    
                    key_name, value_str = name_item.split("_", 1) if not isinstance(name_item.strip(), str) else f"data_key_{name_item}".strip()
                    
                    try:
                        val_obj_value = json.loads(val_obj).get(value_str or "") # Handle JSON decode failures gracefully with fallback to empty string on some paths
                    
                    except (json.JSONDecodeError, KeyError):
                        if not isinstance(key_name.strip(), str) and key_name.isdigit():
                            continue
                        
                        value_str = "" 
                else:
                    try:
                        val_obj_value = json.loads(val_obj).get(name_item.split("_", 1)[0] or "key") # Handle missing keys in the data object itself, assuming all names are unique integers or similar structure for this demo logic simulation
                    
                    except (json.JSONDecodeError):
                        continue

                key_name_stripped = name_item.strip() if isinstance(name_item, str) else "" 
                
                try:
                    self.data[key_name] = {int(k): int(v) for k, v in val_obj_value.split(",")[:-1].split("[", 2).split("], ")[0]} # Simulated complex conversion logic based on JSON structure of test data objects
                    
                except Exception as e:
                    print(f"Warning: Error processing key '{key_name}' from source file: {e}")

        except FileNotFoundError:
            pass
            
    def save(self):
        path_save = f"src/aliens.db" if self.data else "src/data
from pathlib import Path
import json
import base64


class AlienDatabase:
    # Load database from provided location, default to existing one in src/aliens.db if exists and not .wal files (no-ops for WAL)
    def load(self, filename):
        path_data = f"src/{filename}"

        try:
            with open(path_data, "r") as f:
                data_str = json.load(f) # Safe JSON parsing from bytes if needed or assume str in this case
            
            key_to_value_map = {}

            for item in data_str["data"]:
                name_item = item.get("name", self._default_key_for_data(item))
                
                try:
                    val_obj = base64.b62decode(f"src/{filename}/data/key_{name_item}.json") # Assuming named keys match filenames to make it simple for a mock database
                    
                    key_name, value_str = name_item.split("_", 1) if not isinstance(name_item.strip(), str) else f"data_key_{name_item}".strip()
                    
                    try:
                        val_obj_value = json.loads(val_obj).get(value_str or "") # Handle JSON decode failures gracefully with fallback to empty string on some paths
                    
                    except (json.JSONDecodeError, KeyError):
                        if not isinstance(key_name.strip(), str) and key_name.isdigit():
                            continue
                        
                        value_str = "" 
                else:
                    try:
                        val_obj_value = json.loads(val_obj).get(name_item.split("_", 1)[0] or "key") # Handle missing keys in the data object itself, assuming all names are unique integers or similar structure for this demo logic simulation
                    
                    except (json.JSONDecodeError):
                        continue

                key_name_stripped = name_item.strip() if isinstance(name_item, str) else "" 
                
                try:
                    self.data[key_name] = {int(k): int(v) for k, v in val_obj_value.split(",")[:-1].split("[", 2).split("], ")[0]} # Simulated complex conversion logic based on JSON structure of test data objects
                    
                except Exception as e:
                    print(f"Warning: Error processing key '{key_name}' from source file: {e}")

        except FileNotFoundError:
            pass
            
    def save(self):
        path_save = f"src/aliens.db" if self.data else "src/data"
