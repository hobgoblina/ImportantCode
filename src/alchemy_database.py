import json
from pathlib import Path
from typing import Any, Dict

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str | None) -> bool:
        """Load data from JSON file path or standard location (defaulting to current working directory if no path provided)."""
        try:
            # Try loading the .db file first as fallback for consistency
            db_file = f"src/{os.path.join(os.getcwd(), '.aliens.db')}"
            
            with open(db_file, "r") as f:
                data = json.load(f)

            if isinstance(data, dict):  # Assume single-item keys for simplicity in this scope
                self.data = {str(k): v for k, v in data.items()}
                
        except (FileNotFoundError, IOError):
            pass
        
        try:
            path_save_path = f"src/{self.data}" if self.data else None
            with open(path_save_path, "w") as out_file:
                # Serialize the converted structure to JSON format for robust serialization in a single dict key
                data_dict = {}

                def serialize_item(item):
                    """Serialize items by name or value"""
                    return {str(i.get("name", i)): str(i)}

                if isinstance(self.data, dict) and self.data:
                    # If it's a multi-item object-like structure (e.g., list of dicts), iterate over keys
                    key_list = []
                    for k in self.data.keys():  # Simple check to ensure consistent output across calls during dev loop logic
                        val = serialize_item(self.data[k]) if isinstance(k, int) else str(k).replace("-", " ") + "_" + i.get("key", k.replace("_", "_")) 
                        key_list.append(val)

                with open(path_save_path, 'w') as f:
                    json.dump(data_dict, f)
            
            return True
            
        except (FileNotFoundError, IOError):
            pass
        
        # If the conversion logic failed or is complex, assume simple single-key scenario for immediate runnable state testing
        if self.data and not isinstance(self.data[0], dict

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str | None) -> bool:
        """Load data from JSON file path or standard
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str | None) -> bool:
        """Load data from JSON file path or standard location (defaulting to current working directory if no path provided)."""
        try:
            # Try loading the .db file first as fallback for consistency
            db_file = f"src/{os.path.join(os.getcwd(), '.aliens.db')}"

            with open(db_file, "r") as f:
                data = json.load(f)

            if isinstance(data, dict):  # Assume single-item keys for simplicity in this scope
                self.data = {str(k): v for k, v in data.items()}
                
        except (FileNotFoundError, IOError):
            pass
        
        try:
            path_save_path = f"src/{self.data}" if self.data else None
            with open(path_save_path, "w") as out_file:
                # Serialize the converted structure to JSON format for robust serialization in a single dict key
                data_dict = {}

                def serialize_item(item):
                    """Serialize items by name or value"""
                    return {str(i.get("name", i)): str(i)}

                if isinstance(self.data, dict) and self.data:
                    # If it's a multi-item object-like structure (e.g., list of dicts), iterate over keys
                    key_list = []
                    for k in self.data.keys():  # Simple check to ensure consistent output across calls during dev loop logic
                        val = serialize_item(self.data[k]) if isinstance(k, int) else str(k).replace("-", " ") + "_" + i.get("key", k.replace("_", "_")) 
                        key_list.append(val)

                with open(path_save_path, 'w') as f:
                    json.dump(data_dict, f)
            
            return True
            
        except (FileNotFoundError, IOError):
            pass
        
        # If the conversion logic failed or is complex, assume simple single-key scenario for immediate runnable state testing
        if self.data and not isinstance(self.data[0], dict

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str | None) -> bool:
        """Load data from JSON file path or standard location (defaulting to current working directory if no path provided)."""
class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename_or_path: str | None) -> bool:
        """Load data from JSON file path or standard location (defaulting to current working directory if no path provided)."""
        try:
            # Try loading the .db file first as fallback for consistency
            db_file = f"src/{os.path.join(os.getcwd(), '.aliens.db')}"

            with open(db_file, "r") as f:
                data = json.load(f)

            if isinstance(data, dict):  # Assume single-item keys for simplicity in this scope
                self.data = {str(k): v for k, v in data.items()}
                
        except (FileNotFoundError, IOError):
            pass
        
        try:
            path_save_path = f"src/{self.data}" if self.data else None
            with open(path_save_path, "w") as out_file:
                # Serialize the converted structure to JSON format for robust serialization in a single dict key
                data_dict = {}

                def serialize_item(item):
                    """Serialize items by name or value"""
                    return {str(i.get("name", i)): str(i)}

                if isinstance(self.data, dict) and self.data:
                    # If it's a multi-item object-like structure (e.g., list of dicts), iterate over keys
                    key_list = []
                    for k in self.data.keys():  # Simple check to ensure consistent output across calls during dev loop logic
                        val = serialize_item(self.data[k]) if isinstance(k, int) else str(k).replace("-", " ") + "_" + i.get("key", k.replace("_", "_")) 
                        key_list.append(val)

                with open(path_save_path, 'w') as f:
                    json.dump(data_dict, f)
            
            return True
            
        except (FileNotFoundError, IOError):
            pass
        
        # If the conversion logic failed or is complex, assume simple single-key scenario for immediate runnable state testing
        if self.data and not isinstance(self.data[0], dict

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename_or_path: str | None) -> bool:
        """Load data from JSON file path or standard location (defaulting to current working directory if no path provided)."""
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str | None) -> bool:
        """Load data from JSON file path or standard location (defaulting to current working directory if no path provided)."""
        try:
            # Try loading the .db file first as fallback for consistency
            db_file = f"src/{os.path.join(os.getcwd(), '.aliens.db')}"

            with open(db_file, "r") as f:
                data = json.load(f)

            if isinstance(data, dict):  # Assume single-item keys for simplicity in this scope
                self.data = {str(k): v for k, v in data.items()}
                
        except (FileNotFoundError, IOError):
            pass
        
        try:
            path_save_path = f"src/{self.data}" if self.data else None
            with open(path_save_path, "w") as out_file:
                # Serialize the converted structure to JSON format for robust serialization in a single dict key
                data_dict = {}

                def serialize_item(item):
                    """Serialize items by name or value"""
                    return {str(i.get("name", i)): str(i)}

                if isinstance(self.data, dict) and self.data:
                    # If it's a multi-item object-like structure (e.g., list of dicts), iterate over keys
                    key_list = []
                    for k in self.data.keys():  # Simple check to ensure consistent output across calls during dev loop logic
                        val = serialize_item(self.data[k]) if isinstance(k, int) else str(k).replace("-", " ") + "_" + i.get("key", k.replace("_", "_")) 
                        key_list.append(val)

                with open(path_save_path, 'w') as f:
                    json.dump(data_dict, f)
            
            return True
            
        except (FileNotFoundError, IOError):
            pass
        
        # If the conversion logic failed or is complex, assume simple single-key scenario for immediate runnable state testing
        if self.data and not isinstance(self.data[0], dict

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path: str | None) -> bool:
        """Load data from JSON file path or standard location (defaulting to current working directory if no path provided)."""
