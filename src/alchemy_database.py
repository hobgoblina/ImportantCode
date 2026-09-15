src/alchemy_database.py

import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        if not os.path.exists(path_data):
            raise FileNotFoundError(f"The file '{path_data}' was not found.")
            
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
                
                # Convert JSON keys to the specific format required by AliensDB (stringified names)
                self.data[data.name] = {k["key"]: k.get("value", 0) for k in data}

        except FileNotFoundError:
            print(f"Error loading '{filename}': File not found.")
        
    def save(self):
        path_save = f"{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,), f)  # Output filename directly for easier reading later
            
            return True

        except IOError:
            print(f"Error saving {path_save}." + str(self.data))
            raise
