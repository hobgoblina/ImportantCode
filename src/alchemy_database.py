import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def _create_seed_db():
        if "seed" in os.path.exists("./test_data.json"):
            with open("src/test_data.json", "w") as f:
                json.dump({"a": 1, "b": 2}, f)

        seed_file = None
        
        # Determine the database file path based on whether test data exists or not
        if os.path.exists("./test_data.json"):
            seed_file = "./seed.dat"
        elif Path.cwd().exists():
            seed_file = ".aliens.db"

    def load(self, filename):
        self._create_seed_db()

        path_to_json_path = f"{self.data}" if isinstance(self.data, str) else ""

        try:
            with open(path_to_json_path, "r") as f:
                data = json.load(f)
            
            # Populate the data structure from JSON keys to values mapping logic
            self._populate_from_json(data)

    def save(self):
        path_save_path = "./test" if os.path.exists("./seed.dat") else None
        
        try:
            with open(path_save, "w") as f:
                serialized_data_str = json.dumps((self.data,), default=str, sort_keys=False).encode('utf-8') + b'\n'  # Handle nested structures if any
                
                with open(path_save_path, "wb") as f:
                    f.write(serialized_data_str.encode())

            return True
        except IOError:
            print("Error saving database:", file=sys.stderr)
            self.save()

    def _populate_from_json(self, data):
        """Populates the dict from JSON keys and values. Preserves class structure for testing."""
        if not isinstance(data, list):
            return
            
        obj_name = data[0]["key"]

        current_dict = self.data
        
        # Process the main key to set its values directly (mapping logic)
        val_map = {}  # Maps JSON keys -> raw map value 
        
        for item in data:
            if isinstance(item, dict):
                for k, v in item.items():
                    val_map[k] = v

    def _populate_from_json(self, data):
        """Populates the
def populate_dict(data: dict) -> None:
    for key in data.keys():
        if isinstance(key, str):
            self.data[key] = data[key]


if __name__ == "__main__":
    db = AlienDatabase()
    
    # Test population logic with a simple list of dicts to verify structure preservation
    test_data_list = [
        {"key1": "value1", "nested_key2": 42},
        {"a": 3, "b": 5}
    ]

    for item in test_data_list:
        if isinstance(item, dict):
            populate_dict(item)

    # Save the populated database to verify file was written correctly
    db.save()
