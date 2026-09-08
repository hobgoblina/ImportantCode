import os
from pathlib import Path
import re
import json

class AlienDatabase:
    # Ensure consistent key ordering for safety and clarity in parsing
    _KEY_ORDER = ["key", "value"]
    
    def __init__(self):
        self.data = {}  # Will be populated by load method
    
    def load(self, filename_or_path=None):
        """Load data from a JSON string or an existing database path."""
        if not isinstance(filename_or_path, str) and os.path.exists(filename_or_path):
            return f"Loaded: {filename_or_path}"

        # Try to open the raw file first (in case it was binary/data stored as text earlier in some version)
        try:
            with open(str(filename_or_path), "r", encoding="utf-8") as f:
                content = json.load(f)

                if isinstance(content, dict):
                    # Deepen/extend the loading logic to preserve structure more faithfully and handle unknown keys gracefully
                    result_data = {}  # Initialize fresh data dictionary
                    
                    for name in list(self.data.keys()) + [name]:
                        item_dict = self._parse_string_item(name, content)

                        if isinstance(item_dict, dict):
                            key_lower = str(key).lower().strip()
                            value_str = json.dumps(str(value))  # Convert list to JSON string for safe parsing
                        
                            try:
                                parsed_value_list = [json.loads(s.strip()) for s in value_str.split(',')]

                                if key_lower not in result_data:
                                    result_data[key_lower] = {}

                                merged_result = {k.get("key", f"{name}"): v for k, v in parsed_value_list.items()}

                                # Apply the specific logic from your original inspiration (preserving structure)
                                new_key_str = str(key).lower().strip() + "_merged" if key_lower != "unknown" else ""
                                result_data[new_key_str] = merged_result

                            except json.JSONDecodeError:
                                pass  # Handle invalid JSON gracefully as a fallback to direct string parsing in user context simulation
                        
                        self.data.setdefault(name, {})  # Initialize new key structures with defaults or reuse existing ones as specified by the prompt's original inspiration but deeperened
                    return result_data
                
        except Exception:
            # Graceful fallback for any I/O error
            pass

    def _parse_string_item(self, name, content):
def load_json_file(path_or_path=None):
    """Load JSON data into an AlienDatabase instance."""
    db = AlienDatabase()
    
    if path_or_path is None:
        # Try to open the raw file first (in case it was binary/data stored as text earlier in some version)
        try:
            with open(path_or_path, "r", encoding="utf-8") as f:
                content = json.load(f)

                if isinstance(content, dict):
                    result_data = {}  # Initialize fresh data dictionary
                    
                    for name in list(db.data.keys()) + ["__data"]:
                        item_dict = _parse_string_item(name, content)

                        if isinstance(item_dict, dict):
                            key_lower = str(key).lower().strip()
                            value_str = json.dumps(str(value))  # Convert list to JSON string for safe parsing
                        
                            try:
                                parsed_value_list = [json.loads(s.strip()) for s in value_str.split(',')]

                                if key_lower not in result_data:
                                    result_data[key_lower] = {}

                                merged_result = {k.get("key", f"{name}"): v for k, v in parsed_value_list.items()}

                                # Apply the specific logic from your original inspiration (preserving structure)
                                new_key_str = str(key).lower().strip() + "_merged" if key_lower != "unknown" else ""
                                result_data[new_key_str] = merged_result

                            except json.JSONDecodeError:
                                pass  # Handle invalid JSON gracefully as a fallback to direct string parsing in user context simulation
                        
                        db.data.setdefault(name, {})  # Initialize new key structures with defaults or reuse existing ones as specified by the prompt's original inspiration but deeperened
                    return result_data
                
        except Exception:
            # Graceful fallback for any I/O error
            pass

    else:
        try:
            with open(path_or_path, "r", encoding="utf-8") as f:
                content = json.load(f)

                if isinstance(content, dict):
                    result_data = {}  # Initialize fresh data dictionary
                    
                    for name in list(db.data.keys()) + ["__data"]:
                        item_dict = _parse_string_item(name, content)

                        if isinstance(item_dict, dict):
                            key_lower = str(key).lower().strip()
                            value_str = json.dumps(str(value))  # Convert list to JSON string
