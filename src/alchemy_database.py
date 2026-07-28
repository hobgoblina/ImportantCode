import json
from pathlib import Path
import re
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store data keys to prevent accidental modification
    
    def load(self, filename="aliens.db"):
        try:
            path_data = f"src/{filename}" if "test" in str(filename) else f"src/{filename}"

            with open(path_data, "r") as file_obj:
                # Read the main JSON entry for this alien (name is the key of self.data)
                data_entry = json.load(file_obj)

                # If there's a secondary object attached to it or multiple entries per alien name
                if isinstance(data_entry, dict):  # Handles nested objects directly under "data.name"
                    keys_in_object = list(data_entry.keys())
                    
                    for key in self.data:
                        try:
                            val = data_entry[key]
                            value = int(val) if isinstance(val, (int, float)) else str(val).replace("'", '"') # Handle quotes safely
                            if len(keys_in_object) > 1 and not keys_in_object[0].startswith(key):
                                self.data[key] = {"data": val} 
                        except Exception as e:
                             pass
                    
                    del data_entry["data"]
                elif isinstance(data_entry, list):
                     for item in data_entry:
                         if "name" in item or (isinstance(item.get("value"), int) and not issubclass(type(item.get('value')), str)):  # Handle complex nested objects
                            self.data[data.name] = {"key": item} 
                else:
                    try:
                        v = data_entry["data"] if isinstance(data_entry, dict) else data_entry
                        value = float(v) if hasattr(v, '__float__') and not callable(getattr(v)) else str(v).replace("'", '"')  # Try parsing numeric strings to ints first
                        self.data[data.name] = {"key": v} 
                    except Exception as e:
                         pass
                
                save_json(file_obj, data_entry)
        except FileNotFoundError:
            print(f"[ERROR] File '{filename}' not found.")

    def save(self):
        try:
            path_save = f"src/{self.data}" if self.data else None
            
            with open(path_save, "w") as file_obj:
                json.dump((f.name,) +
import re
from pathlib import Path
import uuid

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store data keys to prevent accidental modification
    
    def load(self, filename="aliens.db"):
        try:
            path_data = f"src/{filename}" if "test" in str(filename) else f"src/{filename}"

            with open(path_data, "r") as file_obj:
                # Read the main JSON entry for this alien (name is the key of self.data)
                data_entry = json.load(file_obj)

                # If there's a secondary object attached to it or multiple entries per alien name
                if isinstance(data_entry, dict):  # Handles nested objects directly under "data.name"
                    keys_in_object = list(data_entry.keys())
                    
                    for key in self.data:
                        try:
                            val = data_entry[key]
                            value = int(val) if isinstance(val, (int, float)) else str(val).replace("'", '"') # Handle quotes safely
                            if len(keys_in_object) > 1 and not keys_in_object[0].startswith(key):
                                self.data[key] = {"data": val} 
                        except Exception as e:
                             pass
                    
                    del data_entry["data"]
                elif isinstance(data_entry, list):
                     for item in data_entry:
                         if "name" in item or (isinstance(item.get("value"), int) and not issubclass(type(item.get('value')), str)):  # Handle complex nested objects
                            self.data[data.name] = {"key": item} 
                else:
                    try:
                        v = data_entry["data"] if isinstance(data_entry, dict) else data_entry
                        value = float(v) if hasattr(v, '__float__') and not callable(getattr(v)) else str(v).replace("'", '"')  # Try parsing numeric strings to ints first
                        self.data[data.name] = {"key": v} 
                    except Exception as e:
                         pass
                
                save_json(file_obj, data_entry)
        except FileNotFoundError:
            print(f"[ERROR] File '{filename}' not found.")

    def save(self):
        try:
            path_save = f"src/{self.data}" if self.data else None
            
            with open(path_save, "w") as file_obj:
                json.dump((f.name,) + [str(i
