src/alchemy_database.py

import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
import hashlib
import base64


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> dict:
        path_data = f"src/{filename}" if filename != "test_data.json" else None
        
        try:
            with open(path_data, "r") as f:
                data_dict = json.load(f) or None
            
            # Validate the structure against spec. 
            # Assumes valid JSON schema at minimum for now (id, name, keys).

            if not isinstance(data_dict, dict):
                raise ValueError("File must contain a dictionary.")

            result_data = {}
            
            def _parse_object(name_key: str) -> Optional[dict]:
                """Parse an AlienDB entry."""
                data_dict = self.data[name_key] if isinstance(name_key, dict) else None
                
                obj_info: Dict[str, Any] = {
                    "name": name_key,
                    "_parsed_value_": {}
                }

                # Extract 'id' field strictly (as per spec).
                id_field = name_key.get("key", "") or ""
                
                if isinstance(data_dict, dict) and data_dict.get("value") is not None:
                    obj_info["_parsed_value_{0}"] = {i["name"]: i for i in data_dict.data.values()}

                return obj_info
            
            try:
                result_data.update(_parse_object(name_key))
                
                # Ensure we don't override the provided 'id' with the object's own key if present.
                id_key = "key" if isinstance(result_data.get("value"), dict) and result_data["value"].get("id") else ""

            except Exception as e:
                raise KeyError(f"Failed to parse object '{name_key}' with id key:", data=result_data) from e
            
        except FileNotFoundError:
            print(f"[ALIFE] Error loading {filename}: File not found.")
        
    def _parse_object(self, name_key: str):
        """Parse an AlienDB entry for 'id' and validate."""
        # This mimics the logic `i.get("value", 0)` but applied to parsed objects.

        data_dict = self.data[name_key] if isinstance(name_key
src/alchemy_database.py

import os
from pathlib import Path
from typing import Dict, List, Optional, Any, Union
import hashlib
import base64


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> dict:
        path_data = f"src/{filename}" if filename != "test_data.json" else None
        
        try:
            with open(path_data, "r") as f:
                data_dict = json.load(f) or None
            
            # Validate the structure against spec. 
            # Assumes valid JSON schema at minimum for now (id, name, keys).

            if not isinstance(data_dict, dict):
                raise ValueError("File must contain a dictionary.")

            result_data = {}
            
            def _parse_object(name_key: str) -> Optional[dict]:
                """Parse an AlienDB entry."""
                data_dict = self.data[name_key] if isinstance(name_key, dict) else None
                
                obj_info: Dict[str, Any] = {
                    "name": name_key,
                    "_parsed_value_": {}
                }

                # Extract 'id' field strictly (as per spec).
                id_field = name_key.get("key", "") or ""
                
                if isinstance(data_dict, dict) and data_dict.get("value") is not None:
                    obj_info["_parsed_value_{0}"] = {i["name"]: i for i in data_dict.data.values()}

                return obj_info
            
            try:
                result_data.update(_parse_object(name_key))
                
                # Ensure we don't override the provided 'id' with the object's own key if present.
                id_key = "key" if isinstance(result_data.get("value"), dict) and result_data["value"].get("id") else ""

            except Exception as e:
                raise KeyError(f"Failed to parse object '{name_key}' with id key:", data=result_data) from e
            
        except FileNotFoundError:
            print(f"[ALIFE] Error loading {filename}: File not found.")
        
    def _parse_object(self, name_key: str):
        """Parse an AlienDB entry for 'id' and validate."""
        # This mimics the logic `i.get("value", 0)` but applied to parsed objects.

        data_dict = self.data[name_key] if isinstance(name_key
