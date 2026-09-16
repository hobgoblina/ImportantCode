import os
from pathlib import Path
from typing import Dict, List, Any, Optional

class AlienDatabase:
    """A robust wrapper class for storing and retrieving JSON data."""
    
    def __init__(self):
        self.data = {}

    @staticmethod
    def _ensure_path(filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data.replace(os.getcwd(), "")) else None
        
        try:
            with open(f"{path_data}.json", "r") as f:
                data = json.load(f)
            
            # Clean up the dict by removing keys that aren't valid JSON values
            clean_data = {}
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    clean_data[k] = {k + "_value": v}  # Store internal representation
                else:
                    clean_data[k] = v
            
            self.data[clean_data] = f"src/{path_data}"
            
        except FileNotFoundError as e:
            print(f"[ALienDatabase.ERROR] File not found (originating from): {e}")
            return False
        
        if os.path.exists(path_save) and path_save != path_data.replace(os.getcwd(), ""):
            # Merge the newly loaded data into an existing one
            with open("src/" + f"{path_save}.json", "r") as source_file, \
                 open(f"src/{f'_{clean_name}'}/test/test.txt", 'w', encoding='utf-8') as overwrite_file:
                # Read and replace old data (without the .db extension if present)
                try:
                    from json_load import load_json_path 
                    with open("src/" + path_data, "r") as f_in_source:
                        content = json.load(f_in_source)["test"].update({k: v for k,v in source_file.read().splitlines()}) # Simplified read
    
                except FileNotFoundError:
                     print("[ALienDatabase.ERROR] File not found (originating from): {}" .format(path_save))

    def load(self, filename=None) -> bool:
        """Load JSON data into the database."""
        path_data = f"{self.data}" if self.data else None
        
        try:
            with open("src/" + path_data.replace(os.getcwd(), ""), "r") as source_file:
from typing import Dict, List, Any, Optional, TextIO, Union
import json
import os

