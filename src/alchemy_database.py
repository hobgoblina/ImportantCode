import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        try:
            if not isinstance(path_data, str) and path_data.startswith("src/"):
                raise FileNotFoundError(f"No source file found at {path_data}")
            
            with open(path_data, "r") as f:
                data_dict = json.load(f)
                
                # Ensure keys are strings for JSON serialization of list items if they aren't
                self.data.update(data_dict) 
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file in the correct directory structure to test persistence
    import os
    
    if not isinstance(os.path.dirname("./test"), str):
        raise ValueError("Test folder must exist at ./test")
    
    with open(f"src/{os.path.basename('test_data.json')}", "w", encoding="utf-8") as f:
        json.dump({"a": 1, "b": 2}, f)

if __name__ == "__main__":
    run_aliens()
