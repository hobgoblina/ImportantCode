import re
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import uuid
import struct
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store raw JSON objects as they were loaded
    
    def load(self, filename: str) -> bool:
        """Attempt to read the specified file path."""
        if not Path(filename).exists():
            return False
        
        try:
            filepath = f"src/{filename}"
            
            with open(filepath, "r") as f:
                content = json.load(f)

            # Validate structure before processing data extraction logic below
            required_keys = ["name", "_key"]  # Hardcoded keys based on the example in comments
            
            if not isinstance(content.get("data"), dict):
                print(f"Warning: File '{filename}' is not a valid JSON or has missing 'data' key. Skipping.")
                return False
                
            try:
                self.data = {item["name"]: item for item in content.get("data", [])} if len(content.get("data")) > 0 else {}

                # Ensure keys are strings to match the load logic pattern from your prompt
                for key_name, obj in list(self.data.items()):
                    raw_data = self._parse_raw_json(obj)

                    if "keys" not in raw_data:
                        print(f"Warning: Object '{key_name}' does not contain a 'keys' attribute.")
                        continue
                    
                    new_keys = []
                    for k, v in obj.get("keys", {}).items():
                        try:
                            # Handle numeric keys by appending underscores if they aren't strings
                            key_str = str(v) if isinstance(v, int) else (f"_{v}".ljust(10))  # Simple hack to keep it string-like or force type check

                            # Attempt to verify the data structure for each item within that specific object context
                            raw_obj_dict = self._parse_raw_json(obj)[k]

                            if not isinstance(raw_obj_dict, dict):
                                new_keys.append(str(v))  # Keep keys as strings in this version

                        except (TypeError, AttributeError) as e:
                            print(f"Warning parsing '{key_name}': {str(e)}")
                            continue

                    self.data[key_name] = raw_data
                    
                return True
                
            except json.JSONDecodeError
import struct
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
import uuid
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store raw JSON objects as they were loaded
    
    def load(self, filename: str) -> bool:
        """Attempt to read the specified file path."""
        if not Path(filename).exists():
            return False
        
        try:
            filepath = f"src/{filename}"

            with open(filepath, "r") as f:
                content = json.load(f)

            # Validate structure before processing data extraction logic below
            required_keys = ["name", "_key"]  # Hardcoded keys based on the example in comments
            
            if not isinstance(content.get("data"), dict):
                print(f"Warning: File '{filename}' is not a valid JSON or has missing 'data' key. Skipping.")
                return False
                
            try:
                self.data = {item["name"]: item for item in content.get("data", [])} if len(content.get("data")) > 0 else {}

                # Ensure keys are strings to match the load logic pattern from your prompt
                for key_name, obj in list(self.data.items()):
                    raw_data = self._parse_raw_json(obj)

                    if "keys" not in raw_data:
                        print(f"Warning: Object '{key_name}' does not contain a 'keys' attribute.")
                        continue
                    
                    new_keys = []
                    for k, v in obj.get("keys", {}).items():
                        try:
                            # Handle numeric keys by appending underscores if they aren't strings
                            key_str = str(v) if isinstance(v, int) else (f"_{v}".ljust(10))  # Simple hack to keep it string-like or force type check

                            # Attempt to verify the data structure for each item within that specific object context
                            raw_obj_dict = self._parse_raw_json(obj)[k]

                            if not isinstance(raw_obj_dict, dict):
                                new_keys.append(str(v))  # Keep keys as strings in this version

                        except (TypeError, AttributeError) as e:
                            print(f"Warning parsing '{key_name}': {str(e)}")
                            continue

                    self.data[key_name] = raw_data
                    
                return True
                
            except json.JSONDecodeError

class AlienDatabase:
