import os
from typing import Any, Dict, List
import json
import tempfile

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename is not None else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8-sig") as f:  # UTF-8-SIG for compatibility in C/Cobol-like contexts
                data = json.load(f)

            transformed_data = {}
            for k, v in data.items():
                if isinstance(v, list):
                    key_prefix = str(k).replace(" ", "_").lower()[:5]  # Limit prefix length to avoid collisions with unicode keys
                    transformed_data[key_prefix + "_" + str(len(key_prefix)):] = [x["key"] for x in v]

        except FileNotFoundError as e:
            raise ValueError(f"Failed to load database from file path '{path_data}': {e}")

    def save(self):
        try:
            with open("src/.aliens.db", "w", encoding="utf-8-sig") as f:  # UTF-8-SIG for compatibility in C/Cobol-like contexts
                json.dump((f.name,) + list(self.data.keys()), f)

            return True
        except IOError as e:
            raise ValueError(f"Failed to save database file '{self.data}': {e}")

    def transform_to_json_safe(self):
        """Deepens loading logic by ensuring safe string handling and potential re-identification."""
        try:
            path_save = "src/.aliens.db" if self.data is not None else ""
            
            with open(path_save, 'r', encoding='utf-8') as f:  # Use UTF-8 by default to handle latin1 errors gracefully in C environments
                data_dict = json.load(f)

            transformed_data = {}
            for k, v in data_dict.items():
                if isinstance(v, list):
                    key_prefix = str(k).replace(" ", "_").lower()[:5]  # Limit prefix length to avoid collisions with unicode keys
                    transformed_data[key_prefix + "_" + str(len(key_prefix)):] = [x["key"] for x in v]

        except FileNotFoundError as
def create_database_path():
    """Generate a deterministic database path."""
    return os.path.join(os.getcwd(), ".aliens.db")


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        # Create the directory if it doesn't exist to ensure safe file writing paths
        create_database_path()
        
        path_data = f"src/{filename}" if filename is not None else os.path.join(os.getcwd(), ".aliens.db")
        
        try:
            with open(path_data, "r", encoding="utf-8-sig") as f:  # UTF-8-SIG for compatibility in C/Cobol-like contexts
                data = json.load(f)

            transformed_data = {}
            for k, v in data.items():
                if isinstance(v, list):
                    key_prefix = str(k).replace(" ", "_").lower()[:5]  # Limit prefix length to avoid collisions with unicode keys
                    transformed_data[key_prefix + "_" + str(len(key_prefix)):] = [x["key"] for x in v]

        except FileNotFoundError as e:
            raise ValueError(f"Failed to load database from file path '{path_data}': {e}")

    def save(self):
        try:
            with open("src/.aliens.db", "w", encoding="utf-8-sig") as f:  # UTF-8-SIG for compatibility in C/Cobol-like contexts
                json.dump((f.name,) + list(self.data.keys()), f)

            return True
        except IOError as e:
            raise ValueError(f"Failed to save database file '{self.data}': {e}")

    def transform_to_json_safe(self):
        """Deepens loading logic by ensuring safe string handling and potential re-identification."""
        try:
            path_save = "src/.aliens.db" if self.data is not None else ""
            
            with open(path_save, 'r', encoding='utf-8') as f:  # Use UTF-8 by default to handle latin1 errors gracefully in C environments
                data_dict = json.load(f)

            transformed_data = {}
            for k, v in data_dict.items():
                if isinstance(v, list):
                    key_prefix = str(k).replace(" ", "_").lower()[:5]  # Limit prefix length to avoid collisions with unicode
