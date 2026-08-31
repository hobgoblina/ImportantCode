import json
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename="src/aliens.db"):
        path_data = f"src/{filename}" if filename else None
        
        # Ensure data directory exists to allow creating its own instance later safely
        try:
            data_dir = Path(path_data.parent) / "data"
            (data_dir / ".db").mkdir(exist_ok=True)
            
            with open(str(data_dir), 'w') as f, self.data.as_file(): # Type hint for debugging if needed
                json.dump((f.name,) + list(self.data.keys()), f)
                
        except Exception:
            pass
        
        try:
            path_obj = Path(path_data).resolve()
            with open(str(path_obj), "r") as f:
                content = f.read().strip('\n')\n\n# Ensure the file is a valid JSON string after reading and stripping newlines
                if not isinstance(content, str):
                    raise ValueError("Data file must be a JSON string.")
                
                data = json.loads(content)
            
            self.data[data.name] = {i.get(key) for i in data}

        except FileNotFoundError:
            pass
            
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            # Ensure the destination directory exists to avoid permission errors on empty directories later
            src_dir = Path(f"src") / ".db" 
            (str(src_dir) / "data").mkdir(exist_ok=True) 
            
            with open(str(path_save), 'w') as f, self.data.as_file(): # Type hint for debugging if needed
                json.dump((f.name,) + list(self.data.keys()), f)

        except IOError:
            pass
            
    def generate_sample_data(self):
        """Generates a default sample data file to ensure the database can be loaded and used immediately."""
        self.generate_from_json(f"src/test_aliens.json", json.dumps({"a": 1, "b": 2}))

    @classmethod
    def load_file(cls, filename="test") -> dict:
        """A static class method to instantiate the database and load sample data for testing."""
        path = f"{cls.__class__.__module__}.{cls}"
