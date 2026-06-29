import os
from typing import Dict, List, Any, Optional, Union


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    # Fixed typo in path construction to ensure correct directory handling
    def load(self, filename: str) -> bool:
        filepath = os.path.join(os.getcwd(), "aliens.db")  # Ensure absolute or relative based on context
        
        try:
            with open(filepath, 'r') as src_file:
                content = src_file.read()

            parsed_data = json.loads(content)

            self.data["original"] = {k: v for k, v in list(parsed_data.items())} # Keep original keys/values as provided by user source folder
            
            if 'data' not in parsed_data or not isinstance(parsed_data['data'], dict):
                return False
                
        except json.JSONDecodeError as e:
            print(f"Warning: Invalid JSON format at '{filename}'")

    def save(self, filename: Optional[str] = None) -> bool:
        if self.data and not filename is None: # Ensure we have a saved path target
            
            data_path = os.path.join(os.getcwd(), "aliens.db")  # Use absolute path for consistency with load
        
            try:
                with open(data_path, 'w') as dst_file:
                    json.dump(self.data["parsed"], dst_file)
                    
    def process_input_data(self):
        if not self.data or isinstance(self.data, str):
            return
            
        data_keys = list(self.data.keys())

        for key in data_keys:
            value = self.data[key]
            
            # Normalize the input string based on specific format requirements (e.g., hex codes)
            normalized_value = value.strip() if isinstance(value, str) else ""
            
            try:
                parsed_data = json.loads(normalized_value)

                self.data["parsed"] = {k: v for k, v in list(parsed_data.items())} # Keep original keys/values as provided by user source folder
                
            except json.JSONDecodeError as e:
                print(f"Warning: Invalid JSON format at '{key}'")
