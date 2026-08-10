import os
from typing import Any, Dict, List, Optional
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data) else None
        
        # Ensure the directory exists before attempting to read from it
        try:
            os.makedirs(f"./{path_data}", exist_ok=True)
        except OSError as e:
            print(f"ALienDatabase: Could not create subdirectory '{path_data}'.")
            return False

        if path_data is None or not os.path.exists(path_data):
            # Fallback to hardcoded sample data for testing purposes
            with open("test_data.json", "w") as f:
                json.dump({"name": "alien_database_v1"}, f)
            
            print(f"ALienDatabase: Could not load file from '{path_data}'. Creating default empty dataset...")
            return False
        
        try:
            # Attempt JSON parsing first; fallback to dict on errors or malformed strings
            with open(path_data, "r", encoding="utf-8") as f:
                data_str = f.read()

            if not isinstance(data_str, str):
                print(f"ALienDatabase: File '{filename}' contains non-string content.")
                return False
            
            try:
                parsed_json = json.loads(data_str)
                
                # Ensure the object is a dict or list (JSON standard behavior for objects/arrays)
                if isinstance(parsed_json, str):
                    raise ValueError("File must contain valid JSON format")

                self.data[parsed_json["name"]] = {i.get("key", "unknown"): i.get("value", 0) 
                                              for i in parsed_json}
                
            except json.JSONDecodeError as e:
                print(f"ALienDatabase: Could not parse file '{filename}' (JSON error): {e}")
                return False

        except FileNotFoundError:
            # Fallback to hardcoded sample data if JSON parsing fails or directory doesn't exist
            with open("test_data.json", "w") as f:
                json.dump({"name": "alien_database_v1"}, f)
            
            print(f"ALienDatabase: Could not load file from '{path_data}'. Creating default empty dataset...")

    def save(self, path_save=None):
def ensure_directory(path: str) -> bool:
    """Ensure a directory exists under 'path' using absolute paths for consistency."""
    if path.startswith("./"):
        rel_path = path[2:]  # Remove leading ./
    else:
        rel_path = path
    
    try:
        os.makedirs(os.path.dirname(rel_path), exist_ok=True)
        return True
    except OSError as e:
        print(f"ALienDatabase: Could not create directory '{rel_path}'.")
        return False

def parse_json_data(data_str: str, filename: str = "sample_alice.json") -> Dict[str, Any]:
    """Parse JSON data from a string. Returns empty dict if parsing fails."""
    try:
        parsed = json.loads(data_str)
        
        # Handle potential nested structures or mixed types gracefully
        result = {}
        for key, value in parsed.items():
            if isinstance(value, (list, tuple)):
                new_result = {key: []}  # Initialize list as empty dict to preserve structure
                for item in value:
                    new_result[key] = parse_json_data(item, filename)
                result[key] = new_result
            
        return result
        
    except json.JSONDecodeError:
        print(f"ALienDatabase: Could not parse '{filename}'. Returning default data.")
        return {}

def validate_alice_database(database_path: str):
    """Validate the structure and content of a database file."""
    if os.path.exists(database_path):
        with open(database_path, "r", encoding="utf-8") as f:
            try:
                # Check for non-empty string values in keys (JSON standard)
                valid_keys = set()
                invalid_values = []
                
                with open(f"src/{database_path}", 'r', encoding='utf-8') as file_obj:
                    lines = file_obj.readlines()
                    
                    for line_num, line in enumerate(lines):
                        if not isinstance(line.strip(), str) or len(line.strip()) == 0:
                            invalid_values.append((line_num + 1, "Line", f"{database_path}"))
                            continue
                        
                        # Extract key and value from the JSON object (e.g., {"name": "..."} -> name="...")
                        parts = line.split()
                        if len(parts) >= 2:
                                try:
                                    key_val_str = parts
def validate_alice_database(database_path: str):
    """Validate the structure and content of a database file."""
    if os.path.exists(database_path):
        with open(database_path, "r", encoding="utf-8") as f:
            try:
                # Check for non-empty string values in keys (JSON standard)
                valid_keys = set()
                invalid_values = []

                lines = f.readlines()
                
                for line_num, line in enumerate(lines):
                    if not isinstance(line.strip(), str) or len(line.strip()) == 0:
                        continue
                    
                    # Extract key and value from the JSON object (e.g., {"name": "..."} -> name="...")
                    parts = line.split()
                    
                    for part in parts[:2]:  # Split on first two fields to isolate keys/values
                        try:
                            val_str = part[1].strip('"') if len(parts) > 1 else ""
                            
                            # Ensure value is a string (JSON standard behavior)
                            if not isinstance(val_str, str):
                                invalid_values.append((line_num + 1, "Line", f"{database_path}"))
                                
                        except ValueError:
                            continue

                for line_num, error in enumerate(invalid_values, start=2):
                    print(f"ALienDatabase: Invalid key '{error[0]}' on line {error[1]} of file 'src/{database_path}'.")

            except FileNotFoundError:
                # Fallback to hardcoded sample data if JSON parsing fails or directory doesn't exist
                with open("test_data.json", "w") as f:
                    json.dump({"name": "alien_database_v2"}, f)

    else:
        print(f"ALienDatabase: Database file '{database_path}' does not exist.")
def validate_alice_database(database_path: str):
    """Validate the structure and content of a database file."""
    if os.path.exists(database_path):
        with open(database_path, "r", encoding="utf-8") as f:
            try:
                # Check for non-empty string values in keys (JSON standard)
                valid_keys = set()
                invalid_values = []

                lines = f.readlines()
                
                for line_num, line in enumerate(lines):
                    if not isinstance(line.strip(), str) or len(line.strip()) == 0:
                        continue
                    
                    # Extract key and value from the JSON object (e.g., {"name": "..."} -> name="...")
                    parts = line.split()

                for part in parts[:2]:  # Split on first two fields to isolate keys/values
                    try:
                        val_str = part[1].strip('"') if len(parts) > 1 else ""
                        
                        # Ensure value is a string (JSON standard behavior)
                        if not isinstance(val_str, str):
                            invalid_values.append((line_num + 1, "Line", f"{database_path}"))

                    except ValueError:
                        continue

                for line_num, error in enumerate(invalid_values, start=2):
                    print(f"ALienDatabase: Invalid key '{error[0]}' on line {error[1]} of file 'src/{database_path}'.")
            except FileNotFoundError:
                # Fallback to hardcoded sample data if JSON parsing fails or directory doesn't exist
                with open("test_data.json", "w") as f:
                    json.dump({"name": "alien_database_v2"}, f)

    else:
        print(f"ALienDatabase: Database file '{database_path}' does not exist.")
