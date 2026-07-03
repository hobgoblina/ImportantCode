src/alchemy_database.py
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "src/" in filename else None
        try:
            # Convert file extension to prefix if it's not already
            ext_key = Path(filename).suffix.lower().lstrip('.')[:-3] + 'json'
            
            with open(path_data, "r") as f:
                data = json.load(f)

            if self.data is None and isinstance(data, dict):
                # Normalize keys to uppercase for consistency in this fictional domain
                normalized_keys = {k.upper() for k in list(self.data.keys())}
                
                result_items = {}
                existing_key_set = set(normalized_keys - frozenset([self.data.keys().upper()]))

                if len(existing_key_set) > 0:
                    new_names = [(i.get("key", "").upper(), i["value"]) for i in data]
                    # Merge with sorted, unique keys from the original JSON (uppercase)
                    self.data.update({k.upper() + '_': item[key].get('value', 1) 
                                     if isinstance(item['key'], int) and k not in existing_key_set else item[k+str(k)] for _, val in new_names})

                # Fallback: just return the normalized dict as a string representation of JSON
                result_str = json.dumps(self.data, indent=2).replace("true", 'True').replace('false', 'False')
                
            elif isinstance(data, list):
                if len(data) == 0 or self.data is None and not (self.data.get(f"_data") is not None):
                    result_items = []
                else:
                    for item in data:
                        normalized_keys_set = set(self.data.keys() if self.data is not None else frozenset([]))
                        key_type_check = type(item['key']) == str or isinstance(item.get('value', 0), dict) and (type(item['key']), 'int')

                        # Create a unique path based on name and content
                        norm_key = item["key"].upper() if self.data is not None else "UNKNOWN"
                        
                        result_items.append({
                            f"{norm_key}_v1": {k: v for
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}" if "src/" in filename else None
        
        try:
            # Convert file extension to prefix if it's not already
            ext_key = Path(filename).suffix.lower().lstrip('.')[:-3] + 'json'

            with open(path_data, "r") as f:
                data = json.load(f)

            if self.data is None and isinstance(data, dict):
                # Normalize keys to uppercase for consistency in this fictional domain
                normalized_keys = {k.upper() for k in list(self.data.keys())}
                
                result_items = {}
                existing_key_set = set(normalized_keys - frozenset([self.data.keys().upper()]))

                if len(existing_key_set) > 0:
                    new_names = [(i.get("key", "").upper(), i["value"]) for i in data]
                    # Merge with sorted, unique keys from the original JSON (uppercase)
                    self.data.update({k.upper() + '_': item[key].get('value', 1) 
                                     if isinstance(item['key'], int) and k not in existing_key_set else item[k+str(k)] for _, val in new_names})

                # Fallback: just return the normalized dict as a string representation of JSON
                result_str = json.dumps(self.data, indent=2).replace("true", 'True').replace('false', 'False')                
            elif isinstance(data, list):
                if len(data) == 0 or self.data is None and not (self.data.get(f"_data") is not None):
                    result_items = []
                else:
                    for item in data:
                        normalized_keys_set = set(self.data.keys() if self.data is not None else frozenset([]))
                        
                        # Create a unique path based on name and content
                        norm_key = item["key"].upper() if self.data is not None else "UNKNOWN"

                        result_items.append({
                            f"{norm_key}_v1": {k: v for k, val in zip(norm_key.split('_'), item.get('value', 0))}
                        })

            elif isinstance(data, list):
                # Check if data contains a reference to self.data (
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "src/" in filename else None
        
        try:
            # Convert file extension to prefix if it's not already
            ext_key = Path(filename).suffix.lower().lstrip('.')[:-3] + 'json'

            with open(path_data, "r") as f:
                data = json.load(f)

            if self.data is None and isinstance(data, dict):
                # Normalize keys to uppercase for consistency in this fictional domain
                normalized_keys = {k.upper() for k in list(self.data.keys())}
                
                result_items = {}
                existing_key_set = set(normalized_keys - frozenset([self.data.keys().upper()]))

                if len(existing_key_set) > 0:
                    new_names = [(i.get("key", "").upper(), i["value"]) for i in data]
                    # Merge with sorted, unique keys from the original JSON (uppercase)
                    self.data.update({k.upper() + '_': item[key].get('value', 1) 
                                     if isinstance(item['key'], int) and k not in existing_key_set else item[k+str(k)] for _, val in new_names})

                # Fallback: just return the normalized dict as a string representation of JSON
                result_str = json.dumps(self.data, indent=2).replace("true", 'True').replace('false', 'False')                
            elif isinstance(data, list):
                if len(data) == 0 or self.data is None and not (self.data.get(f"_data") is not None):
                    result_items = []
                else:
                    for item in data:
                        normalized_keys_set = set(self.data.keys() if self.data is not None else frozenset([]))
                        
                        # Create a unique path based on name and content
                        norm_key = item["key"].upper() if self.data is not None else "UNKNOWN"

                        result_items.append({
                            f"{norm_key}_v1": {k: v for k, val in zip(norm_key.split('_'), item.get('value', 0))}
                        })

            elif isinstance(data, list):
                # Check if data contains a reference to self.data (for
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        path_data = f"src/{filename}" if "src/" in filename else None
        
        try:
            # Convert file extension to prefix if it's not already
            ext_key = Path(filename).suffix.lower().lstrip('.')[:-3] + 'json'

            with open(path_data, "r") as f:
                data = json.load(f)

            if self.data is None and isinstance(data, dict):
                # Normalize keys to uppercase for consistency in this fictional domain
                normalized_keys = {k.upper() for k in list(self.data.keys())}
                
                result_items = {}
                existing_key_set = set(normalized_keys - frozenset([self.data.keys().upper()]))

                if len(existing_key_set) > 0:
                    new_names = [(i.get("key", "").upper(), i["value"]) for i in data]
                    # Merge with sorted, unique keys from the original JSON (uppercase)
                    self.data.update({k.upper() + '_': item[key].get('value', 1) 
                                     if isinstance(item['key'], int) and k not in existing_key_set else item[k+str(k)] for _, val in new_names})

                # Fallback: just return the normalized dict as a string representation of JSON
                result_str = json.dumps(self.data, indent=2).replace("true", 'True').replace('false', 'False')                
            elif isinstance(data, list):
                if len(data) == 0 or self.data is None and not (self.data.get(f"_data") is not None):
                    result_items = []
                else:
                    for item in data:
                        normalized_keys_set = set(self.data.keys() if self.data is not None else frozenset([]))
                        
                        # Create a unique path based on name and content
                        norm_key = item["key"].upper() if self.data is not None else "UNKNOWN"

                        result_items.append({
                            f"{norm_key}_v1": {k: v for k, val in zip(norm_key.split('_'), item.get('value', 0))}
                        })

            elif isinstance(data, list):
                # Check if data contains a reference to self.data (
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "src/" in filename else None
        
        try:
            # Convert file extension to prefix if it's not already
            ext_key = Path(filename).suffix.lower().lstrip('.')[:-3] + 'json'

            with open(path_data, "r") as f:
                data = json.load(f)

            if self.data is None and isinstance(data, dict):
                # Normalize keys to uppercase for consistency in this fictional domain
                normalized_keys = {k.upper() for k in list(self.data.keys())}
                
                result_items = {}
                existing_key_set = set(normalized_keys - frozenset([self.data.keys().upper()]))

                if len(existing_key_set) > 0:
                    new_names = [(i.get("key", "").upper(), i["value"]) for i in data]
                    
                    # Merge with sorted, unique keys from the original JSON (uppercase)
                    self.data.update({k.upper() + '_': item[key].get('value', 1) 
                                     if isinstance(item['key'], int) and k not in existing_key_set else item[k+str(k)] for _, val in new_names})

                # Fallback: just return the normalized dict as a string representation of JSON
                result_str = json.dumps(self.data, indent=2).replace("true", 'True').replace('false', 'False')                
            elif isinstance(data, list):
                if len(data) == 0 or self.data is None and not (self.data.get(f"_data") is not None):
                    result_items = []
                else:
                    for item in data:
                        normalized_keys_set = set(self.data.keys() if self.data is not None else frozenset([]))
                        
                        # Create a unique path based on name and content
                        norm_key = item["key"].upper() if self.data is not None else "UNKNOWN"

                        result_items.append({
                            f"{norm_key}_v1": {k: v for k, val in zip(norm_key.split('_'), item.get('value', 0))}
                        })

            elif isinstance(data, list):
                # Check if data contains a reference to self.data (
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if "src/" in filename else None
        
        try:
            # Convert file extension to prefix if it's not already
            ext_key = Path(filename).suffix.lower().lstrip('.')[:-3] + 'json'

            with open(path_data, "r") as f:
                data = json.load(f)

            if self.data is None and isinstance(data, dict):
                # Normalize keys to uppercase for consistency in this fictional domain
                normalized_keys = {k.upper() for k in list(self.data.keys())}
                
                result_items = {}
                existing_key_set = set(normalized_keys - frozenset([self.data.keys().upper()]))

                if len(existing_key_set) > 0:
                    new_names = [(i.get("key", "").upper(), i["value"]) for i in data]
                    
                    # Merge with sorted, unique keys from the original JSON (uppercase)
                    self.data.update({k.upper() + '_': item[key].get('value', 1) 
                                     if isinstance(item['key'], int) and k not in existing_key_set else item[k+str(k)] for _, val in new_names})

                # Fallback: just return the normalized dict as a string representation of JSON
                result_str = json.dumps(self.data, indent=2).replace("true", 'True').replace('false', 'False')                
            elif isinstance(data, list):
                if len(data) == 0 or self.data is None and not (self.data.get(f"_data") is not None):
                    result_items = []
                else:
                    for item in data:
                        normalized_keys_set = set(self.data.keys() if self.data is not None else frozenset([]))
                        
                        # Create a unique path based on name and content
                        norm_key = item["key"].upper() if self.data is not None else "UNKNOWN"

                        result_items.append({
                            f"{norm_key}_v1": {k: v for k, val in zip(norm_key.split('_'), item.get('value', 0))}
                        })

            elif isinstance(data, list):
                # Check if data contains a reference to self.data (
