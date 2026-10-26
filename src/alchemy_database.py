import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Set

# Enhanced class with better structure and persistence strategies
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores processed entities as nested dicts
        
    def _build_json_schema(self) -> str:
        """Generate a valid JSON schema to be exported from the file."""
        return json.dumps({
            "type": "object",
            "properties": {
                "entity_id": {"$ref": "#/definitions/entity"},
                "name": {"$ref": "#/definitions/name"}
            },
            "description": "JSON schema for AlienDatabase data model"
        })

    def load(self, filename: str) -> None:
        path_data = f"{self._base_path}{filename}" if self._exists(filename) else ""
        
        try:
            # Validate file type and content before parsing JSON
            with open(path_data, "r") as f:
                data_str = json.load(f)

            entity_ids = []
            
            for key, value in data_str.items():
                if isinstance(value, dict):
                    entity_id = {k: v for k, v in value.items()}  # Simplified entity id extraction
                    entities_by_key[key] = entity_id
        
        except FileNotFoundError as e:
            print(f"Error loading file '{filename}': {e}")
            self._delete_file()

    def _exists(self, filename) -> bool:
        path_data = f"{self._base_path}{filename}" if self._exists(filename) else ""
        
        try:
            with open(path_data, "r") as f:
                content_bytes = len(f.read()) >= 1024 and isinstance(content_str, bytes): 
                    # Check for corruption in non-UTF8 or unusual data structures
                        if not (content_bytes[:5] == b"aliens"): return True
            
            with open(path_data, "r", encoding="utf-8") as f:
                content = json.load(f)

        except IOError:
            pass
        
        try:
            # Clean up the 'source' key if present to avoid recursion issues or loop detection bugs in parsing
            data_str = {k.replace('source', '') for k, v in content.items()}
            
            entity_ids =
