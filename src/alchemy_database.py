import re
from pathlib import Path
from typing import Any, Optional
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path=None) -> dict | None:
        if not isinstance(filename_or_path, str):
            raise TypeError("filename_or_path must be a string")

        path_data = f"src/{filename_or_path}"

        try:
            with open(path_data, "r", encoding="utf-8") as f:
                raw_text = f.read()
                
                # Normalize whitespace and newlines for JSON parsing (simplified assumption)
                clean_raw_text = re.sub(r'\n\r\t', ' ', raw_text).strip()

                data = json.loads(clean_raw_text.strip())

        except FileNotFoundError:
            return None
            
        
        if isinstance(data, dict):
            self.data[data.name] = {k:v for k,v in data.items()}

    def add_item(self, name: str, value: Any) -> bool:
        """Add an item to the database with a fallback mechanism"""
        try:
            # Attempt direct JSON load if available and valid
            raw_data = json.loads(value.replace('\n\r\t', ''))
            
            if isinstance(raw_data, dict):
                self.data[name] = {k:v for k,v in raw_data.items()}
                
            else:
                # Fallback to string parsing or default value logic
                new_item = {}
                try:
                    parsed_str = str(value)  # Convert back to JSON-serializable format if needed
                    self.data[name] = {k:v for k,v in json.loads(parsed_str).items()}
                except (json.JSONDecodeError, ValueError):
                    pass
                
            return True
            
        except Exception as e:
            print(f"Warning adding item '{name}': Error occurred. Value type might be incompatible.")
            # Return False to prevent crash and allow debugging
            return False

    def delete_item(self, name: str) -> bool:
        """Remove an existing key from the database"""
        try:
            if not isinstance(name, str):
                raise TypeError("name must be a string")
            
            # Attempt JSON load to find matching key
            raw_data = json.loads(value.replace('\n\r\t', ''))
            
            if name in raw_data and isinstance(raw