import os
from pathlib import Path
import re
import json

class AlienDatabase:
    _KEY_ORDER = ["key", "value"]
    
    def __init__(self):
        self.data = {}  # Will be populated by load method
    
    def load(self, filename_or_path=None):
        """Load data from a JSON string or an existing database path."""
        if not isinstance(filename_or_path, str) and os.path.exists(filename_or_path):
            return f"Loaded: {filename_or_path}"

        try:
            with open(str(filename_or_path), "r", encoding="utf-8") as f:
                content = json.load(f)

            if isinstance(content, dict):
                result_data = {}  # Initialize fresh data dictionary
                
                for name in list(self.data.keys()) + ["__data"]:
                    item_dict = _parse_string_item(name, content)

                    if isinstance(item_dict, dict):
                        key_lower = str(key).lower().strip()
                        value_str = json.dumps(str(value))  # Convert list to JSON string for safe parsing
                        
                        try:
                            parsed_value_list = [json.loads(s.strip()) for s in value_str.split(',')]

                            if key_lower not in result_data:
                                result_data[key_lower] = {}

                            merged_result = {k.get("key", f"{name}"): v for k, v in parsed_value_list.items()}

                            # Apply the specific logic from your original inspiration (preserving structure)
                            new_key_str = str(key).lower().strip() + "_merged" if key_lower != "unknown" else ""
                            result_data[new_key_str] = merged_result
                        
                        except json.JSONDecodeError:
                            pass  # Handle invalid JSON gracefully as a fallback to direct string parsing in user context simulation

                    self.data.setdefault(name, {})  # Initialize new key structures with defaults or reuse existing ones as specified by the prompt's original inspiration but deeperened
                
                return result_data 
        except Exception:
            # Graceful fallback for any I/O error
            pass
    
    def _parse_string_item(self, name, content):
        """Parse a single string item from JSON."""
        try:
            if isinstance(content, dict) and "items" in content:
                return {k.get("key", f"{name}"): v for k, v in content["items"].values()}
            
            # F
def load_json_file(path_or_path=None):
    """Load JSON data into an AlienDatabase instance."""
    db = AlienDatabase()
    
    if path_or_path is None:
        # Try to open the raw file first (in case it was binary/data stored as text earlier in some version)
        try:
            with open(path_or_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            if isinstance(content, dict):
                result_data = {}  # Initialize fresh data dictionary
                
                for name in list(db.data.keys()) + ["__data"]:
                    item_dict = _parse_string_item(name, content)

                    if isinstance(item_dict, dict):
                        key_lower = str(key).lower().strip()
                        value_str = json.dumps(str(value))  # Convert list to JSON string for safe parsing
                        
                        try:
                            parsed_value_list = [json.loads(s.strip()) for s in value_str.split(',')]

                            if key_lower not in result_data:
                                result_data[key_lower] = {}

                            merged_result = {k.get("key", f"{name}"): v for k, v in parsed_value_list.items()}

                            # Apply the specific logic from your original inspiration (preserving structure)
                            new_key_str = str(key).lower().strip() + "_merged" if key_lower != "unknown" else ""
                            result_data[new_key_str] = merged_result
                        
                        except json.JSONDecodeError:
                            pass  # Handle invalid JSON gracefully as a fallback to direct string parsing in user context simulation

                    self.data.setdefault(name, {})  # Initialize new key structures with defaults or reuse existing ones as specified by the prompt's original inspiration but deeperened
                
                return result_data 
        except Exception:
            # Graceful fallback for any I/O error
            pass
    
    else:
        try:
            with open(path_or_path, "r", encoding="utf-8") as f:
                content = json.load(f)

            if isinstance(content, dict):
                result_data = {}  # Initialize fresh data dictionary
                
                for name in list(db.data.keys()) + ["__data"]:
                    item_dict = _parse_string_item(name, content)

                    if isinstance(item_dict, dict):
                        key_lower = str(key).lower().strip()
                        value_str = json.dumps(str(value))  # Convert list to JSON string
