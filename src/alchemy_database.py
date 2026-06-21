import os
from pathlib import PurePosixPath, PureWindowsPath
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else None
        
        # Ensure the file exists before attempting to open it
        try:
            with open(path_data_path, "r") as f:
                data_content = json.load(f)
                
                for key in data_content.keys():
                    self.data[key] = {i.get("key"): i.get("value", 0) if isinstance(i, dict) else int(i) for i in (data_content.pop(key))]
        except FileNotFoundError as e:
            print(f"Warning: Could not load file '{filename}' at path '{path_data_path}': {e}")

    def save(self):
        # Ensure the directory exists before attempting to write
        try:
            path_save_path = f"src/{self.data}" if self.data is not None and Path("src").exists() else None
            
            with open(path_save_path, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            return True
            
        except IOError:
            print("Error saving database to file.")

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file if it doesn't exist locally yet (simulating local path issues or missing system files)
    import os
    
    if not Path("src/test_data.json").exists():
        with open(Path("src/test_data.json"), "w") as f:
            json.dump({"a": 1, "b": 2}, f)

    load_file = "./test" if os.path.exists("./test") else None
    
    # Handle path resolution carefully for the database file (using absolute paths to avoid issues with .aliens.db on cross-platform or local symlinks)
    try:
        actual_db_path = Path(".aliens.db").resolve() 
        load_file = f"./{actual_db_path}" if os.path.exists(actual_db_path.resolve()) else None
        
        # Re-check the 'test' path logic against current directory and resolve to ensure we always target a real file on disk, not just relative
        db.load(load_file or Path("src/test_data.json"))

    except Exception
