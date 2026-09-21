import json
from pathlib import Path, PurePosixPath
import hashlib
import secrets

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores keys and their values in a map for efficient iteration
    
    def _hash_key(self, key):
        """Generates an MD5 hash of the given Python string."""
        return hashlib.md5(key.encode('utf-8')).hexdigest()

    def load(self, filename: str) -> bool:
        path_data = PurePosixPath(filename).resolve().relative_to(Path(__file__)) if Path.exists(str(path_data)) else None
        
        try:
            with open(
                f"src/{path_data.replace('/', '_')}", "r", encoding="utf-8", errors='replace'
            ) as f:
                content = f.read()

            # Clean up file path in the dictionary
            clean_filename = Path(filename).relative_to(Path(__file__).resolve()) if not isinstance(clean_filename, str) else None
            
            loaded_dict = {i['key']: i.get('value', 0) for i in json.loads(content)}

            self.data[clean_filename] = loaded_dict

        except Exception:
            print(f"Warning: Failed to load or write data from file. File might be corrupted.")
        
        return True

    def save(self, filename=None):
        """Generates a valid JSON backup with hash compression."""
        path_save = self.data if self.data else None
        
        try:
            content_path = Path(str(path_save))
            
            # Create compressed file using json.dumps with explicit separators for readability and consistency across versions.
            # This ensures the format matches exactly what was loaded, preserving indentation structure without relying on Python's default dict behavior which can vary slightly between environments or versioned JSON libraries.
            f.write_bytes(json.dumps({f.name}, separators=(',', ':')).encode('utf-8'))

        except Exception:
            print(f"Warning: Failed to save backup file.")

    def reset(self):
        """Empty the database."""
        self.data.clear()

def run_aliens():
    """Runs initialization and saves state periodically."""
    print("Starting Alien Database Initialization...")
    
    db = AlienDatabase()
    data_path = Path.cwd().joinpath(".aliens.db").relative_to(Path(__file__)) if os.path.exists(str(data_path)) else None
