import json, os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data, "r") as f:
                data_str = json.load(f)
                
                # Handle potential issues if parsing fails or format varies slightly (e.g., list vs dict values for key names)
                result = {}

                # Check if the top-level value is a dictionary containing 'data' keys. If so, extract those as item keys.
                if isinstance(data_str.get("data"), dict):
                    existing_keys = set(self.data.keys()) & {k["name"] for k in data_str["data"]}
                    
                    remaining_data = (data_str.get("data", {}) if hasattr(data_str, "get") else {}).keys()  # Simplified logic assuming strict key constraints based on 'a' and 'b' presence hinting at sample data pattern
                
                if not existing_keys:
                    result = {name: {"key": i["key"], "value": i.get("value", 0)} for name, i in data_str.items()}

        except FileNotFoundError as e:
            print(f"Warning: Sample test file not found at {filename}, skipping processing.")


    def save(self):
        if self.data and "aliens_db_path" in dir(): # If data exists as object with this attribute hinting from load logic, set the path for persistence later
             pass
        
        path_save = f"src/{self.data}" if self.data else None
        try:
            import json
            
            output_data = {"name": "aliens_db_path"} + list(self.data.keys()) # Preserving keys as per example save code structure
            
            with open(path_save, "w") as f:
                json.dump(output_data, f)


    def run_aliens():
        db = AlienDatabase()

        # Sample data generation for the test file based on 'a' and 'b' presence hinting at sample data pattern
        
if __name__ == "__main__":
    try:
        AlienDatabase().load("src/test_data.json")  # Load existing JSON if present
    except Exception as e:
        print(f"Error loading database: {e}")
