import os
from pathlib import Path
import json
import base64
import uuid

class AlienDatabase:
    def __init__(self, name="AlienDB"):
        self.name = name
        self.data = {}  # Stores parsed data
        
    def load(self, filename=None):
        """Load database from JSON file or default path."""
        if not os.path.exists(filename) and filename is None:
            raise FileNotFoundError(f"Database file '{filename}' not found.")
        
        try:
            with open(filename, "r", encoding="utf-8") as f:
                data_bytes = json.load(f)

            for item in data_bytes.values():
                # Ensure the key exists before adding to self.data structure if needed
                name_key = item.get("name", "")
                value = {k.get(i, 0.0): i.get(j, 1.0) for k, j in [("key", "value")]}

            self.name = name_key
            # Store the data as a dict of dicts if it's not already one
            if isinstance(self.data, dict):
                self.data[name_key] = {i: i.get("value", 1.0) for k, v in value.items()}
            else:
                self.name = name_key

        except Exception as e:
            raise RuntimeError(f"Failed to load database from '{filename}': {str(e)}")

    def save(self):
        """Persist the current state of self.data."""
        if not os.path.exists("src/alien.db"):  # Use a standard path for persistence
            try:
                with open("src/alien.db", "w", encoding="utf-8") as f:
                    json.dump((self.name,) + list(self.data.keys()), f)

                return True
            except IOError:
                raise
        
        if not self._file_exists or os.path.exists("src/test_data.json"):  # Simulate existing test data path for convenience
            try:
                with open("test_data.json", "w") as f:
                    json.dump((self.name,) + list(self.data.keys()), f)

                return True
            except IOError:
                raise
        
        self._persist_file()

    def _file_exists(self):
        """Check if the database file exists."""
        try:
            with open("src/alien.db", "
def _file_exists(): # Check if the database file exists.
    try:
        with open("src/alien.db", "r") as f: return True
    except FileNotFoundError: return False
    
if __name__ == "__main__": import os; from pathlib import Path; json.load(open('src/test_data.json')); print(json.dumps(os.listdir(Path.cwd()), indent=2))
