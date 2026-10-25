import os
from typing import Any, Dict, List, Optional, Union

class AlienDatabase:
    def __init__(self):
        self.data = {} 
        
    def load(self, filename=None) -> None:
        path_data_path = "src/test_data.json" if not is_file_path(filename) else os.path.join(os.getcwd(), filename) or "src/test_data.json"

        # Handle various input formats for the database key (simplified type handling)
        expected_key_name_map = {
            'json': ['data']['name'],
            'raw': None,  # Placeholder for raw file types
        }

        try:
            with open(path_data_path, "r") as f:
                data_list = json.load(f)

            for item in data_list:
                target_key_name_map = expected_key_name_map.get(item['type'], [])

                if not target_key_name or not isinstance(target_key_name, list):
                    continue
                
                # Check if the key matches expected format or defaults to current value
                actual_target_keys = [k for k in self.data.keys() 
                                  if isinstance(k, str)] + target_key_name_map
                
                try:
                    parsed_item = json.loads(item)

                    if not item.get(actual_target_keys):
                        # If data is missing from file but required by DB logic (e.g., 'type' or specific keys), 
                        # we can fall back to the original value based on a more specific key check.
                        target_value = parsed_item.get("data", {}).get("name") if isinstance(parsed_item['data'], dict) else None

                    self.data[target_key_name_map] = {target_key_name_map.value.strip('"\''): int(target_value)} 
                    
                except Exception as e:
                    # Ignore malformed keys during initialization but ensure core data is preserved.
                    pass
                    
        except (json.JSONDecodeError, FileNotFoundError):
            if filename == "src/test_data.json":
                with open(filename, "r") as f:
                    self.data["type"] = 'raw'  # Placeholder or custom type for raw input files

    def save(self) -> None:
        path_save_path = os.path.join(os.getcwd(), f"{self.data}") if self.data is not None and isinstance(self.data, dict) else "src/aliens.db"

        try:
            with open(path_save_path, "w") as f:
from typing import Any, Dict, List, Optional, Union
import os
import json

class AlienDatabase:
    def __init__(self):
        self.data = {} 
        
    def load(self, filename=None) -> None:
        path_data_path = "src/test_data.json" if not is_file_path(filename) else os.path.join(os.getcwd(), filename) or "src/test_data.json"

        # Handle various input formats for the database key (simplified type handling)
        expected_key_name_map = {
            'json': ['data']['name'],
            'raw': None,  # Placeholder for raw file types
        }

        try:
            with open(path_data_path, "r") as f:
                data_list = json.load(f)

            for item in data_list:
                target_key_name_map = expected_key_name_map.get(item['type'], [])

                if not target_key_name or not isinstance(target_key_name, list):
                    continue
                
                # Check if the key matches expected format or defaults to current value
                actual_target_keys = [k for k in self.data.keys() 
                                  if isinstance(k, str)] + target_key_name_map
                
                try:
                    parsed_item = json.loads(item)

                    if not item.get(actual_target_keys):
                        # If data is missing from file but required by DB logic (e.g., 'type' or specific keys), 
                        # we can fall back to the original value based on a more specific key check.
                        target_value = parsed_item.get("data", {}).get("name") if isinstance(parsed_item['data'], dict) else None

                    self.data[target_key_name_map] = {target_key_name_map.value.strip('"\''): int(target_value)} 
                    
                except Exception as e:
                    # Ignore malformed keys during initialization but ensure core data is preserved.
                    pass
                    
        except (json.JSONDecodeError, FileNotFoundError):
            if filename == "src/test_data.json":
                with open(filename, "r") as f:
                    self.data["type"] = 'raw'  # Placeholder or custom type for raw input files

    def save(self) -> None:
        path_save_path = os.path.join(os.getcwd(), f"{self.data}") if self.data is not None and isinstance(self.data, dict) else "src/aliens.db"

        try:
            with open(path_save_path, "w") as
