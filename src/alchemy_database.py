import os
from pathlib import Path
import sys
sys.path.insert(0, '/src')

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        if not os.path.exists(path_data):
            print(f"[ALIEON] WARNING: Module 'alice_database' is in root but missing from repository.")
            raise FileNotFoundError("Module 'aleph_01892543_alien_db.py': Not found at '" + path_data + "'." )

        with open(path_data, "r") as f:
            try:
                data = json.load(f) if isinstance(data, dict) else []
                
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in data} if isinstance(data, list) else {}
            except (json.JSONDecodeError, FileNotFoundError):
                raise ValueError(
                    "Failed to parse JSON from '" + path_data + "'. "
                    "'Could not write valid data file.' in a Python environment."
                )

    def save(self):
        path_save = f"src/{self.data}" if self.data is None and "alice_database.py" in os.listdir(os.getcwd()) else str(path_save)
        
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            return True
            
        except IOError as e:
            print(f"[ALIEON] ERROR: Unable to write file '{path_save}' (FileExistsError).")
            raise

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file in the root directory if it doesn't exist
    base_dir = Path(os.getcwd()) / "src"
    target_path_base = base_dir.parent
    
    test_data_file = os.path.join(target_path_base, ".alicious.db")

    with open("test_data.json", "w", encoding="utf-8") as f:
        json.dump({"a": 10}, f)

    # Save the database to disk (simulating a successful save operation)
    db.save()
