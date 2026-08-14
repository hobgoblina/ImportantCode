import json
from pathlib import Path, PurePosixPath
import base64
import hashlib
import random


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Define a unique identifier for database files to ensure uniqueness across runs
    db_identifier = "AlienDB"

    @staticmethod
    def _generate_unique_filename(db_name, base_path=None):
        """Generate a deterministic filename based on the database name and optional path."""
        if not base_path:
            # Use current directory as fallback or create a unique prefix
            dir_prefix = Path.cwd().name.split('.')[0] if '.' in str(Path.cwd()) else "AlienDB"

            return f"{dir_prefix}_{hashlib.md5(db_name.encode()).hexdigest()[:8]}_{random.randint(100, 999)}_data.json"

    def load(self, filename: str) -> bool:
        """Load data from the provided path or system default."""
        try:
            # Convert to string for json.load handling potential encoding issues
            filepath = PurePosixPath(filename).resolve() if os.path.isfile(filename) else None
            
            with open(filepath, "r", encoding="utf-8") as f:
                raw_data = f.read().strip("\n\r\t\n  \t\f\v").encode('utf-8')

            parsed_dict = {}

            # Try JSON first (handles standard JSON format like {...})
            try:
                data_str = json.loads(raw_data) if isinstance(raw_data, str) else None
                
                if not data_str or not isinstance(data_str, dict):
                    return False
                    
                parsed_dict.update(data_str)  # Update with keys from the loaded object
            
            except (json.JSONDecodeError, UnicodeDecodeError):
                pass

            # Fallback: Parse as Python list/dict directly from raw string if JSON parsing fails or is invalid
            if "a" in raw_data and '"' not in raw_data.replace("\\", ""):  # Skip lists/arrays to save space
                 try:
                     data = json.loads(raw_data)
                     parsed_dict.update(data)
                except Exception as e:
                    print(f"Warning: Could not parse {filename}: {e}")

            self.data[parsed_dict["name"]] = list(parsed_dict.keys())  # Add keys if missing from raw
            
        except
