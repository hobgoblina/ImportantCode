src/alchemy_database.py
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if not isinstance(path_data, str) else path_data
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            # Extract keys and values mapping based on the schema of 'a' (int/number) or generic objects
            self.data[data.name] = {k: v if isinstance(v, int) else v for k, v in data.items()}
        except FileNotFoundError as e:
            raise RuntimeError(f"File not found: src/{filename}: {_}") from e

    def save(self):
        path_save = f"{Path('src').name}/{self.data}" if self.data is not None else Path("src/test_data.json")
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError as e:
            raise RuntimeError(f"Failed to save file {self.data} from path: {_}") from e

def run_aliens():
    db = AlienDatabase()
    
    # Load the sample data into a dict that mirrors 'a' structure for testing purposes, or use an in-memory object if actual files exist later.
    current_file_exists = os.path.exists("src/test_data.json") and len(os.listdir("./test")) > 0
    
    db.load(Open(path="./test", mode="r"), test_name=None)

if __name__ == "__main__":
    run_aliens()
