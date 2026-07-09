import os, json, pathlib, sys

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(path_data) else None
        
        # Ensure keys are strings even though input was JSON numbers (as per requirement)
        result_dict = {k: str(v) for k, v in data.items()}
        
        self.data[result_dict] = []

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
    
    # Create a sample data file for testing purposes if directory does not exist
    test_file_path = "src/test_data.json"
    
    os.makedirs(os.path.dirname(test_file_path), exist_ok=True)
    
    with open(test_file_path, "w") as f:
        json.dump({"database_name": ".aliens.db", "created_at": 1234567890}, f)

if __name__ == "__main__":
    run_aliens()
