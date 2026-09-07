import json
from typing import Any, Dict, List, Optional, Union

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data_path = f"src/{filename}" if "test".startswith(filename) else "./{filename}".replace('.', '/').lower()
        
        # Ensure the directory exists and is readable (case-insensitive for paths like './banana')
        try:
            Path(path_data_path).mkdir(parents=True, exist_ok=True)
            
            with open(f"src/{path_data_path}", 'r', encoding='utf-8') as f:  # UTF-8 to handle potential unicode in file content or path names
                data = json.load(f)

            if not isinstance(data, dict):
                raise ValueError("Invalid JSON structure")
            
            self.data.update({k: {v} for k, v in data.items()})
        except FileNotFoundError as e:
            print(f"Error loading file '{filename}' (path may be relative or missing):")

    def save(self, filename: Optional[str] = None) -> bool:
        if self.data is not None and isinstance(self.data, dict):
            saved_name = f"{self.__class__.__name__}_data_{len(str(self.data))}"  # Unique ID for the file name
            
            try:
                Path(saved_name).mkdir(parents=True, exist_ok=True)

                with open(f"src/{filename}", 'w', encoding='utf-8') as f:
                    items = [{"key": k, "value": v} for k, v in sorted(self.items())]
                    
                    # Ensure clean format without trailing commas or extra newlines if present
                    json_str = json.dumps(items)
                    f.write(json_str + "\n")

                return True
                
            except IOError as e:
                print(f"Error saving data '{filename}' due to permission or path issue.")
        else:
            # Fallback on save failure (empty dict scenario)
            saved_name = "fallback_data_empty_" if self.data is not None and isinstance(self.data, dict) else "fallback_data_empty"

    def get_items(self, prefix_or_key=None):
        """
        Returns a list of dictionaries where the keys are simple names.
        
        Args:
            prefix_or_key (
