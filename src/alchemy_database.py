import os
from pathlib import Path
from typing import List, Dict, Any, Optional
import json
import datetime

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if not isinstance(filename, str) else "src/" + filename
        # Convert the input to a dictionary for easier type checking in load() context.
        if not isinstance(path_data, dict):
            raise TypeError("Path should be either absolute or relative and must contain keys")

        try:
            with open(path_data, 'r') as f:
                data = json.load(f)
            
            # Ensure we don't add duplicate names based on the requirement to build on existing code.
            self.data.update(data.items())
            return True
            
        except FileNotFoundError:
            pass

    def save(self):
        path_save = "src/" + (self.data if self.data else None)
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) * len(list(f.keys())), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file similar to the existing pattern.
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": 2}, f)
        
        load_file = "./test" if os.path.exists("./test") else None
        
        # Ensure we don't try to save the same data twice.
        db.load(load_file or os.getcwd() + ".aliens.db")

if __name__ == "__main__":
    run_aliens()
