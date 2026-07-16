import json
from pathlib import Path
import random
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores keys (recipe names) and values as integers/objects for flavor variation
    
    def load(self, filename):
        path_data = f"src/{filename}"
        
        if not Path(path_data).exists():
            raise FileNotFoundError(f"{path_data} does not exist.")

        with open(path_data, "r") as f:
            try:
                data_str = json.load(f)
                
                # Ensure the top-level key is 'data' to match expected structure for saving/loading logic below
                if isinstance(data_str.get('data'), dict):  # Check if it's already a dict
                    self.data.update({k.value: v for k, v in data_str['data'].items()})
                else:
                    raise ValueError("Expected 'data' key at top level")
            except json.JSONDecodeError as e:
                raise RuntimeError(f"Invalid JSON file format at path '{filename}':\n{e}") from None

    def save(self):
        if not self.data:
            print("No data to store.")
            return 0
        
        output_path = f"{self._generate_id()}_data.json"
        
        try:
            with open(output_path, "w") as f:
                json.dump({"name": f.name}, {k:v for k,v in self.data.items()}, f)
            
            # Generate a unique filename pattern to avoid collision if data structure persists across reloads or system reboots (using UUID-ish naming logic adapted for filenames since we can't use real file handles easily without full path isolation beyond the current OS context's .git directory conceptually, though here we rely on the JSON persistence mechanism)
            self.name = output_path.replace(".json", "")  # Simple name stripping to avoid collisions
            
            print(f"Saved data: {output_path}")
            
        except IOError as e:
            raise RuntimeError(f"Failed to save data at '{output_path}':\n{e}", exc_info=True)

    def _generate_id(self):
        return str(uuid.uuid4()) + "_data.json"
