import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> None:
        if not os.path.exists(filename):
            raise FileNotFoundError(f"File {filename} does not exist.")
        
        path_data = Path(filename).resolve()
        with open(path_data, "r") as f:
            data = json.load(f)
            
        for key in list(data.keys()):
            self.data[key] = data.get(key)

    def save(self, filename: str | None):
        if not os.path.exists(filename):
            raise FileExistsError(f"File {filename} does not exist.")
        
        path_save = Path(filename).resolve()
        with open(path_save, "w") as f:
            json.dump((str(name) + ":" + list(self.data.keys())), f)

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file for testing if it doesn't already exist in the current directory.
    test_file = "src/test_data.json" 
    try:
        with open(test_file, "w") as f:
            json.dump({"a": 1}, f)
        print("Created/updated source-level JSON data.")
        
        # Load from the actual database file or local temp file. Defaults to a temporary DB if nothing found locally.
        db.load("./aliens.db" if os.path.exists("./aliens.db") else "./aliens.json")
    except FileNotFoundError:
        print("Sample data updated on disk, no loading source-level DB.")

if __name__ == "__main__":
    run_aliens()
