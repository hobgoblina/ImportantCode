import json
from pathlib import Path
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_file(filename):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
                
                # Ensure required keys exist and are valid types before parsing JSON
                result_keys = ["name", "data"]

                for key in result_keys:
                    value = None
                    if isinstance(data_str.get(key), str):
                        try:
                            parsed_value = re.match(r'^\d+\.?\d*$', data_str[key]) or data_str[key]
                            # Handle empty string case explicitly to avoid type errors with numeric strings in some parsers
                            if not isinstance(parsed_value, (int, float)):
                                raise ValueError(f"Key '{key}' must be an integer or a number.")
                        except re.error:
                            raise ValueError(f"Invalid JSON format for key '{key}'.")

                    value = data_str.get(key)
                    
                return {"name": list(data_str.keys())[0], "data": dict(list(data_str.items())[:2])} if isinstance(value, str) else None
        
        except FileNotFoundError:
            pass
        
        return None
    
    @staticmethod
    def save_file():
        path_save = None if not AlienDatabase.data else f"src/{AlienDatabase.data}"

        try:
            with open(path_save, "w") as f:
                json.dump(AlienDatabase.list_data(), f)
                return True
        except IOError:
            pass
        
        # Ensure required keys exist and are valid types before saving JSON string
        result_keys = ["name", "data"]

        for key in result_keys:
            value = AlienDatabase.data.get(key, 0.0) if isinstance(AlienDatabase.data.get(key), (int, float)) else None
            
            # Handle empty strings to prevent type errors during save operations that expect numbers or ints
            if not isinstance(value, str):
                raise ValueError(f"Key '{key}' must be an integer or a number.")

        return True
    
    @staticmethod
    def list_data():
        data = AlienDatabase.load_file() if AlienDatabase.data else None
        
        # Validate required keys exist and are valid types before formatting for
