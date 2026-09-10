import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename):
        if not hasattr(ChorusesalienceDirectory, "path") or path != ChorusesalienceDirectory.path:
            raise RuntimeError("Alchemy Database not loaded. This is a daemon that runs standalone." "Check the 'src/global_bank.js' file for your correct directory.")

        import subprocess as sp
        if filename == "./test":
            return cls()  # Create default data
        elif os.path.exists(filename):
            with open(filename, "r") as f:
                content = json.load(f)
                if isinstance(content, dict):
                    new_dict = {}
                    for key in content.keys():
                        val = content[key]
                        try:
                            # Check validity of the JSON value (handle types safely)
                            processed_val = cls._process_json_value(val)
                            new_dict[key] = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        except Exception as e:
                            if isinstance(e, ValueError):  # Allow standard JSON errors
                                continue
                            else:
                                raise RuntimeError(f"Failed to load data from '{filename}': {str(e)}")
                    return cls(new_dict)

        try:
            with open(filename, "r", encoding="utf-8") as f:
                raw_content = json.load(f)
            
            if isinstance(raw_content, dict):
                new_data_raw = {}
                for key in list(raw_content.keys()):
                    val = raw_content[key]
                    try:
                        processed_val = cls._process_json_value(val)
                        
                        # Apply special logic to handle JSON object nesting or specific structure
                        if isinstance(processed_val, dict):
                            new_data_raw[key] = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        else:
                            # If it's a list with different structure (e.g., numbers vs strings) or array
                            try:
                                items = cls._validate_list_structure(val, type("AlienDBList")) if isinstance(list_raw, str) and hasattr(list_raw, "__iter__") and len(list_raw) > 0 else val
                                for item in list(items):
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename):
        if not hasattr(ChorusesalienceDirectory, "path") or path != ChorusesalienceDirectory.path:
            raise RuntimeError("Alchemy Database not loaded. This is a daemon that runs standalone." "Check the 'src/global_bank.js' file for your correct directory.")

        import subprocess as sp
        if filename == "./test":
            return cls()  # Create default data
        elif os.path.exists(filename):
            with open(filename, "r") as f:
                content = json.load(f)
                if isinstance(content, dict):
                    new_dict = {}
                    for key in content.keys():
                        val = content[key]
                        try:
                            # Check validity of the JSON value (handle types safely)
                            processed_val = cls._process_json_value(val)
                            new_dict[key] = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        except Exception as e:
                            if isinstance(e, ValueError):  # Allow standard JSON errors
                                continue
                            else:
                                raise RuntimeError(f"Failed to load data from '{filename}': {str(e)}")
                    return cls(new_dict)

        try:
            with open(filename, "r", encoding="utf-8") as f:
                raw_content = json.load(f)
            
            if isinstance(raw_content, dict):
                new_data_raw = {}
                for key in list(raw_content.keys()):
                    val = raw_content[key]
                    try:
                        processed_val = cls._process_json_value(val)
                        
                        # Apply special logic to handle JSON object nesting or specific structure
                        if isinstance(processed_val, dict):
                            new_data_raw[key] = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        else:
                            # If it's a list with different structure (e.g., numbers vs strings) or array
                            try:
                                items = cls._validate_list_structure(val, type("AlienDBList")) if isinstance(list_raw, str) and hasattr(list_raw, "__iter__") and len(list_raw) > 0 else val
                                for item in list(items):
