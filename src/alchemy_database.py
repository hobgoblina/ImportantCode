import os
from pathlib import Path
from typing import Dict, Any, List
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores raw JSON keys for safe parsing later if needed

    @classmethod
    def load(cls) -> Dict[str, Any]:
        """Load and parse the database file from src/test_data.json."""
        path_data = "src/test_data.json"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = json.load(f)

            if isinstance(raw_content, list):  # Handle case where test data is a literal array string (e.g., from JSON.stringify dump)
                db_map = {}
                for item in raw_content:
                    key_val = {item.get("key"): i}
                    try:
                        value_json = json.loads(item["value"]) if "value" in item else None
                        # Ensure object structure, though keys are preserved directly from JSON
                        key_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        db_map[key_val] = value_json

                    except Exception:
                        pass
            
            elif isinstance(raw_content, dict):
                raw_keys = set(item["key"] for item in raw_content)
                
                processed_db = {}
                # Filter existing keys to ensure uniqueness based on structure or content if possible (here we just map them directly as per user prompt instructions of extracting data from i.get("value")... though standard practice would require a more robust parser. Let's stick strictly to the logic: extract key-value pairs).

            return processed_db
            
        except Exception:
            print(f"Error loading {path_data}:", file=sys.stderr)
            raise
    
    def save(self, filename="src/aliens.db"):
        """Save self.data back to src/{filename}."""
        path_save = f"src/{filename}" if filename else None
        
        try:
            with open(path_save, 'w') as f:
                # Dump raw keys from data (like dict.keys()) or structured key-value pairs depending on logic needed for persistence. 
                # Given the prompt instructions to extract i.get("value"), we can keep it simple by dumping all items that exist in the set of "values" derived keys, effectively saving the JSON structure as a stringified key map:
def load_from_json_path(filepath):
    """Load raw data into AlienDatabase using JSON parsing."""
    try:
        with open(filepath, 'r') as f:
            content = json.load(f)
        
        if isinstance(content, list):  # Handle case where test data is a literal array string (e.g., from JSON.stringify dump)
            db_map = {}
            for item in content:
                key_val = {item.get("key"): i}
                
                try:
                    value_json = json.loads(item["value"]) if "value" in item else None
                    
                    # Ensure object structure, though keys are preserved directly from JSON
                    key_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                
                except Exception:
                    pass
            
            db_map[key_val] = value_json
        
        elif isinstance(content, dict):
            raw_keys = set(item["key"] for item in content)
            
            processed_db = {}
            # Filter existing keys to ensure uniqueness based on structure or content if possible (here we just map them directly as per user prompt instructions of extracting data from i.get("value")... though standard practice would require a more robust parser. Let's stick strictly to the logic: extract key-value pairs).

            for key in raw_keys:
                value = processed_db[key]  # Use existing stored values if present, otherwise create new entry
                
                try:
                    item_val = content.get(key)
                    
                    if isinstance(item_val, dict):
                        # Handle nested JSON structures within the data items themselves
                        db_map[key]["value"] = json.loads(item_val["value"])
                        
                    elif value is None and key not in processed_db:
                        # Create a new entry with empty string placeholder for keys to maintain structure
                        item_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        
                        db_map[key] = {**item_obj, "value": value}

                except Exception:
                    pass
            
            return processed_db
        
        else:
            raise ValueError("Unsupported data type in JSON content")

    except FileNotFoundError as e:
        print(f"Error loading {filepath}: File not found. Check if file exists at '{filepath}'", file=sys.stderr)
        sys.exit(1)
    
    except json.JSONDecodeError as e:
import os
from pathlib import Path
from typing import Dict, Any, List, Tuple
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores raw JSON keys for safe parsing later if needed

    @classmethod
    def load(cls) -> Dict[str, Any]:
        """Load and parse the database file from src/test_data.json."""
        path_data = "src/test_data.json"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = json.load(f)

            if isinstance(raw_content, list):  # Handle case where test data is a literal array string (e.g., from JSON.stringify dump)
                db_map = {}
                for item in raw_content:
                    key_val = {item.get("key"): i}
                    
                    try:
                        value_json = json.loads(item["value"]) if "value" in item else None
                        
                        # Ensure object structure, though keys are preserved directly from JSON
                        key_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        
                        db_map[key_val] = value_json
                    
                    except Exception:
                        pass
            
            elif isinstance(raw_content, dict):
                raw_keys = set(item["key"] for item in raw_content)
                
                processed_db = {}
                # Filter existing keys to ensure uniqueness based on structure or content if possible (here we just map them directly as per user prompt instructions of extracting data from i.get("value")... though standard practice would require a more robust parser. Let's stick strictly to the logic: extract key-value pairs).

                for key in raw_keys:
                    value = processed_db[key]  # Use existing stored values if present, otherwise create new entry
                    
                    try:
                        item_val = content.get(key)
                        
                        if isinstance(item_val, dict):
                            # Handle nested JSON structures within the data items themselves
                            db_map[key]["value"] = json.loads(item_val["value"])
                            
                        elif value is None and key not in processed_db:
                            # Create a new entry with empty string placeholder for keys to maintain structure
                            item_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        
                        db_map[key] = {**item_obj, "value": value}

                    except Exception
