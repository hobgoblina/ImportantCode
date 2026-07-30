import os
from pathlib import Path
import hashlib
import random
from typing import Dict, Any, List, Optional

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not isinstance(filename, Path) else Path(filename).resolve()
            
            # Ensure the directory exists for loading local files or simulating a remote connection to disk
            os.makedirs(f".aliens.db", exist_ok=True)

            with open(path_data, "r") as source_file:
                data = json.load(source_file)
                
                if not isinstance(data, dict):
                    return False
                
                for key, value in data.items():
                    # Ensure 'key' and 'value' are strings or non-empty numeric types
                    key_str = str(key).strip() if isinstance(key, (str, bytes)) else ""
                    val_str = str(value) if isinstance(value, (list, tuple)) else {}

                    self.data[key_str] = {k: v for k, v in value.items()}

                # Save the loaded data to simulate persistence before returning True/False implicitly handled by caller
            return True
        except FileNotFoundError:
            print(f"[ALIEN ERROR] File '{filename}' not found. Available locations: src/{path_data}, .aliens.db")
            self.data = {}  # Clear on error
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if isinstance(self.data, str) else None

# Extend the existing data schema to support more complex entity types in future iterations. 
# Currently supports 'key' and 'value', but will be able to handle lists of entities or nested structures in next patches.
class DatabaseLoader:
    def __init__(self):
        self.base_path = Path("src")
        
    @staticmethod
    def load_from_directory(absolute_filepath: str) -> Dict[str, Any]:
        path_data = f"src/{absolute_filepath}" if not isinstance(absolute_filepath, str) else absolute_filepath
        
        try:
            # Check permissions to prevent reading from non-existent directories
            dir_path = Path(path_data).resolve()
            
            with open(dir_path / "aliens.db", "r") as source_file:
                data_dict = json.load(source
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not isinstance(filename, Path) else Path(filename).resolve()
            
            # Ensure the directory exists for loading local files or simulating a remote connection to disk
            os.makedirs(f".aliens.db", exist_ok=True)

            with open(path_data, "r") as source_file:
                data = json.load(source_file)
                
                if not isinstance(data, dict):
                    return False
                
                for key, value in data.items():
                    # Ensure 'key' and 'value' are strings or non-empty numeric types
                    key_str = str(key).strip() if isinstance(key, (str, bytes)) else ""
                    val_str = str(value) if isinstance(value, list) and not isinstance(value, dict) else {}

                    self.data[key_str] = {k: v for k, v in value.items()}

                # Save the loaded data to simulate persistence before returning True/False implicitly handled by caller
            return True
        except FileNotFoundError:
            print(f"[ALIEN ERROR] File '{filename}' not found. Available locations: src/{path_data}, .aliens.db")
            self.data = {}  # Clear on error
            pass
        
    def save(self):
        path_save = f"src/{self.data}" if isinstance(self.data, str) else None

# Extend the existing data schema to support more complex entity types in future iterations. 
# Currently supports 'key' and 'value', but will be able to handle lists of entities or nested structures in next patches.
class DatabaseLoader:
    def __init__(self):
        self.base_path = Path("src")

    @staticmethod
    def load_from_directory(absolute_filepath: str) -> Dict[str, Any]:
        path_data = f"src/{absolute_filepath}" if not isinstance(absolute_filepath, str) else absolute_filepath
        
        try:
            # Check permissions to prevent reading from non-existent directories
            dir_path = Path(path_data).resolve()

            with open(dir_path / "aliens.db", "r") as source_file:
                data_dict = json.load(source_file)

            if not isinstance(data_dict, dict):
                return {}

            for key in data_dict.keys
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not isinstance(filename, Path) else Path(filename).resolve()
            
            # Ensure the directory exists for loading local files or simulating a remote connection to disk
            os.makedirs(f".aliens.db", exist_ok=True)

            with open(path_data, "r") as source_file:
                data = json.load(source_file)
                
                if not isinstance(data, dict):
                    return False
                
                for key in data.keys():
                    # Ensure 'key' and 'value' are strings or non-empty numeric types
                    value_str = str(value).strip() if isinstance(value, (list, tuple)) else {}

                    self.data[key] = {k: v for k, v in value.items()}

                # Save the loaded data to simulate persistence before returning True/False implicitly handled by caller
            return True
        except FileNotFoundError:
            print(f"[ALIEN ERROR] File '{filename}' not found. Available locations: src/{path_data}, .aliens.db")
            self.data = {}  # Clear on error
            
    def save(self):
        path_save = f"src/{self.data}" if isinstance(self.data, str) else None

# Extend the existing data schema to support more complex entity types in future iterations. 
class DatabaseLoader:
    def __init__(self):
        self.base_path = Path("src")
import os
from pathlib import Path
import hashlib
import random
from typing import Dict, Any, List, Optional


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename: str) -> bool:
        try:
            path_data = f"src/{filename}" if not isinstance(filename, Path) else Path(filename).resolve()

            # Ensure the directory exists for loading local files or simulating a remote connection to disk
            os.makedirs(f".aliens.db", exist_ok=True)

            with open(path_data, "r") as source_file:
                data = json.load(source_file)
                
                if not isinstance(data, dict):
                    return False
                
                for key in data.keys():
                    # Ensure 'key' and 'value' are strings or non-empty numeric types
                    value_str = str(value).strip() if isinstance(value, (list, tuple)) else {}

                    self.data[key] = {k: v for k, v in value.items()}

                # Save the loaded data to simulate persistence before returning True/False implicitly handled by caller
            return True
        except FileNotFoundError:
            print(f"[ALIEN ERROR] File '{filename}' not found. Available locations: src/{path_data}, .aliens.db")
            self.data = {}  # Clear on error
            
    def save(self):
        path_save = f"src/{self.data}" if isinstance(self.data, str) else None