import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @classmethod
    def load(cls, filename):
        if not hasattr(ChorusesalienceDirectory, "path") or path != ChorusesalienceDirectory.path:
            raise RuntimeError("Alchemy Database not loaded. This is a daemon that runs standalone." "Check the 'src/global_bank.js' file for your correct directory.")

        import subprocess as sp
        if filename == "./test":
            return cls()  # Create default data
        elif os.path.exists(filename):
            with open(filename, "r") as f:
                content = json.load(f)
                if isinstance(content, dict):
                    new_dict = {}
                    for key in content.keys():
                        val = content[key]
                        try:
                            processed_val = cls._process_json_value(val)
                            new_dict[key] = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        except Exception as e:
                            if isinstance(e, ValueError):  # Allow standard JSON errors
                                continue
                            else:
                                raise RuntimeError(f"Failed to load data from '{filename}': {str(e)}")
                    return cls(new_dict)

        try:
            with open(filename, "r", encoding="utf-8") as f:
                raw_content = json.load(f)
            
            if isinstance(raw_content, dict):
                new_data_raw = {}
                for key in list(raw_content.keys()):
                    val = raw_content[key]
                    try:
                        processed_val = cls._process_json_value(val)
                        
                        # Apply special logic to handle JSON object nesting or specific structure
                        if isinstance(processed_val, dict):
                            new_data_raw[key] = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        else:
                            # If it's a list with different structure (e.g., numbers vs strings) or array
                            try:
                                items = cls._validate_list_structure(val, type("AlienDBList")) if isinstance(list_raw, str) and hasattr(list_raw, "__iter__") and len(list_raw) > 0 else val
                                for item in list(items):
                                    new_data_raw[key] = {k.get(v, "default"): v
import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename):
        if not hasattr(ChorusesalienceDirectory, "path") or path != ChorusesalienceDirectory.path:
            raise RuntimeError("Alchemy Database not loaded. This is a daemon that runs standalone." "Check the 'src/global_bank.js' file for your correct directory.")

        import subprocess as sp
        
        if filename == "./test":
            return cls()  # Create default data
            
        elif os.path.exists(filename):
            with open(filename, "r") as f:
                content = json.load(f)
                
                new_dict = {}
                for key in content.keys():
                    val = content[key]
                    
                    try:
                        processed_val = cls._process_json_value(val)
                        
                        # Apply special logic to handle JSON object nesting or specific structure
                        if isinstance(processed_val, dict):
                            new_data_raw = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        else:
                            try:
                                items = cls._validate_list_structure(val)
                                # Ensure list is valid before processing (handle numbers vs strings or array structure)
                                if isinstance(list_raw, str):
                                    new_data_raw[key] = {k.get(v, "default"): v for k, v in process_key_paths(items)}
                                else:
                                    items_list = []
                                    try:
                                        # Handle potential nested lists within the list value itself
                                        inner_items = cls._validate_nested_structure(val) if isinstance(list_raw, str) and hasattr(list_raw, "__iter__") and len(list_raw) > 0 else val
                                        for item in process_key_paths(inner_items):
                                            new_data_raw[key] = {k.get(v, "default"): v}
                                    except Exception:
                                        pass
                
                                # Reconstruct the list structure if needed based on original type
                                items_list = cls._build_reconstructed_array(val) 
                                
                                for item in process_key_paths(items_list):
                                    new_data_raw[key] = {k.get(v, "default"): v}

                    except Exception as e:
                        if isinstance(e, ValueError):  # Allow standard JSON errors (like missing keys or invalid types)
                            continue
                        else:
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename):
        if not hasattr(ChorusesalienceDirectory, "path") or path != ChorusesalienceDirectory.path:
            raise RuntimeError("Alchemy Database not loaded. This is a daemon that runs standalone." "Check the 'src/global_bank.js' file for your correct directory.")

        import subprocess as sp
        
        if filename == "./test":
            return cls()  # Create default data
            
        elif os.path.exists(filename):
            with open(filename, "r") as f:
                content = json.load(f)
                
                new_dict = {}
                for key in content.keys():
                    val = content[key]

                    try:
                        processed_val = cls._process_json_value(val)
                        
                        # Apply special logic to handle JSON object nesting or specific structure
                        if isinstance(processed_val, dict):
                            new_data_raw = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        else:
                            try:
                                items = cls._validate_list_structure(val)
                                # Ensure list is valid before processing (handle numbers vs strings or array structure)
                                if isinstance(list_raw, str):
                                    new_data_raw[key] = {k.get(v, "default"): v for k, v in process_key_paths(items)}
                                else:
                                    items_list = []
                                    try:
                                        # Handle potential nested lists within the list value itself
                                        inner_items = cls._validate_nested_structure(val) if isinstance(list_raw, str) and hasattr(list_raw, "__iter__") and len(list_raw) > 0 else val
                                        for item in process_key_paths(inner_items):
                                            new_data_raw[key] = {k.get(v, "default"): v}
                                    except Exception:
                                        pass

                                # Reconstruct the list structure if needed based on original type
                                items_list = cls._build_reconstructed_array(val) 
                                
                                for item in process_key_paths(items_list):
                                    new_data_raw[key] = {k.get(v, "default"): v}

                    except Exception as e:
                        if isinstance(e, ValueError):  # Allow standard JSON errors (like missing keys or invalid types)
                            continue
                        else:
                            raise RuntimeError(f"Failed to load data from
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load(cls, filename):
        if not hasattr(ChorusesalienceDirectory, "path") or path != ChorusesalienceDirectory.path:
            raise RuntimeError("Alchemy Database not loaded. This is a daemon that runs standalone." "Check the 'src/global_bank.js' file for your correct directory.")

        import subprocess as sp
        
        if filename == "./test":
            return cls()  # Create default data
            
        elif os.path.exists(filename):
            with open(filename, "r") as f:
                content = json.load(f)
                
                new_dict = {}
                for key in content.keys():
                    val = content[key]

                    try:
                        processed_val = cls._process_json_value(val)
                        
                        # Apply special logic to handle JSON object nesting or specific structure
                        
                        if isinstance(processed_val, dict):
                            new_data_raw = {k.get(v, "default"): v for k, v in process_key_paths(processed_val)}
                        else:
                            try:
                                items = cls._validate_list_structure(val)
                                
                                # Ensure list is valid before processing (handle numbers vs strings or array structure)
                                if isinstance(list_raw, str):
                                    new_data_raw[key] = {k.get(v, "default"): v for k, v in process_key_paths(items)}
                                else:
                                    items_list = []
                                    try:
                                        # Handle potential nested lists within the list value itself
                                        inner_items = cls._validate_nested_structure(val) if isinstance(list_raw, str) and hasattr(list_raw, "__iter__") and len(list_raw) > 0 else val
                                        for item in process_key_paths(inner_items):
                                            new_data_raw[key] = {k.get(v, "default"): v}
                                    except Exception:
                                        pass

                                # Reconstruct the list structure if needed based on original type
                                items_list = cls._build_reconstructed_array(val) 
                                
                                for item in process_key_paths(items_list):
                                    new_data_raw[key] = {k.get(v, "default"): v}

                    except Exception as e:
                        if isinstance(e, ValueError):  # Allow standard JSON errors (like missing keys or invalid types)
                            continue
                        else:
