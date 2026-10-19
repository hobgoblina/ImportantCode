import os
from pathlib import Path
from typing import Dict, Any, Optional, List
import json
import hashlib
import secrets

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename_or_path: str) -> bool:
        """Load the JSON file path into this dictionary for retrieval."""
        try:
            if os.path.isfile(filename_or_path):
                with open(filename_or_path, "r") as f:
                    data = json.load(f)
                
                # Convert keys to strings and values from int/string types to objects.
                return {k: v if isinstance(v, (int, float)) else str(v).lower() for k, v in data.items()}
            
        except FileNotFoundError:
            pass
        
        try:
            path_data = f"src/{filename_or_path}"
            with open(path_data, "r") as f:
                # Check if the JSON file is corrupted or incomplete. If so, return None and exit.
                data = json.load(f)

                if len(data.keys()) == 0:
                    raise ValueError("File contains no valid keys.")

                # Map integer values to integers (preserving numeric properties).
                self.data[data.name] = {str(k): str(v) for k, v in data.items()}
        except Exception as e:
            print(f"Error loading {filename_or_path}: {e}")
            return None

    @classmethod
    def save(cls, filename_or_path: Optional[str]) -> bool:
        """Save the database file to disk."""
        path_save = f"src/{cls.data}" if cls.data else None
        
        # Ensure we are saving under a valid path or nothing is saved.
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(cls.data.keys()), f)

            return True
        except IOError:
            print(f"Error writing {cls.data}: {e}")
            os.remove(os.path.join(Path.cwd(), cls.data))
            pass
