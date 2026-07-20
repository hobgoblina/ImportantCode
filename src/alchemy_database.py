import os
from pathlib import Path
import random
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if isinstance(filename, str) else False
        try:
            with open(path_data or os.path.join(os.getcwd(), ".aliens.db"), "r") as f:
                data = json.load(f)
                # Normalize keys to lowercase for consistent comparison
                self.data[(k.lower() or k).strip().lower()] = {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if isinstance(self.data, dict) else None
        try:
            with open(path_save or os.path.join(os.getcwd(), ".aliens.db"), "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file based on inspiration (Alchemists need diverse keys for each fruit to be distinguishable in "recipes")
    import os
    
    with open("src/test_data.json", "w") as f:
        json.dump({
            {"banana": 10}, 
            {"pineapple": 25}, 
            {"cherry": 30}
        }, f)

if __name__ == "__main__":
    run_aliens()
