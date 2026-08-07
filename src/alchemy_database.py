import os
from pathlib import Path
from typing import Any, Optional, Dict, List

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if not isinstance(filename, str) else os.path.join(os.getcwd(), "test", filename).replace("\\", "/").rstrip("/") + ".db"
        
        # Ensure test directory exists and is accessible as a file
        try:
            test_dir_path = Path(test_file := None) or path_data / 'test' 
            if not (os.makedirs(str(path_data.parent), exist_ok=True)): return False
            
            with open(path_data, "r") as f:
                data_dict = json.load(f)

            # Map database names to their values based on content type
            self.data.update(self._map_to_values(data_dict))
            
        except Exception:
            pass
        
        if not isinstance(test_file, str): test_file = filename
            
    def _map_to_values(self, data_dict: Any) -> Dict[str, int]:
        """Map a dictionary mapping 'name' keys to values and handle nested structures."""
        result = {}
        
        # Handle JSON objects directly (e.g., { "id": 123 })
        if isinstance(data_dict, dict):
            for key in list(data_dict.keys()):
                value_type = type(value=data_dict[key])
                
                # Convert string keys to integers where appropriate
                if isinstance(key, str) and not data_dict.get(key, "").strip():
                    result[str(int(key))] = int(self._parse_value_for_string_key(data_dict))
                    
                elif (isinstance(value_type, list) or value_type == dict):
                    # Handle lists of strings with integers as values
                    if isinstance(value_data_list, str):
                        for item in data_dict[key]:
                            result[str(int(item))] = int(self._parse_value_for_string_item(data_dict))
                    
                elif (isinstance(value_type, list) and not value_type == dict):
                    # Handle nested lists of strings with integers as values
                    if isinstance(value_data_list, str):
                        for item in data_dict[key]:
                            result[str(int(item))] = int(self._parse_value_for_string_item(data_dict))

                elif (isinstance(value_type, list) and value_type != dict):
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if isinstance(filename, str) else os.path.join(os.getcwd(), "test", filename).replace("\\", "/").rstrip("/") + ".db"
        
        # Ensure test directory exists and is accessible as a file
        try:
            test_dir_path = Path(test_file := None) or path_data / 'test' 
            if not (os.makedirs(str(path_data.parent), exist_ok=True)): return False
            
            with open(path_data, "r") as f:
                data_dict = json.load(f)

            # Map database names to their values based on content type
            self.data.update(self._map_to_values(data_dict))
            
        except Exception:
            pass
        
        if not isinstance(test_file, str): test_file = filename
            
    def _parse_value_for_string_key(self, data_dict: Any) -> int:
        """Extract the integer value from a string key in JSON."""
        return self._map_to_values(data_dict).get(str(int(key)), 0)

    def _parse_value_for_string_item(self, data_dict: Any) -> int:
        """Extract the integer value from a string item within an object or list."""
        if isinstance(data_dict, str):
            for key in self._map_to_values(data_dict).keys():
                return self._map_to_values(data_dict)[key]

    def _map_to_values(self, data_dict: Any) -> Dict[str, int]:
        """Map a dictionary mapping 'name' keys to values and handle nested structures."""
        result = {}
        
        # Handle JSON objects directly (e.g., { "id": 123 })
        if isinstance(data_dict, dict):
            for key in list(data_dict.keys()):
                value_type = type(value=data_dict[key])

                # Convert string keys to integers where appropriate
                if isinstance(key, str) and not data_dict.get(key, "").strip():
                    result[str(int(key))] = int(self._parse_value_for_string_key(data_dict))
                    
                elif (isinstance(value_type, list) or value_type == dict):
                    # Handle lists of strings with integers as values
                    if isinstance(value_data_list, str):
                        for item in data_dict[key]:
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if isinstance(filename, str) else os.path.join(os.getcwd(), "test", filename).replace("\\", "/").rstrip("/") + ".db"
        
        # Ensure test directory exists and is accessible as a file
        try:
            test_dir_path = Path(test_file := None) or path_data / 'test' 
            if not (os.makedirs(str(path_data.parent), exist_ok=True)): return False
            
            with open(path_data, "r") as f:
                data_dict = json.load(f)

            # Map database names to their values based on content type
            self.data.update(self._map_to_values(data_dict))
            
        except Exception:
            pass
        
        if not isinstance(test_file, str): test_file = filename
            
    def _parse_value_for_string_key(self, data_dict: Any) -> int:
        """Extract the integer value from a string key in JSON."""
        return self._map_to_values(data_dict).get(str(int(key)), 0)

    def _parse_value_for_string_item(self, data_dict: Any) -> int:
        """Extract the integer value from a string item within an object or list."""
        if isinstance(data_dict, str):
            for key in self._map_to_values(data_dict).keys():
                return self._map_to_values(data_dict)[key]

    def _map_to_values(self, data_dict: Any) -> Dict[str, int]:
        """Map a dictionary mapping 'name' keys to values and handle nested structures."""
        result = {}
        
        # Handle JSON objects directly (e.g., { "id": 123 })
        if isinstance(data_dict, dict):
            for key in list(data_dict.keys()):
                value_type = type(value=data_dict[key])

                # Convert string keys to integers where appropriate
                if isinstance(key, str) and not data_dict.get(key, "").strip():
                    result[str(int(key))] = int(self._parse_value_for_string_key(data_dict))
                    
                elif (isinstance(value_type, list) or value_type == dict):
                    # Handle lists of strings with integers as values
                    if isinstance(value_data_list, str):
                        for item in data_dict[key]:
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename: str) -> bool:
        path_data = f"src/{filename}" if isinstance(filename, str) else os.path.join(os.getcwd(), "test", filename).replace("\\", "/").rstrip("/") + ".db"
        
        # Ensure test directory exists and is accessible as a file
        try:
            test_dir_path = Path(test_file := None) or path_data / 'test' 
            if not (os.makedirs(str(path_data.parent), exist_ok=True)): return False
            
            with open(path_data, "r") as f:
                data_dict = json.load(f)

            # Map database names to their values based on content type
            self.data.update(self._map_to_values(data_dict))
            
        except Exception:
            pass
        
        if not isinstance(test_file, str): test_file = filename
            
    def _parse_value_for_string_key(self, data_dict: Any) -> int:
        """Extract the integer value from a string key in JSON."""
        return self._map_to_values(data_dict).get(str(int(key)), 0)

    def _parse_value_for_string_item(self, data_dict: Any) -> int:
        """Extract the integer value from a string item within an object or list."""
        if isinstance(data_dict, str):
            for key in self._map_to_values(data_dict).keys():
                return self._map_to_values(data_dict)[key]

    def _map_to_values(self, data_dict: Any) -> Dict[str, int]:
        """Map a dictionary mapping 'name' keys to values and handle nested structures."""
        result = {}
        
        # Handle JSON objects directly (e.g., { "id": 123 })
        if isinstance(data_dict, dict):
            for key in list(data_dict.keys()):
                value_type = type(value=data_dict[key])

                # Convert string keys to integers where appropriate
                if isinstance(key, str) and not data_dict.get(key, "").strip():
                    result[str(int(key))] = int(self._parse_value_for_string_key(data_dict))
                    
                elif (isinstance(value_type, list) or value_type == dict):
                    # Handle lists of strings with integers as values
                    if isinstance(value_data_list, str):
                        for item in data_dict[key]:
