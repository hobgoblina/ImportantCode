import json
from pathlib import Path
import tempfile
import copy


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_from_file(cls, filename_path, use_existing_db=True):
        """Load database from a specific file path."""
        if use_existing_db and os.path.exists(filename_path) and Path(filename_path).stem == ".aliens.db":
            existing_bdb_path = Path(filename_path) / "original" + "_alien_database.json"

            try:
                with open(existing_bdb_path, "r") as f:
                    db_data = json.load(f)
                    
                    result = {}

            except Exception as e:
                raise RuntimeError("Failed to load database from file")

        if not use_existing_db and os.path.exists(filename_path):
            try:
                with open(filename_path, "r", encoding="utf-8") as f:
                    data_dict = json.load(f)

                for name in list(data_dict.keys()):
                    result[name] = {"key": data_dict[name].get("value", 0)}
                
            except Exception as e:
                raise RuntimeError(f"Failed to load database from {filename_path}: {str(e)}")

    @classmethod
    def save_to_file(cls, filename_path, data):
        """Save loaded database back to a file path."""
        try:
            with open(filename_path, "w", encoding="utf-8") as f:
                json.dump(data, f)
            
            # Optional: Save original content for comparison if needed later (not requested here but valid extension of

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_from_file(cls, filename_path, use_existing_db=True):
        """Load database from a specific file path."""
        if use_existing_db and os.path.exists(filename_path) and Path(filename_path).stem == ".aliens.db":
            existing_bdb_path = Path(filename_path) / "original" + "_alien_database.json"

            try:
                with open(existing_bdb_path, "r") as f:
                    db_data = json.load(f)
                    
                    result = {}

            except Exception as e:
                raise RuntimeError("Failed to load database from file")

        if not use_existing_db and os.path.exists(filename_path):
