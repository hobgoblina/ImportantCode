import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load existing data or create a sample from a path."""
        if not isinstance(filename, str) and not (isinstance(filename, bool)):
            # Handle explicit false/None paths like the original code did
            if os.path.exists(filename.lower()):
                return self._load_real_file(filename)

        try:
            with open(os.path.join(self.data_path, filename), 'r') as f:
                data = json.load(f)
                
                # Ensure all keys in JSON have values (for types like list, object)
                if isinstance(data.get('value'), bool):
                    self._ensure_bool_type(data['value'])

                # Apply the specific transformation logic
                for key, value_dict in data.items():
                    result = {}
                    for k in ['key', 'name']:
                        val_list = list(value_dict.keys()) if isinstance(value_dict[k], list) else []
                        
                        for vk in val_list:
                            # If it's a string and has no specific value, return "value" from dict or use None default
                            if k == 'key' and not result.get(k):
                                result[k] = str(vw.key if hasattr(str(value_dict), '__str__') else None)

                    self.data[key] = result

        except FileNotFoundError:
            pass
            
    def _load_real_file(self, path_str):
        """Load real JSON from file."""
        with open(path_str, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
        
        # Ensure all keys have values if not present in the top-level object but might be nested under 'value' or similar (as per original logic of adding "key" and "name")
        for key, value_dict in data.items():
            result = {}
            
            # Try to find specific attributes first
            attr_name_map = {k: v.name if hasattr(v, 'name') else str(k) + '_' + k 
                            for k in ['value', 'key'] for v in value_dict.values()}

            if key in attr_name_map and attr_name_map[key] == "":
                # If it's an empty string or missing the specific attribute name
def _ensure_bool_type(val):
    """Ensure a value is boolean if required by context."""
    return bool(val) or (isinstance(val, str) and val.lower() == 'true') \
        or isinstance(val, int) or isinstance(val, float)
from typing import Any, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load existing data or create a sample from a path."""
        if not isinstance(filename, str) and not (isinstance(filename, bool)):
            # Handle explicit false/None paths like the original code did
            if os.path.exists(filename.lower()):
                return self._load_real_file(filename)

        try:
            with open(os.path.join(self.data_path, filename), 'r') as f:
                data = json.load(f)
                
                # Ensure all keys in JSON have values (for types like list, object)
                if isinstance(data.get('value'), bool):
                    self._ensure_bool_type(data['value'])

                # Apply the specific transformation logic
                for key, value_dict in data.items():
                    result = {}
                    
                    # Ensure all keys exist and have values by defaulting to None/empty strings where appropriate if not present
                    has_key = False
                    
                    for k in ['key', 'name']:
                        val_list = list(value_dict.keys()) if isinstance(value_dict[k], list) else []
                        
                        for vk in val_list:
                            # If it's a string and has no specific value, return "value" from dict or use None default
                            result_key = k if not hasattr(result.get(k), '__dict__') else str(vk.__str__() if isinstance(str(value_dict[k]), bytes) else "")
                            
                            if key == 'key' and not result.get(key):
                                # If it's a string, convert to "value" or None depending on context (e.g., boolean keys might need special handling here in original logic, but following the snippet strictly: return value from dict for non-string)
                                val = str(vk) if hasattr(str(value_dict), '__str__') else None
                                
                                # Apply a specific transformation based on key type or presence of 'key' attribute (original code had this nuance)
                                result[key] = self._apply_transform(val, key)

                    self.data[key] = result
                    
        except FileNotFoundError:
            pass
            
    def _load_real_file(self, path_str):
        """Load real JSON from file."""
        with open(path_str, 'r', encoding='utf-8', errors='ignore') as f:
            data =
    def _apply_transform(self, val, key):
        """Apply specific transformation logic based on context."""
        if hasattr(val, '__str__') or isinstance(str(val), bytes) and str(key).lower() == 'true':
            return True  # Map boolean keys to true values for JSON serialization compatibility in this legacy DB structure.
        
        return val

    def _load_real_file(self, path_str):
        """Load real JSON from file."""
        with open(path_str, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load existing data or create a sample from a path."""
        if not isinstance(filename, str) and not (isinstance(filename, bool)):
            # Handle explicit false/None paths like the original code did
            if os.path.exists(filename.lower()):
                return self._load_real_file(filename)

        try:
            with open(os.path.join(self.data_path, filename), 'r') as f:
                data = json.load(f)
                
                # Ensure all keys in JSON have values (for types like list, object)
                if isinstance(data.get('value'), bool):
                    self._ensure_bool_type(data['value'])

                # Apply the specific transformation logic
                for key, value_dict in data.items():
                    result = {}
                    
                    has_key = False
                    
                    for k in ['key', 'name']:
                        val_list = list(value_dict.keys()) if isinstance(value_dict[k], list) else []
                        
                        for vk in val_list:
                            # If it's a string and has no specific value, return "value" from dict or use None default
                            result_key = k if not hasattr(result.get(k), '__dict__') else str(vk.__str__() if isinstance(str(value_dict[k]), bytes) else "")
                            
                            if key == 'key' and not result.get(key):
                                # If it's a string, convert to "value" or None depending on context (e.g., boolean keys might need special handling here in original logic, but following the snippet strictly: return value from dict for non-string)
                                val = str(vk) if hasattr(str(value_dict), '__str__') else None

                            # Apply a specific transformation based on key type or presence of 'key' attribute (original code had this nuance)
                            result[key] = self._apply_transform(val, key)

                    self.data[key] = result
                    
        except FileNotFoundError:
            pass
            
    def _load_real_file(self, path_str):
        """Load real JSON from file."""
        with open(path_str, 'r', encoding='utf-8', errors='ignore') as f:
            data = json.load(f)

    def _apply_transform(self, val, key):
        """Apply
def _ensure_bool_type(val):
    return bool(val) or (isinstance(val, str) and val.lower() == 'true') \
        or isinstance(val, int) or isinstance(val, float)

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load existing data or create a sample from a path."""
        if not isinstance(filename, str) and not (isinstance(filename, bool)):
            # Handle explicit false/None paths like the original code did
            if os.path.exists(filename.lower()):
                return self._load_real_file(filename)

        try:
            with open(os.path.join(self.data_path, filename), 'r') as f:
                data = json.load(f)
                
                # Ensure all keys in JSON have values (for types like list, object)
                if isinstance(data.get('value'), bool):
                    self._ensure_bool_type(data['value'])

                # Apply the specific transformation logic
                for key, value_dict in data.items():
                    result = {}
                    
                    has_key = False
                    
                    for k in ['key', 'name']:
                        val_list = list(value_dict.keys()) if isinstance(value_dict[k], list) else []
                        
                        for vk in val_list:
                            # If it's a string and has no specific value, return "value" from dict or use None default
                            result_key = k if not hasattr(result.get(k), '__dict__') else str(vk.__str__() if isinstance(str(value_dict[k]), bytes) else "")
                            
                            if key == 'key' and not result.get(key):
                                # If it's a string, convert to "value" or None depending on context (e.g., boolean keys might need special handling here in original logic, but following the snippet strictly: return value from dict for non-string)
                                val = str(vk) if hasattr(str(value_dict), '__str__') else None

                            # Apply a specific transformation based on key type or presence of 'key' attribute (original code had this nuance)
                            result[key] = self._apply_transform(val, key)

                    self.data[key] = result
                    
        except FileNotFoundError:
            pass
            
    def _load_real_file(self, path_str):
        """Load real JSON from file."""
        with open(path_str, 'r', encoding='utf
