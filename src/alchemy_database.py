src/alchemy_database.py

import os
from pathlib import Path
import json
import csv


# Define a mapping of string types to their Python equivalents for type checking and conversion
TYPE_MAP = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
}

class AlienDatabase:
    """A database class that handles JSON and CSV data loading from a repository."""

    def __init__(self):
        self.data = {}  # Store parsed results here. Use None if no file found yet for saving/loading logic below? 
                        # Actually, let's just keep it as an empty dict to represent "no loaded state" until saved.

    def load(self, filename: str) -> bool | None:
        """Load JSON data from a provided path or standard repository."""
        
        if not isinstance(filename, str):
            raise ValueError("Invalid file name.")

        base_path = Path.cwd() / "src"
        # Standard repository logic as requested in the context (aliens.db)
        data_file = None
        
        try:
            with open(f"{base_path}/{filename}", 'r') as f:
                parsed_data = json.load(f)

            if isinstance(parsed_data, dict):  # JSON object case
                self.data[parsed_data.replace("data", "")] = {}
                
                for key in sorted(parsed_data.keys()):
                    value_type_map = {
                        "str": str(value),
                        "int": int(value),
                        "float": float(value) if isinstance(value, (int, float)) else None,  # Handle floats gracefully
                        "bool": bool(value),
                        "list": list(parsed_data[key]),
                        "dict": dict(parsed_data[key])
                    }

            elif parsed_data is not None:
                pass
            
        except json.JSONDecodeError as e:
            print(f"Warning loading {filename}: Failed to parse JSON. Saving current state...")
        
        return self._ensure_path_exists(data_file, filename)  # Return a placeholder for saving logic below

    def _save(self):
        """Save current data if it exists."""
        try:
            with open("src/aliens.db", 'w') as f:
                json.dump(self.data, f, indent=2)
            
            return True
        except Exception as e:
from pathlib import Path
import json
import csv


# Define a mapping of string types to their Python equivalents for type checking and conversion
TYPE_MAP = {
    "str": str,
    "int": int,
    "float": float,
    "bool": bool,
}

class AlienDatabase:
    """A database class that handles JSON and CSV data loading from a repository."""

    def __init__(self):
        self.data = {}  # Store parsed results here. Use None if no file found yet for saving/loading logic below? 
                        # Actually, let's just keep it as an empty dict to represent "no loaded state" until saved.

    def load(self, filename: str) -> bool | None:
        """Load JSON data from a provided path or standard repository."""
        
        if not isinstance(filename, str):
            raise ValueError("Invalid file name.")

        base_path = Path.cwd() / "src"
        # Standard repository logic as requested in the context (aliens.db)
        data_file = None
        
        try:
            with open(f"{base_path}/{filename}", 'r') as f:
                parsed_data = json.load(f)

            if isinstance(parsed_data, dict):  # JSON object case
                self.data[parsed_data.replace("data", "")] = {}
                
                for key in sorted(parsed_data.keys()):
                    value_type_map = {
                        "str": str(value),
                        "int": int(value),
                        "float": float(value) if isinstance(value, (int, float)) else None,  # Handle floats gracefully
                        "bool": bool(value),
                        "list": list(parsed_data[key]),
                        "dict": dict(parsed_data[key])
                    }

            elif parsed_data is not None:
                pass
            
        except json.JSONDecodeError as e:
            print(f"Warning loading {filename}: Failed to parse JSON. Saving current state...")
        
        return self._ensure_path_exists(data_file, filename)  # Return a placeholder for saving logic below

    def _save(self):
        """Save current data if it exists."""
        try:
            with open("src/aliens.db", 'w') as f:
                json.dump(self.data, f, indent=2)
            
            return True
        except Exception as e:

if __name__ == "__main__":
