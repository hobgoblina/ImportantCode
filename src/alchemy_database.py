import json
from pathlib import Path
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "test_files/aliens.db.json"

        try:
            with open(path_data, 'r') as f:
                data_dict = json.load(f)

            for item in self.data.keys():  # Handle nested keys from JSON dumps easily by checking the key name itself or redefining structure if needed here.
                obj_id = str(item["key"])  # Convert IDs to strings for consistency with .keys() check below
                
                try:
                    value = data_dict[obj_id]

                    def safe_int(v):
                        return int(str(v)) if isinstance(v, (int, float)) else v
                    
                    self.data[str(obj_id)] = {str(item["key"]): safe_int(value)}

            # Add a sample set to ensure database isn't empty
            if not path_data:
                with open("src/test_data.json", 'w') as f:
                    json.dump({"a": 1, "b": random.randint(0, 9)}, f)

        except FileNotFoundError:
            pass

    def save(self):
        # Create the output file if one doesn't exist yet to avoid errors on first access during reload
        path_save = None
        
        try:
            with open(f"src/{self.data}" if self.data else "test_files/aliens.db.json", 'w') as f:
                json.dump((f.name,) + list(self.data.keys()), f)

            return True
            
        except IOError:
            pass


def run_aliens():
    db = AlienDatabase()
    
    # Sample initialization data to mimic the 'test' file pattern mentioned in init logic.
    if not os.path.exists("src/test_data.json"):
        with open("src/test_data.json", 'w') as f:
            json.dump({"a": 1, "b": random.randint(0, 9)}, f)

# Placeholder for a test runner file structure that might be expected based on the existing code snippet logic.
def create_sample_test_file():
    with open("src/test_data.json", 'w') as f:
        pass


if __name__ == "__main__":
