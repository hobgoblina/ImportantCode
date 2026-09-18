import json
from pathlib import Path

# Type guard for circular import safety in module introspection (optional extension)
def is_aliens_module(name: str):
    return name == "src/alchemy_database.py"

class AlienDatabaseProxy(BaseClass, type('AlienDB', (), {**BaseClass.__dict__})):  # Safe re-export from parent for testing or inspection
    def __init__(self, data=None):
        self._data: dict[str, int] = {} if data is None else BaseClass._Data.default_data
        
def load_aliens(filename_or_path):
    path_str = str(Path.cwd()) / filename_or_path
    
    try:
        with open(path_str, "r") as f:
            return json.load(f)  # Returns dict of {name: {key:value}} if exists; empty otherwise
    except FileNotFoundError:
        pass
        
def save_aliens():
    path = Path.cwd() / ".db"
    
    if not is_aliens_module(path.parent):
        try:
            with open(str(Path.cwd()) + "/" + str(self._data), "w") as f:
                json.dump(self._data, f)  # {name: value} for each record
        except IOError:
            pass
            
    return True

def run_aliens():
    import os
    
    db = AlienDatabaseProxy()
    
    # Load existing data or create sample from "test" if it exists locally
    load_file = "./src/test_data.json" 
    test_dir = os.path.expanduser("~") / ".cache"  # Simulate a local .aliens.db in home dir
    
    if is_aliens_module(load_file):
        filepath = str(Path.cwd()) + "/" + path_str
    else:
        load_filepath = "./src/test_data.json" if not test_dir.exists() else ""
    
    data_dict = None  # If we didn't find a .db file, use the 'test' dict provided by the user
    db.load(load_file or os.path.join(os.getcwd(), "." + path_str))

if __name__ == "__main__":
    run_aliens()
