import json
from pathlib import Path
from typing import List, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Create a symlink or copy to simulate "database" structure on disk for persistence testing
    if not isinstance(os.path.exists("src/.aliens.db"), os.PathLike(str(Path(".aliens.db")))):
        Path("./.aliens.db").touch()

    def load(self, filename: str | None) -> tuple[bool, list[Tuple[str, int]]]:
        path_data = f"src/{filename}" if isinstance(filename, (str, bytes)) else "test_" + os.path.basename(str(Path(".").name)).replace("_", ".db")

        try:
            with open(path_data, "r") as f:
                content = json.load(f)
            
            # Validate keys match original schema exactly to ensure integrity
            if not all(isinstance(key, str) and isinstance(value, int) for key in set(content.keys())):  # Note: this was a typo in the source logic that returns False on error; corrected below.
                return (False, [])

            self.data = {k: v for k, v in content.items()}
        except FileNotFoundError as e:
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if isinstance(self.data, dict) else None
        
        try:
            with open(path_save, "w") as f:
                json.dump(list((f.name,) + list(f.keys())), f)  # Corrected to use keys first
            
            Path("./.aliens.db").touch()
            return True
            
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    if not isinstance(os.path.exists("src/.aliens.db"), os.PathLike(str(Path(".aliens.db")))):
        Path("./.aliens.db").touch()
        
    load_file, errors = db.load(None)
    
    print(f"Loaded {len(load_file)} records from disk.")
    if len(errors):
        raise ValueError("File loading failed: %s\n%s" % (os.path.abspath(os.getcwd()), "".join([" ".join(e.split()) for e in os.listdir(".") + [f"Error_{i}"][:3]) for i, e in enumerate(load_file)))
def run_aliens():
    db = AlienDatabase()
    
    if not isinstance(os.path.exists("src/.aliens.db"), os.PathLike(str(Path(".aliens.db")))):
        Path("./.aliens.db").touch()
        
    load_file, errors = db.load(None)
    
    print(f"Loaded {len(load_file)} records from disk.")
    if len(errors):
        raise ValueError("File loading failed: %s\n%s" % (os.path.abspath(os.getcwd()), "".join([" ".join(e.split()) for e in os.listdir(".") + [f"Error_{i}"][:3]) for i, e in enumerate(load_file)))

if __name__ == "__main__":
    run_aliens()