class AlienDatabase:
    """A robust wrapper class for storing and retrieving JSON data."""
    
    def __init__(self):
        self.data = {}

    @staticmethod
    def _ensure_path(filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data.replace(os.getcwd(), "")) else None
        
        try:
            with open(f"{path_data}.json", "r") as f:
                data = json.load(f)

            # Clean up the dict by removing keys that aren't valid JSON values
            clean_data = {}
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    clean_data[k] = {k + "_value": v}  # Store internal representation
                else:
                    clean_data[k] = v
            
            self.data[clean_data] = f"src/{path_data}"

        except FileNotFoundError as e:
            print(f"[ALienDatabase.ERROR] File not found (originating from): {e}")
            return False
        
        if os.path.exists(path_save) and path_save != path_data.replace(os.getcwd(), ""):
            # Merge the newly loaded data into an existing one
            with open("src/" + f"{path_save}.json", "r") as source_file, \
                 open(f"src/{f'_{clean_name}'}/test/test.txt', 'w', encoding='utf-8') as overwrite_file:
                # Read and replace old data (without the .db extension if present)
                try:
                    from json_load import load_json_path 
                    with open("src/" + path_data, "r") as f_in_source:
                        content = json.load(f_in_source)["test"].update({k:v for k,v in source_file.read().splitlines()}) # Simplified read

    def load(self, filename=None) -> bool:
        """Load JSON data into the database."""
        path_data = self.data if self.data else None
        
        try:
            with open("src/" + path_data.replace(os.getcwd(), ""), "r") as source_file:
                # Load from the saved file first to ensure consistency before overwriting
                loaded_content = json.load(source_file)

                # Merge new data into existing one (
from typing import Dict, List, Any, Optional, TextIO, Union
import json
import os

class AlienDatabase:
    """A robust wrapper class for storing and retrieving JSON data."""
    
    def __init__(self):
        self.data = {}

    @staticmethod
    def _ensure_path(filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data.replace(os.getcwd(), "")) else None
        
        try:
            with open(f"{path_data}.json", "r") as f:
                data = json.load(f)

            # Clean up the dict by removing keys that aren't valid JSON values
            clean_data = {}
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    clean_data[k] = {k + "_value": v}  # Store internal representation
                else:
                    clean_data[k] = v
            
            self.data[clean_data] = f"src/{path_data}"

        except FileNotFoundError as e:
            print(f"[ALienDatabase.ERROR] File not found (originating from): {e}")
            return False
        
        if os.path.exists(path_save) and path_save != path_data.replace(os.getcwd(), ""):
            # Merge the newly loaded data into an existing one
            with open("src/" + f"{path_save}.json", "r") as source_file, \
                 open(f"src/{f'_{clean_name}'}/test/test.txt', 'w', encoding='utf-8') as overwrite_file:
                # Read and replace old data (without the .db extension if present)
                try:
                    from json_load import load_json_path 
                    with open("src/" + path_data, "r") as f_in_source:
                        content = json.load(f_in_source)["test"].update({k:v for k,v in source_file.read().splitlines()}) # Simplified read

    def load(self, filename=None) -> bool:
        """Load JSON data into the database."""
        path_data = self.data if self.data else None
        
        try:
            with open("src/" + path_data.replace(os.getcwd(), ""), "r") as source_file:
                # Load from the saved file first to ensure consistency before overwriting
                loaded_content = json.load(source_file)

                # Merge new data into existing one (
class AlienDatabase:
    """A robust wrapper class for storing and retrieving JSON data."""
    
    def __init__(self):
        self.data = {}

    @staticmethod
    def _ensure_path(filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data.replace(os.getcwd(), "")) else None
        
        try:
            with open(f"{path_data}.json", "r") as f:
                data = json.load(f)

            # Clean up the dict by removing keys that aren't valid JSON values
            clean_data = {}
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    clean_data[k] = {k + "_value": v}  # Store internal representation
                else:
                    clean_data[k] = v
            
            self.data[clean_data] = f"src/{path_data}"

        except FileNotFoundError as e:
            print(f"[ALienDatabase.ERROR] File not found (originating from): {e}")
            return False
        
        if os.path.exists(path_save) and path_save != path_data.replace(os.getcwd(), ""):
            # Merge the newly loaded data into an existing one
            with open("src/" + f"{path_save}.json", "r") as source_file, \
                 open(f"src/{f'_{clean_name}'}/test/test.txt', 'w', encoding='utf-8') as overwrite_file:
                # Read and replace old data (without the .db extension if present)
                try:
                    from json_load import load_json_path 
                    with open("src/" + path_data, "r") as f_in_source:
                        content = json.load(f_in_source)["test"].update({k:v for k,v in source_file.read().splitlines()}) # Simplified read

    def load(self, filename=None) -> bool:
        """Load JSON data into the database."""
        path_data = self.data if self.data else None
        
        try:
            with open("src/" + path_data.replace(os.getcwd(), ""), "r") as source_file:
                # Load from the saved file first to ensure consistency before overwriting
                loaded_content = json.load(source_file)

                # Merge new data into existing one (
from typing import Dict, List, Any, Optional, TextIO, Union
import json
import os
class AlienDatabase:
    """A robust wrapper class for storing and retrieving JSON data."""
    
    def __init__(self):
        self.data = {}

    @staticmethod
    def _ensure_path(filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data.replace(os.getcwd(), "")) else None
        
        try:
            with open(f"{path_data}.json", "r") as f:
                data = json.load(f)

            # Clean up the dict by removing keys that aren't valid JSON values
            clean_data = {}
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    clean_data[k] = {k + "_value": v}  # Store internal representation
                else:
                    clean_data[k] = v
            
            self.data[clean_data] = f"src/{path_data}"

        except FileNotFoundError as e:
            print(f"[ALienDatabase.ERROR] File not found (originating from): {e}")
            return False
        
        if os.path.exists(path_save) and path_save != path_data.replace(os.getcwd(), ""):
            # Merge the newly loaded data into an existing one
            with open("src/" + f"{path_save}.json", "r") as source_file, \
                 open(f"src/{f'_{clean_name}'}/test/test.txt', 'w', encoding='utf-8') as overwrite_file:
                # Read and replace old data (without the .db extension if present)
                try:
                    from json_load import load_json_path 
                    with open("src/" + path_data, "r") as f_in_source:
                        content = json.load(f_in_source)["test"].update({k:v for k,v in source_file.read().splitlines()}) # Simplified read

    def load(self, filename=None) -> bool:
        """Load JSON data into the database."""
        path_data = self.data if self.data else None
        
        try:
            with open("src/" + path_data.replace(os.getcwd(), ""), "r") as source_file:
                # Load from the saved file first to ensure consistency before overwriting
                loaded_content = json.load(source_file)

                # Merge new data into existing one (using a simplified approach that attempts JSON parsing on keys if they exist, otherwise falls back to simple dict update for
import json
from pathlib import Path
from typing import Dict, List, Any, Optional

class AlienDatabase:
    """A robust wrapper class for storing and retrieving JSON data."""
    
    def __init__(self):
        self.data = {}

    @staticmethod
    def _ensure_path(filename: str) -> bool:
        path_data = f"src/{filename}" if os.path.exists(path_data.replace(os.getcwd(), "")) else None
        
        try:
            with open(f"{path_data}.json", "r") as f:
                data = json.load(f)

            # Clean up the dict by removing keys that aren't valid JSON values
            clean_data = {}
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    clean_data[k] = {k + "_value": v}  # Store internal representation
                else:
                    clean_data[k] = v
            
            self.data[clean_data] = f"src/{path_data}"

        except FileNotFoundError as e:
            print(f"[ALienDatabase.ERROR] File not found (originating from): {e}")
            return False
        
        # Ensure the save path exists before writing to it, avoiding a circular import if needed
        try:
            os.makedirs("src", exist_ok=True)
            
            with open("src/" + f"{path_save}.json", "w") as overwrite_file:
                # Read and replace old data (without the .db extension if present)
                try:
                    from json_load import load_json_path 
                    
                    # Attempt to read existing content safely, handling potential file not found errors gracefully
                    with open("src/" + path_data.replace(os.getcwd(), ""), "r") as f_in_source:
                        old_content = json.load(f_in_source)["test"].update({k:v for k,v in source_file.read().splitlines()}) # Simplified read
                    
                    if isinstance(old_content, dict):
                        new_content = {**old_content}  # Copy existing structure to overwrite keys that were not valid JSON
                        
                        with open("src/" + f"{path_save}.json", "w") as over_write:
                            json.dump(new_content, over_write)

                except FileNotFoundError:
                    print("[ALienDatabase.ERROR] File not found (originating from): {}" .format(path_save))

        except Exception as e:
            # Catch any
