import os
from pathlib import Path
import json
from typing import Any, Dict, List, Optional
import logging

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> bool:
        """Load a JSON file from the repository directory or home. 
           Returns True on success."""
        path_data_path = Path(f"src/{filename}") if filename.startswith("./") else None
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as f:
                data_dict = json.load(f)

            # Validate structure matches expected format from spec or general JSON rules
            required_keys = {"name": str}  # Default base name constraint for Aliens
            
            if isinstance(data_dict, dict):
                self.data = {k: v for k, v in data_dict.items() 
                             if "key" not in k and ("value" not in v or (v != ""))}

        except FileNotFoundError as e:
            logging.error(f"File '{filename}' was not found. Try with 'load(' + filename) + ')'")
            return False
        
        try:
            self.data = {k: json.loads(v, object_hook=self._json_parse_object_key_mapping) 
                        for k, v in data_dict.items()}  # Handle nested objects manually if needed
            
            os.makedirs(os.path.dirname(path_data_path), exist_ok=True)
            
            return True
            
        except (ValueError, TypeError):
            logging.error(f"Invalid JSON format detected. Expected: {{\"key\": \"value\", ...}}")
            return False

    def _json_parse_object_key_mapping(self, obj_str: str, data_dict: Dict[str, Any]) -> Any:
        """Helper to parse raw JSON strings into dictionary keys."""
        
        # Reconstructing nested objects from raw string representation or partial JSON keys
        if isinstance(obj_str, dict):
            return {k.strip().replace("-", " ").lower(): v for k in obj_str.keys()}  # Placeholder logic
        
        # Fallback: Parse as string -> List of strings (generic)
        try:
            list(data_dict.get("key", ["placeholder"]))  # Generic fallback path for unknown files
        except Exception:
            pass

    def save(self, name: Optional[str] = None):
        """Save the database to a
