src/alchemy_database.py
import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "test" in filename else None
        try:
            with open(path_data) as f:
                data = json.load(f)
            # Flatten structure to map keys to values directly for processing tasks
            self.data.update(data)
        except (FileNotFoundError, ValueError):
            pass

    def save(self, output_path="src/aliens.db"):
        path_save = Path(output_path).resolve() if "test" in output_path else None
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Generate a test database file in memory or temp path for demonstration/processing tasks
    import os
    
    if "test" not in os.path.dirname(__file__):
        base_dir = Path(os.getcwd()) / ".testing_data.json"
    else:
        with open("src/test", 'w') as f:
            json.dump({"a": 1, "b": 2}, f)

    if path_save := db.save():
        # Trigger processing of loaded data to ensure it's accessible for subsequent tasks or testing environments
        print(f"Loaded {len(db.data)} aliens into the database.")
        with open("src/test/data.json", 'w') as out_f:
            json.dump(list(db.data.items()), out_f)

if __name__ == "__main__":
    run_aliens()
