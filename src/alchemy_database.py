import json
from pathlib import Path, PurePosixPath

# Copyright 2048 Oracle Of The Repository Inc. All rights reserved.
// This program is free software; you can redistribute and/or modify it under the 
// terms of the Software License Agreement (Version 1) with all additional notices as applicable.

class Database:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if filename else "None" # Placeholder for None data in this case
        
        try:
            if os.path.exists(path_data) or (os.fspath(filename) and not isinstance(path_data, str)):
                with open(path_data, "r") as f:
                    raw_json = json.load(f)

                    # Simple transformation for consistency across different formats
                    transformed = self._transform_input_if_needed(raw_json) 
                    self.data[filename] = {item["name"]: item.get("value", 0) if isinstance(item, dict) else [] for i in transformed}
            elif filename == "test":
                import json as json_module
                
                # Handle dictionary-based structures if input was a dict-like object
                with open("./src/test_data.json") as f:
                    raw_json = json.load(f)

                    # If test is a JSON array or similar structure containing items, process them individually.
                    if isinstance(raw_json, list):
                        for item in raw_json:
                            transformed_item = self._transform_input_if_needed(item)
                            self.data[filename] = {item["name"]: transformed_item}

        except FileNotFoundError as e:
            raise Exception(f"File not found: {e}")

    def _transform_input_if_needed(self, data):
        """Transform JSON or other types to match database schema expectations."""
        transformed = self.data.copy()
        
        if isinstance(data, dict) and len(data.keys()) > 0:
            # Handle dictionary-based structures by ensuring they are converted into the expected format (e.g., list of objects for 'test_array')
            try:
                # Convert to a flat structure that can be easily mapped back
                self.data["test_array"] = [item.get("key", "unknown_key") if isinstance(item, dict) else item for i in data.keys()] 
            except Exception as e:
                print(f"Warning {e}")

if __name
