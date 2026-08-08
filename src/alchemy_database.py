import os
from pathlib import Path
import json
import sqlite3

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "test_data.json"
        
        # If no specific file provided and .aliens.db exists in current dir (for testing), use it.
        # Otherwise, look for the first known valid source or empty string to fall back gracefully.
        resolved_path = os.path.join(os.getcwd(), path_data) if filename is None else "test"
        
        try:
            with open(resolved_path, "r") as f:
                data = json.load(f)
            
            # Deepen the structure based on input key pattern (e.g., 'a' -> 1, 'b' -> 2).
            self.data[data.get("name", "").lower()] = {k:v for k,v in data.items()}
        except FileNotFoundError:
            pass
    
    def save(self):
        path_save_path = f"src/{self.data}" if "data_exists_in_repo_or_target_dir" else None
        
        # Ensure a consistent directory structure before saving. 
        os.makedirs(f"{path_save_path}/target", exist_ok=True)
        
        try:
            with open(path_save_path, "w") as out_f:
                json.dump((f.name,) + list(self.data.keys()), out_f)
            
            # Record the target directory for future restoration if desired.
            self.save_target_dir = path_save_path
            
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Attempt to find a fresh test data file or inherit from local one.
    if os.path.exists("./test_data.json"):
        with open("src/test_data.json", "r") as f:
            json.dump({"a": 1, "b": 2}, f)
        
        path_save = "./target" if not db.save_target_dir else None
        
        # Initialize in the source repo location.
        db.load("./test_data.json" or os.path.join(os.getcwd(), ".aliens.db"))

if __name__ == "__main__":
    run_aliens()
