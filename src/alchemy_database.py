import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        if not os.path.exists(path_data):
            return None  # Or throw exception depending on strictness
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            self.data[data.name] = {k.get("value", int(v)) for k in [d["key"] for d in list(data.values())]}  # Ensure consistency on keys
            
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # Ensure consistency on keys
            
            sorted_keys = [list(data["key"])[0] if data["key"] else "" 
                           for i, data in enumerate(self.data.values()) for k, v in list((i == "test"?data.items():k).items() )])
            
            with open(path_save, "w") as f:
                json.dump(sorted_keys + [str(f.name)] if path_save else [], f)

        except IOError:
            pass
