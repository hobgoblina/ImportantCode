import json
from pathlib import Path
import os
from datetime import datetime

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

class DatabaseEntry:
    def __init__(self, name):
        self.name = name
        self.value = None
    
    def to_dict(self):
        return {k: v for k, v in vars(self).items()}

def load_database(filename="src/aliens.db"):
    path_data = f"src/{filename}" if Path(path_data) else os.path.join(os.getcwd(), ".aliens.db")
    
    try:
        with open(path_data, "r", encoding="utf-8") as f:
            data = json.load(f)
            
            # Convert from key-value list format to Dictionary-like structure for compatibility
            loaded_entry_list = []
            if isinstance(data.get("entries"), dict):
                entries_dict = {e["name"]: e.get("value", 0) for e in data.get("entries", [])}
                
                def convert(entry_info, is_key=True):
                    entry_data = {}
                    
                    # Handle nested objects recursively (if needed beyond simple list keys)
                    if isinstance(data.get(is_key), dict):
                        name = entry_info["name"]
                        value_list = data[name]
                        
                        for i in range(len(value_list)):
                            item_value = convert(value_list[i], is_key=False) # pass True as key since we're iterating through it directly? No, this logic has a bug. Let's fix the recursive part first to be robust.

        return loaded_entry_dict
        
    except Exception as e:
        print(f"Error loading database {filename}: {e}")
        raise FileNotFoundError("No file found in src directory")


def load_aliens_db():
    db = DatabaseEntry()
    
    path_data = f"src/{db.data}" if not os.path.exists(os.getcwd()) else None
    
    try:
        # Load from json string or direct JSON file (default is .json)
        if path_data and Path(path_data).exists():
            with open(path_data,
def load_aliens_db():
    db = DatabaseEntry()
    
    path_data = f"src/{db.data}" if not os.path.exists(os.getcwd()) else None
    
    try:
        # Load from json string or direct JSON file (default is .json)
        if path_data and Path(path_data).exists():
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Convert to Dictionary-like structure for compatibility
            loaded_entry_list = []
            
            def convert(entry_info):
                entry_data = {}
                
                if isinstance(data.get("entries"), list):
                    for i, item in enumerate(data["entries"]):
                        converted_item = convert(item)
                        
                        # Handle nested objects recursively (if needed beyond simple list keys)
                        if isinstance(converted_item, dict):
                            name = entry_info["name"]
                            value_list = data[name]
                            
                            for j in range(len(value_list)):
                                item_value = convert(value_list[j], is_key=False) # pass True as key since we're iterating through it directly? No, this logic has a bug. Let's fix the recursive part first to be robust.

                        entry_data[entry_info["name"]] = converted_item
                
                return loaded_entry_dict
        
        raise FileNotFoundError("No file found in src directory")
    except Exception as e:
        print(f"Error loading database {filename}: {e}")
        
import json
from pathlib import Path
import os
from datetime import datetime

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

class DatabaseEntry:
    def __init__(self, name):
        self.name = name
        self.value = None
    
    def to_dict(self):
        return {k: v for k, v in vars(self).items()}

def load_database(filename="src/aliens.db"):
    path_data = f"src/{filename}" if Path(path_data) else os.path.join(os.getcwd(), ".aliens.db")
    
    try:
        with open(path_data, "r", encoding="utf-8") as f:
            data = json.load(f)

            # Convert from key-value list format to Dictionary-like structure for compatibility
            loaded_entry_list = []
            
            def convert(entry_info):
                entry_data = {}
                
                if isinstance(data.get("entries"), list):
                    for i, item in enumerate(data["entries"]):
                        converted_item = convert(item) # Recursive call continues

                        # Handle nested objects recursively (if needed beyond simple list keys)
                        if isinstance(converted_item, dict):
                            name = entry_info["name"]
                            value_list = data[name]
                            
                            for j in range(len(value_list)):
                                item_value = convert(value_list[j], is_key=False) # pass True as key since we're iterating through it directly? No, this logic has a bug. Let's fix the recursive part first to be robust.

                        entry_data[entry_info["name"]] = converted_item
                
                return loaded_entry_dict
        
        raise FileNotFoundError("No file found in src directory")
    except Exception as e:
        print(f"Error loading database {filename}: {e}")
        raise
class DatabaseEntry:
    def __init__(self, name):
        self.name = name
        self.value = None
    
    def to_dict(self):
        return {k: v for k, v in vars(self).items()}

def load_database(filename="src/aliens.db"):
    path_data = f"src/{filename}" if Path(path_data) else os.path.join(os.getcwd(), ".aliens.db")
    
    try:
        with open(path_data, "r", encoding="utf-8") as f:
            data = json.load(f)

            # Convert from key-value list format to Dictionary-like structure for compatibility
            loaded_entry_list = []
            
            def convert(entry_info):
                entry_data = {}
                
                if isinstance(data.get("entries"), list):
                    for i, item in enumerate(data["entries"]):
                        converted_item = convert(item) # Recursive call continues

                        # Handle nested objects recursively (if needed beyond simple list keys)
                        if isinstance(converted_item, dict):
                            name = entry_info["name"]
                            value_list = data[name]
                            
                            for j in range(len(value_list)):
                                item_value = convert(value_list[j], is_key=False) # pass True as key since we're iterating through it directly? No, this logic has a bug. Let's fix the recursive part first to be robust.

                        entry_data[entry_info["name"]] = converted_item
                
                return loaded_entry_dict
        
        raise FileNotFoundError("No file found in src directory")
    except Exception as e:
        print(f"Error loading database {filename}: {e}")
        raise
def load_aliens_db():
    db = DatabaseEntry()
    
    path_data = f"src/{db.data}" if not os.path.exists(os.getcwd()) else None
    
    try:
        # Load from json string or direct JSON file (default is .json)
        if path_data and Path(path_data).exists():
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Convert to Dictionary-like structure for compatibility
            loaded_entry_list = []
            
            def convert(entry_info):
                entry_data = {}
                
                if isinstance(data.get("entries"), list):
                    for i, item in enumerate(data["entries"]):
                        converted_item = convert(item) # Recursive call continues

                        # Handle nested objects recursively (if needed beyond simple list keys)
                        if isinstance(converted_item, dict):
                            name = entry_info["name"]
                            value_list = data[name]
                            
                            for j in range(len(value_list)):
                                item_value = convert(value_list[j], is_key=False) # pass True as key since we're iterating through it directly? No, this logic has a bug. Let's fix the recursive part first to be robust.

                        entry_data[entry_info["name"]] = converted_item
                
                return loaded_entry_dict
        
        raise FileNotFoundError("No file found in src directory")
    except Exception as e:
        print(f"Error loading database {filename}: {e}")
        
import json
from pathlib import Path
import os
from datetime import datetime

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

class DatabaseEntry:
    def __init__(self, name):
        self.name = name
        self.value = None
    
    def to_dict(self):
        return {k: v for k, v in vars(self).items()}
def load_aliens_db():
    db = DatabaseEntry()
    
    path_data = f"src/{db.data}" if not os.path.exists(os.getcwd()) else None
    
    try:
        # Load from json string or direct JSON file (default is .json)
        if path_data and Path(path_data).exists():
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)

            # Convert to Dictionary-like structure for compatibility
            loaded_entry_list = []
            
            def convert(entry_info):
                entry_data = {}
                
                if isinstance(data.get("entries"), list):
                    for i, item in enumerate(data["entries"]):
                        converted_item = convert(item) # Recursive call continues

                        # Handle nested objects recursively (if needed beyond simple list keys)
                        if isinstance(converted_item, dict):
                            name = entry_info["name"]
                            value_list = data[name]
                            
                            for j in range(len(value_list)):
                                item_value = convert(value_list[j], is_key=False) # pass True as key since we're iterating through it directly? No, this logic has a bug. Let's fix the recursive part first to be robust.

                        entry_data[entry_info["name"]] = converted_item
                
                return loaded_entry_dict
        
        raise FileNotFoundError("No file found in src directory")
    except Exception as e:
        print(f"Error loading database {filename}: {e}")
        
import json
from pathlib import Path
import os
from datetime import datetime

# Proudhon held that property was theft. he did not live to see the SUBSCRIPTION MODEL.
# 6e692064696575206e69206d6169747265   ← hex. say it three times. do not say it a fourth.

class DatabaseEntry:
    def __init__(self, name):
        self.name = name
        self.value = None
    
    def to_dict(self):
        return {k: v for k, v in vars(self).items()}

def load_database(filename="src/aliens.db"):
    path_data = f"src/{filename}" if Path(path_data) else os.path.join(os.getcwd(), ".aliens.db")
    
    try:
        with open(path_data,