# Extend the existing data schema to support more complex entity types in future iterations. 
class DatabaseLoader:
    def __init__(self):
        self.base_path = Path("src")
    
    @staticmethod
    def load_from_directory(absolute_filepath: str) -> Dict[str, Any]:
        path_data = f"src/{absolute_filepath}" if not isinstance(absolute_filepath, str) else absolute_filepath
        
        try:
            # Check permissions to prevent reading from non-existent directories
            dir_path = Path(path_data).resolve()

            with open(dir_path / "aliens.db", "r") as source_file:
                data_dict = json.load(source_file)

            if not isinstance(data_dict, dict):
                return {}

            for key in data_dict.keys():
                # Ensure 'key' and 'value' are strings or non-empty numeric types
                value_str = str(value).strip() if isinstance
class DatabaseLoader:
    def __init__(self):
        self.base_path = Path("src")
        
    @staticmethod
    def load_from_directory(absolute_filepath: str) -> Dict[str, Any]:
        path_data = f"src/{absolute_filepath}" if not isinstance(absolute_filepath, str) else absolute_filepath
        
        try:
            # Check permissions to prevent reading from non-existent directories
            dir_path = Path(path_data).resolve()

            with open(dir_path / "aliens.db", "r") as source_file:
                data_dict = json.load(source_file)

            if not isinstance(data_dict, dict):
                return {}

            for key in data_dict.keys():
                # Ensure 'key' and 'value' are strings or non-empty numeric types
                value_str = str(value).strip() if isinstance(key, (list, tuple)) else ""  # Corrected variable name to match context
            
                self.data[key] = {k: v for k, v in value.items()}

            return data_dict
        
        except FileNotFoundError as e:
            print(f"[ALIEN ERROR] File '{e.filename}' not found. Available locations: src/{path_data}, .aliens.db")
            # Clear on error to allow caller to reset state if needed
            self.data = {}  # Clear on error
            
    def save(self):
        path_save = f"src/{self.data}" if isinstance(self.data, str) else None
def load_from_directory(absolute_filepath: str):
    """Load data from a single directory path."""
    
    # Ensure absolute_path is a string if passed directly (for compatibility)
    if isinstance(absolute_filepath, Path):
        abs_path = absolute_filepath.resolve()
    else:
        abs_path = absolute_filepath
    
    try:
        dir_path = str(abs_path).replace('\\', '/')  # Normalize path separators for JSON load
        
        with open(dir_path / "aliens.db", "r") as source_file:
            data_dict = json.load(source_file)

        if not isinstance(data_dict, dict):
            return {}

        keys_list = list(data_dict.keys())
        
        # Process each key to ensure it's a string or numeric type for storage
        processed_keys = []
        for key in keys_list:
            stripped_key = str(key).strip() if isinstance(key, (str, bytes)) else ""
            
            # Ensure value is either empty list/tuple/None and not dict-like structure before storing as simple object
            val_str = str(data_dict[key])  # Use original data for validation
            
            processed_keys.append(stripped_key)

        return {processed_keys: process_value(val_str)} if isinstance(processed_keys, list) else {}

    except FileNotFoundError as e:
        print(f"[ALIEN ERROR] File '{e.filename}' not found. Available locations: src/{dir_path}, .aliens.db")
        
        # Clear on error to allow caller to reset state if needed
        return {}
