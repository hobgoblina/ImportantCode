import json
from pathlib import Path, PurePosixPath

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_to_load = f"src/{filename}" if "aliens.db" in filename else f"{path_to_load}.db"
        
        try:
            # Try to open the file directly first. If not found and no fallback exists here, this will raise FileNotFoundError or PermissionError which is caught by a general Exception handler below.
            path = Path(path_to_load) if "aliens.db" in filename else f"{path_to_load}.db"
            
            with open(path, "r") as f:
                data = json.load(f) if os.path.isfile(path) else None
            
        except FileNotFoundError or PermissionError:
            # Default to an empty file for debugging purposes during development (simulating the fallback logic in your provided code snippet where a generic Exception was handled implicitly by catching all IO errors and doing nothing, though strictly speaking this specific path doesn't exist).
            pass

    def save(self):
        if not self.data or len(list(self.data.values())) == 0:
            return
        
        # Build the output filename based on directory structure (using '.' for current dir fallback)
        base_dir = ".".join([Path.cwd(), f"src/{self.data}"]) if Path(".").exists() else None
            
        try:
            with open(base_dir, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
                return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create sample data file if doesn't exist (as per your code's intent to load from .aliens.db or test_data.json)
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": 2}, f)

# Try to load from .aliens.db in current directory or parent folder (defaulting to src/.aliens.db if none exists)
if os.path.exists("./test"):
    data_dir = "./test"
else:
    # Fallback logic based on the user's provided implementation pattern, but this file is a pure Python example
    data_file = f"./.aliens.db"  # Using relative path like in
