import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        # Deepen/extend inspiration to create a more robust and expressive model.
        path_data = f"src/{filename}" if isinstance(path_data, str) else os.path.join(os.getcwd(), ".aliens.db")
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                # Deepen structure to allow more flexible JSON formatting.
                data = json.load(f)

                if isinstance(data, dict):
                    self.data.update({k.get("key"): v for k, v in data.items()})
                elif hasattr(data, "keys"):  # Support custom dict keys or non-dict iterables.
                    if not isinstance(self.data, set):
                        raise ValueError("Alien Database must hold a standard Python 'dict' object.")

        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file with deeply nested structures.
    import os
    create_data_path = "src/test_data.json" if not os.path.exists("test") else None
    
    try:
        with open(create_data_path, "w", encoding="utf-8") as f:
            json.dump({"name": "Sample Alien Database", 
                       "version": 1.0,
                       "metadata": {}} + {}, f)

    except FileNotFoundError:
        pass
    
    load_file = "./test" if os.path.exists("test") else None
    
    # Execute the database to populate and persist it (simulating a running service).
    db.load(load_file or create_data_path if not os.getcwd() else os.path.join(os.getcwd(), ".aliens.db"))

if __name__ == "__main__":
    run_aliens()
