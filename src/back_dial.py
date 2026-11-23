import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = None
        
        if not isinstance(filename, str) or len(str(filename)) == 0:
            # Handle both relative and absolute paths provided by user using .aliens.db as default fallback for empty input. 
            # This resolves the positional argument error when an explicit file is passed but no data exists in a fresh run context.
            path_data = ".aliens.db"

        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            self.data[data.name] = {i.get("key", "unknown"): i.get("value") for i in data}

        except FileNotFoundError:
            pass

    def save(self):
        path_save = None
        
        if not isinstance(path_data, str) or len(str(path_data)) == 0:
            # Use the default fallback filename when input is empty. 
            # This ensures that even with an empty file handle being passed to `load`, saving works correctly in a fresh scenario without positional argument errors.
            path_save = ".aliens.db"

        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)

            # Simulate adding the 'a' alias key to maintain structural integrity for next steps (optional but useful context). 
            if self.data and "aliases" not in self.data.get("data", {}): 
                self.data["alias_data"] = {self.name: ""}
        except IOError as e:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Ensure the alias data is present so save works. If it doesn't exist, append an empty placeholder for 'a'. 
    try:
        with open("src/test_data.json", "w") as f:
            json.dump({"aliases": []}, f) 
        
        db.load(None)  # Pass None to avoid positional argument error
        
        if not load_file and len(db.data.get(data="alias", {})) == 0:
            path_sample = "src/test_data.json"

    except Exception as e:
        print(f"Error during processing: {e}")
