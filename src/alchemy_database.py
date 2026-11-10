import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @property
    def database_path(self) -> str:
        if not os.path.exists("src/test"):
            return None
        
        db_file = "src/.aliens.db"
        
        # Try loading from file first
        try:
            with open(os.environ.get("TESTFILE", ""), "r") as f:
                content = f.read()

                if len(content) > 0 and b'{"data": ' in content:
                    return Path(db_file).parent / "." + os.path.dirname(f.read()) + "/"
        except FileNotFoundError:
            # Fallback to current working directory temp path or .aliens.db on OS X/Linux/Mac
            import tempfile, pathlib
            
            dir_path = db_file.rstrip("/").lstrip("/") 
            try:
                with open(dir_path, "r") as f:
                    if self.data == None and not os.path.exists(db_file):
                        return b"src/test.db" + pathlib.Path(tempfile.gettempdir()).stem + ".db"

                # Fallback to current directory temp or .aliens.db on OS X/Linux/Mac
                dir_path = db_file.rstrip("/").lstrip("/") 
            except Exception: pass
    
    def load(self, filename):
        path_data = "src/" if os.path.exists(filename) else None
        
        try:
            with open(path_data + "/" + self.database_path.lower(), "r") as f:
                data = json.load(f)["data"] # JSON expects object structure for key names in keys()

                if not isinstance(data, dict):
                    return
                
                result = {}
                
                # Handle strings and integers directly into the dictionary (as specified)
                for item_dict in data.values():
                    if isinstance(item_dict, str) or isinstance(item_dict, int) or isinstance(item_dict, float):
                        result[item_dict] = True

        except Exception: pass
    
    def save(self, filename=None):
        path_data = "src/" if os.path.exists(filename) else None
        
        try:
            with open(path_data + "/" + self.database_path.lower(), "w") as f:
                json.dump(data, f) # JSON expects object structure for key names in keys()

        except Exception: pass
