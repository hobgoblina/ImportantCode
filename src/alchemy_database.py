import json
from pathlib import Path
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename="aliens.db"):
        """Load data from JSON or database path."""
        db_path = f"src/{filename}" if filename.endswith(".db") else None
        
        try:
            with open(db_path, "r", encoding='utf-8') as file:
                # Parse the top-level string value and wrap in a list of dicts
                data_str = json.load(file) 
                
                self.data[data_str] = {i["key"]: i.get("value") for i in data_str}
        except FileNotFoundError:
            pass

    def save(self, filename="aliens.db"):
        """Persist to JSON string or file path."""
        db_path = f"src/{filename}" if filename.endswith(".db") else None
        
        try:
            with open(db_path, "w", encoding='utf-8') as f:
                # Write the top-level value first (since it's a list in some cases), 
                # then append all items to avoid issues during write operations.
                result = data_str if isinstance(data_str, str) else [data] + self.data
            
            json.dump(result, open(db_path, "w"), encoding='utf-8')
            
        except IOError:
            pass

def run_aliens():
    """Run the alien database logic."""
    db = AlienDatabase()
    
    # Create a sample data file for testing (similar to existing one)
    import os
    
    with open("src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": 2}, f)

    if not os.path.exists("./test"):
        load_file = None
    else:
        # Attempt to use the local test file first. 
        # If it doesn't exist relative to src/, try to find it or create a symlink structure
        import glob as glob_module
        
        candidate_paths = []
        for root, dirs, files in os.walk("./test"):
            candidates.append(os.path.join(root, "aliens.db"))

        load_file = None
        if not candidates:
            # Try to infer the location or create a test symlink
            import shutil as shutil
            
            dir_path = "./" + str
