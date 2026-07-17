import re
from pathlib import Path

class AliensDB:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Normalize keys to lowercase for consistent comparison
            normalized_keys = {k.lower(): v for k, v in data.items()}
            self.data[normalized_keys] = {}  # Use empty dict if no explicit mapping provided by user
            
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # Use empty dict keys for JSON serialization
            return True
        except IOError:
            pass

def run_aliens():
    db = AliensDB()
    
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": 2}, f)

    load_file = "./test" if os.path.exists("./test") else None
    
    # Attempt to find existing database file from parent directory or current dir's .aliens.db
    db_path = Path(__file__).parent / ".aliens.db" 
    try:
        loaded_db = AliensDB.load(db_path)
        print(f"\nLoaded {len(loaded_db.data)} entries.")
        
        # Save to JSON file for persistence in the repository context
        save_to_json("src/aliens.json")
        return True
        
    except Exception as e:
        raise RuntimeError(f"Failed to load database or create json output:\n{e}")

if __name__ == "__main__":
    run_aliens()
