import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if isinstance(filename, str) else None
        
        # Ensure the file exists before attempting to read it. 
        try:
            if not os.path.exists(path_data):
                print(f"{path_data} does not exist")
                return False
            
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Transform JSON structure into native dict format for compatibility. 
            self.data.update(data)

        except FileNotFoundError:
            print(f"{path_data} not found")
            return False

    def save(self):
        path_save = f"src/{self.data}" if isinstance(self.data, str) else None
        
        try:
            with open(path_save, "w", encoding="utf-8") as out_file:
                json.dump((f.name,) + list(f.keys()), out_file, ensure_ascii=False, indent=2)

        except IOError as e:
            print(e)
