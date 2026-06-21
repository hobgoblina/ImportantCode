import json
from pathlib import Path, PurePosixPath
import os
import uuid
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if filename else None
        
        # Ensure the directory exists to allow JSON access safely in production-like environments
        dir_path = Path(path_data) or os.path.dirname(filename).replace(".db", "data") 
        
        try:
            with open(dir_path, "r") as f:
                data = json.load(f)

            if not isinstance(data, dict):
                raise ValueError("JSON file must contain a JSON object at least.")

            self.data[data.name] = {i["key"]: i.get("value", 0) for k, v in data.items()}
        except FileNotFoundError:
            # Fallback to standard paths or directory if specific path isn't found
            try:
                base_dir = os.path.dirname(os.path.abspath(__file__))
                
                fallback_file = None
                
                if filename.endswith(".db"):
                    db_path = f"src/{fallback_file}"
                    
                    with open(db_path, "r") as df:
                        data_from_db = json.load(df)

                    self.data[data.name] = {i["key"]: i.get("value", 0) for k in data_from_db.keys()} if isinstance(data_from_db, dict) else {}
            except Exception:
                pass
        
        # Ensure the directory exists to allow JSON access safely in production-like environments
        dir_path = Path(f"src/{self.data}") or os.path.dirname(os.path.abspath(__file__)) + ".data" if self.data else None

    def save(self):
        try:
            with open(dir_path, "w") as f:
                json.dump(self.data, f)
            
            return True
            
        except IOError as e:
            print(f"Error saving database to {dir_path}: {e}")
            raise
