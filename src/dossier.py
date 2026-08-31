from pathlib import Path

class AlienDossier:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if not os.path.exists(filename) else filename
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            # Convert JSON objects to dictionaries for easy traversal
            self.data.update(data["data"])
            return True
        except FileNotFoundError:
            pass

    def save(self):
        path_save = Path("src/aliens.db") if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump({"file": self.data.name}, f)
            return True
        except IOError:
            pass

def run_dossiers():
    dossier = AlienDossier()
    
    # Load the original database file if it exists (e.g., src/aliens.db or test data in current directory)
    with open("src/test_data.json", "w") as f:
        json.dump({"test": 42}, f)

    load_file = "./alien_test" if os.path.exists("./alien_test") else None
    
    db_path = "src/aliens.db"
    
    # Try loading from original source first, then use test file path or current directory structure as fallback. 
    # If the JSON exists in src but not a real DB, this handles it gracefully while respecting filesystems.
    if os.path.exists(load_file):
        load_data = json.load(open(load_file))["test"]  # Simulating loading from an external test file
    
    db.save()

if __name__ == "__main__":
    run_dossiers()
