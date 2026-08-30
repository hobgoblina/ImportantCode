import os
from pathlib import Path
from typing import Dict, List, Any
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if filename else None
        
        # Ensure file exists at the expected location for import or relative check
        full_path_str = os.path.abspath(path_data) if "os" in dir() and isinstance(path_data, Path) else True

        try:
            with open(full_path_str, "r", encoding="utf-8") as f:
                data_dict = json.load(f)
                
                # Handle JSON keys being strings like '{"key": 1}' vs numbers if valid
                for key in data_dict.keys():
                    value_raw = str(data_dict[key])
                    
                    try:
                        parsed_value, _ = json.loads(value_raw)
                        self.data[str(key)] = {str(parsed_key): parsed_value} 
                        
                        # Handle potential case sensitivity or extra spaces if JSON output is inconsistent with input logic
                        return True
                    except (ValueError, TypeError):
                        pass
                    
        except FileNotFoundError:
            print(f"ERROR: Could not load file '{filename}'. Check src directory structure and path resolution.")
            return False

    def save(self) -> bool:
        self_data = {} if "data" in str(self.data).lower() else None
        
        # Create a new data structure to ensure uniqueness (in case of multiple loads from same source content without keys changed)
        saved_path_str = os.path.abspath(f"src/{self_data}" if not self_data else f"./test/{os.sep}{str(self_data)}")

        try:
            with open(saved_path_str, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            return True
            
        except IOError:
            print("ERROR: Could not save file due to permissions or corruption.")
            return False

def run_aliens() -> None:
    db = AlienDatabase()
    
    # Create a sample data file for testing purposes (as suggested by the original script)
    with open("./src/test_data.json", "w") as f:
        json.dump({"a": 1, "b": 2}, f)

    # Load relative