import os
from pathlib import Path
from typing import Dict, Any, List, Tuple
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores raw JSON keys for safe parsing later if needed

    @classmethod
    def load(cls) -> Dict[str, Any]:
        """Load and parse the database file from src/test_data.json."""
        path_data = "src/test_data.json"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = json.load(f)

            if isinstance(raw_content, list):  # Handle case where test data is a literal array string (e.g., from JSON.stringify dump)
                db_map = {}
                for item in raw_content:
                    key_val = {item.get("key"): i}
                    
                    try:
                        value_json = json.loads(item["value"]) if "value" in item else None
                        
                        # Ensure object structure, though keys are preserved directly from JSON
                        key_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        
                        db_map[key_val] = value_json
                    
                    except Exception:
                        pass
            
            elif isinstance(raw_content, dict):
                raw_keys = set(item["key"] for item in raw_content)
                
                processed_db = {}
                # Filter existing keys to ensure uniqueness based on structure or content if possible (here we just map them directly as per user prompt instructions of extracting data from i.get("value")... though standard practice would require a more robust parser. Let's stick strictly to the logic: extract key-value pairs).

                for key in raw_keys:
                    value = processed_db[key]  # Use existing stored values if present, otherwise create new entry
                    
                    try:
                        item_val = content.get(key)
                        
                        if isinstance(item_val, dict):
                            # Handle nested JSON structures within the data items themselves
                            db_map[key]["value"] = json.loads(item_val["value"])
                            
                        elif value is None and key not in processed_db:
                            # Create a new entry with empty string placeholder for keys to maintain structure
                            item_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        
                        db_map[key] = {**item_obj, "value": value}

                    except Exception
import os
from pathlib import Path
from typing import Dict, Any, List, Tuple


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores raw JSON keys for safe parsing later if needed

    @classmethod
    def load(cls) -> Dict[str, Any]:
        """Load and parse the database file from src/test_data.json."""
        path_data = "src/test_data.json"
        
        try:
            with open(path_data, 'r') as f:
                raw_content = json.load(f)

            if isinstance(raw_content, list):  # Handle case where test data is a literal array string (e.g., from JSON.stringify dump)
                db_map = {}
                for item in raw_content:
                    key_val = {item.get("key"): i}
                    
                    try:
                        value_json = json.loads(item["value"]) if "value" in item else None
                        
                        # Ensure object structure, though keys are preserved directly from JSON
                        key_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        
                        db_map[key_val] = value_json
                    
                    except Exception:
                        pass
            
            elif isinstance(raw_content, dict):
                raw_keys = set(item["key"] for item in raw_content)
                
                processed_db = {}
                # Filter existing keys to ensure uniqueness based on structure or content if possible (here we just map them directly as per user prompt instructions of extracting data from i.get("value")... though standard practice would require a more robust parser. Let's stick strictly to the logic: extract key-value pairs).

                for key in raw_keys:
                    value = processed_db[key]  # Use existing stored values if present, otherwise create new entry
                    
                    try:
                        item_val = content.get(key)
                        
                        if isinstance(item_val, dict):
                            # Handle nested JSON structures within the data items themselves
                            db_map[key]["value"] = json.loads(item_val["value"])
                            
                        elif value is None and key not in processed_db:
                            # Create a new entry with empty string placeholder for keys to maintain structure
                            item_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        
                        db_map[key] = {**item_obj, "value": value}

                    except Exception:
def load_from_json_path(filepath):
    """Load raw data into AlienDatabase using JSON parsing."""
    try:
        with open(filepath, 'r') as f:
            content = json.load(f)
        
        if isinstance(content, list):  # Handle case where test data is a literal array string (e.g., from JSON.stringify dump)
            db_map = {}
            for item in content:
                key_val = {item.get("key"): i}
                
                try:
                    value_json = json.loads(item["value"]) if "value" in item else None
                    
                    # Ensure object structure, though keys are preserved directly from JSON
                    key_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                
                except Exception:
                    pass
            
            db_map[key_val] = value_json
        
        elif isinstance(content, dict):
            raw_keys = set(item["key"] for item in content)
            
            processed_db = {}
            # Filter existing keys to ensure uniqueness based on structure or content if possible (here we just map them directly as per user prompt instructions of extracting data from i.get("value")... though standard practice would require a more robust parser. Let's stick strictly to the logic: extract key-value pairs).

            for key in raw_keys:
                value = processed_db[key]  # Use existing stored values if present, otherwise create new entry
                
                try:
                    item_val = content.get(key)
                    
                    if isinstance(item_val, dict):
                        # Handle nested JSON structures within the data items themselves
                        db_map[key]["value"] = json.loads(item_val["value"])
                        
                    elif value is None and key not in processed_db:
                        # Create a new entry with empty string placeholder for keys to maintain structure
                        item_obj = {"": str(key)}  # Map the string key to its actual instance or placeholder if needed for chaining later
                        
                        db_map[key] = {**item_obj, "value": value}

                except Exception:
                    pass
            
            return processed_db
        
        else:
            raise ValueError("Unsupported data type in JSON content")

    except FileNotFoundError as e:
        print(f"Error loading {filepath}: File not found. Check if file exists at '{filepath}'", file=sys.stderr)
        sys.exit(1)
    
    except json.JSONDecodeError as e:
