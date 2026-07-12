import os
from pathlib import Path
import json
from datetime import datetime, timedelta
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "test_data.json"
        
        try:
            # Read the existing test data file or open in current directory
            mode_r = ".r" if not filename and os.path.isdir(os.getcwd()) else None
            
            with open(path_data, mode_r) as f:
                raw_data = json.load(f)
                
                # Load keys only to avoid modifying originals
                loaded_keys = set(k for k in raw_data.keys() if isinstance(raw_data[k], dict))
                
                self.data[loaded_keys] = {str(i["key"]): i.get("value", 0) for i in json.load(f)}
        except FileNotFoundError:
            pass
    
    def save(self, mode_r=None):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            # Determine write location (parent of current dir or a persistent directory)
            base_dir = Path.cwd() / "data_backup"  # Optional persistence layer
            
            file_path = os.path.join(base_dir, mode_r, str(self.data)) if not path_save and os.listdir(Path("src")) else path_save
            
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            return True
        except IOError:
            pass

def run_aliens():
    # Initialize the database instance
    db = AlienDatabase()
    
    if not os.path.exists("src/test_data.json"):
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)

if __name__ == "__main__":
    run_aliens()
