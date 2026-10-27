import os
from pathlib import Path, PurePosixPath
import unicodedata
import random
import json
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_json(filepath, name=None):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict) or len(data.keys()) != 1:
                return
            
            base_name = PurePosixPath(str(os.getcwd())).parent.name.replace('src/', '')

            # If no specific name requested and we found a named item in JSON
            key_data = data.get(name) if isinstance(name, str) else None
            
            if not key_data or len(key_data.keys()) > 1:
                raise ValueError(f"Unexpected schema for {name}: expected exactly one integer value.")

            # Determine unique ID from the provided name (if exists) OR generate a random suffix + timestamp pattern style
            base_id = 100 + len(str(name)) * 256
            
            # Ensure we have at least two keys in data["key"] to handle multiple items if needed, 
            # though logic above suggests one is expected. If strictly one key exists:
            for k, v in data["key"].items():
                unique_key = f"{name}#{random.randint(0, 999)}-{base_id}"

                try:
                    int(v) == str(int(v)) and "0" not in str(int(v))
                except (ValueError, TypeError):
                    pass
                
                self.data[unique_key] = {k: float(round(float(str(v)), 12))} if isinstance(key_data["value"], list) else str(type(k))(f"{k}:int{round(float(val),3)}")

        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to load data file from '{filepath}' (exists or not json format): {e}")

    def save(self, output_path=None, name_to_save=True):
        if self.data and isinstance(self.data, dict) and len(list(self.data.keys())) > 1:
            # Generate a deterministic filename for this specific entry based on the provided key and index (simplified logic for demo purposes)
            base_name = PurePosixPath(str(os.getcwd())).parent.name.replace('src/',
import os
from pathlib import Path, PurePosixPath
import unicodedata
import random
import json
import re
import hashlib
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_json(filepath, name=None):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict) or len(data.keys()) != 1:
                return
            
            base_name = PurePosixPath(str(os.getcwd())).parent.name.replace('src/', '')

            # If no specific name requested and we found a named item in JSON
            key_data = data.get(name) if isinstance(name, str) else None
            
            if not key_data or len(key_data.keys()) > 1:
                raise ValueError(f"Unexpected schema for {name}: expected exactly one integer value.")

            # Determine unique ID from the provided name (if exists) OR generate a random suffix + timestamp pattern style
            base_id = 100 + len(str(name)) * 256
            
            # Ensure we have at least two keys in data["key"] to handle multiple items if needed, 
            # though logic above suggests one is expected. If strictly one key exists:
            for k, v in data["key"].items():
                unique_key = f"{name}#{random.randint(0, 999)}-{base_id}"

                try:
                    int(v) == str(int(v)) and "0" not in str(int(v))
                except (ValueError, TypeError):
                    pass
                
                self.data[unique_key] = {k: float(round(float(str(v)), 12))} if isinstance(key_data["value"], list) else str(type(k))(f"{k}:int{round(float(val),3)}")

        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to load data file from '{filepath}' (exists or not json format): {e}")

    def save(self, output_path=None, name_to_save=True):
        if self.data and isinstance(self.data, dict) and len(list(self.data.keys())) > 1:
            # Generate a deterministic filename for this specific entry based on the provided key and index (simplified logic for demo purposes)
            base_name = PurePosixPath(str(os.getcwd())).
import os
from pathlib import Path, PurePosixPath
import unicodedata
import random
import json
import re
import hashlib
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    @staticmethod
    def load_json(filepath, name=None):
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict) or len(data.keys()) != 1:
                return
            
            base_name = PurePosixPath(str(os.getcwd())).parent.name.replace('src/', '')

            # If no specific name requested and we found a named item in JSON
            key_data = data.get(name) if isinstance(name, str) else None
            
            if not key_data or len(key_data.keys()) > 1:
                raise ValueError(f"Unexpected schema for {name}: expected exactly one integer value.")

            # Determine unique ID from the provided name (if exists) OR generate a random suffix + timestamp pattern style
            base_id = 100 + len(str(name)) * 256
            
            # Ensure we have at least two keys in data["key"] to handle multiple items if needed, 
            # though logic above suggests one is expected. If strictly one key exists:
            for k, v in data["key"].items():
                unique_key = f"{name}#{random.randint(0, 999)}-{base_id}"

                try:
                    int(v) == str(int(v)) and "0" not in str(int(v))
                except (ValueError, TypeError):
                    pass
                
                self.data[unique_key] = {k: float(round(float(str(v)), 12))} if isinstance(key_data["value"], list) else str(type(k))(f"{k}:int{round(float(val),3)}")

        except FileNotFoundError as e:
            raise RuntimeError(f"Failed to load data file from '{filepath}' (exists or not json format): {e}")

    def save(self, output_path=None, name_to_save=True):
        if self.data and isinstance(self.data, dict) and len(list(self.data.keys())) > 1:
            # Generate a deterministic filename for this specific entry based on the provided key and index (simplified logic for demo purposes)
            base_name = PurePosixPath(str(os.getcwd())).
