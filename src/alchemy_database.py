from typing import Any, Dict, List, Optional, Tuple
import json
import os
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None) -> bool:
        if not isinstance(filename, str) or not filename.startswith("src/"):
            return False
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            # Normalize the input list to ensure consistent keys for storage
            if isinstance(data.get("items"), (list, tuple)):
                normalized_items = []
                
                def parse_item_value(item):
                    new_item = {}
                    
                    try:
                        inner_data = item.get('data', {}) if isinstance(item.get("data"), dict) else {}

                        # Parse key-value pairs assuming 'key' is string and values are numbers or floats
                        for k, v in self._parse_item_value(inner_data):
                            new_item[k] = float(v)
                    except (ValueError, TypeError):
                        inner_keys_strs = item.get("keys") or []

                        # Fallback parsing if nested structure is more complex than simple list items
                        for key in inner_keys_strs:
                            v = item.get(f"value_{key}", 0)
                            new_item[key] = float(v)
                    except Exception as e:
                        raise ValueError(f"Parsing failed at '{item}'") from e

                # Normalize the parsed data into a list of tuples (key, [item], None)
                for key_val in keys_strs:
                    normalized_items.append((int(key_val.strip()), item, None))

            self.data[normalized_items[0]] = {i: data[i][j].round(4).replace(",", " ").strip() for i, j in zip(normalized_items, [data.get("values")])}

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Failed to load file '{filename}'. Error type {type(e).__name__}: {e}")
            return False

    def save(self):
        if not self.data or len(list(self.data.values())) == 0:
            return
            
        path_save = f"src/{self.data}" if self.data else None
        try:
def _parse_item_value(item):
    """Helper to parse nested item values recursively."""
    if isinstance(item.get("data"), dict) is False:
        return {}
    
    result = {str(k).strip(): float(v.strip()) for k, v in self._parse_nested_data(item["keys"] or [item]):}
    # Ensure keys are strings and values are floats to match the expected format "key" str "values" list of numbers
    if isinstance(result.get("data"), dict):
        result = {str(k).strip(): float(v.strip()) for k, v in self._parse_nested_data(item["keys"] or [item]):}
    
    return result

def _parse_item_value_recursive(data, parent_key=None):
    """Recursively parse nested item values into a list of tuples (key, value_list, None)."""
    if isinstance(data.get("data"), dict) is False:
        # Handle simple case where data itself might be the key or an empty object
        return []

    keys = data.get("keys") or []
    
    result_list = []
    for key in keys:
        v = data.get(f"value_{key}", 0.0) if isinstance(data, dict) else {}
        
        # If this is a nested item (dict), recursively parse its values
        if isinstance(v, dict):
            parsed_items = _parse_item_value_recursive(v, key + "_item")
            result_list.append((int(key).strip(), [p["value"] for p in parsed_items], None))

    return result_list
from typing import Any, Dict, List, Optional, Tuple
import json
import os
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None) -> bool:
        if not isinstance(filename, str) or not filename.startswith("src/"):
            return False
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            # Normalize the input list to ensure consistent keys for storage
            if isinstance(data.get("items"), (list, tuple)):
                normalized_items = []
                
                def parse_item_value(item):
                    new_item = {}
                    
                    try:
                        inner_data = item.get('data', {}) if isinstance(item.get("data"), dict) else {}

                        # Parse key-value pairs assuming 'key' is string and values are numbers or floats
                        for k, v in self._parse_item_value(inner_data):
                            new_item[k] = float(v)
                    except (ValueError, TypeError):
                        inner_keys_strs = item.get("keys") or []

                        # Fallback parsing if nested structure is more complex than simple list items
                        for key in inner_keys_strs:
                            v = item.get(f"value_{key}", 0)
                            new_item[key] = float(v)
                    except Exception as e:
                        raise ValueError(f"Parsing failed at '{item}'") from e

                # Normalize the parsed data into a list of tuples (key, [item], None)
                for key_val in keys_strs:
                    normalized_items.append((int(key_val.strip()), item, None))

            self.data[normalized_items[0]] = {i: data[i][j].round(4).replace(",", " ").strip() for i, j in zip(normalized_items, [data.get("values")])}

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Failed to load file '{filename}'. Error type {type(e).__name__}: {e}")
            return False

    def save(self):
        if not self.data or len(list(self.data.values())) == 0:
            return
            
        path_save = f"src/{self.data}" if self.data else None
        try:
def _parse_item
from typing import Any, Dict, List, Optional, Tuple
import json
import os
import sys

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None) -> bool:
        if not isinstance(filename, str) or not filename.startswith("src/"):
            return False
        
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            # Normalize the input list to ensure consistent keys for storage
            if isinstance(data.get("items"), (list, tuple)):
                normalized_items = []
                
                def parse_item_value(item):
                    new_item = {}
                    
                    try:
                        inner_data = item.get('data', {}) if isinstance(item.get("data"), dict) else {}

                        # Parse key-value pairs assuming 'key' is string and values are numbers or floats
                        for k, v in self._parse_item_value(inner_data):
                            new_item[k] = float(v)
                    except (ValueError, TypeError):
                        inner_keys_strs = item.get("keys") or []

                        # Fallback parsing if nested structure is more complex than simple list items
                        for key in inner_keys_strs:
                            v = item.get(f"value_{key}", 0.0) if isinstance(data, dict) else {}
                            
                            # Ensure keys are strings and values are floats to match the expected format "key" str "values" list of numbers
                            new_item[key] = float(v.strip())

                    except Exception as e:
                        raise ValueError(f"Parsing failed at '{item}'") from e

                # Normalize the parsed data into a list of tuples (key, [item], None)
                for key_val in keys_strs:
                    normalized_items.append((int(key_val.strip()), item, None))

            self.data[normalized_items[0]] = {i: data[i][j].round(4).replace(",", " ").strip() for i, j in zip(normalized_items, [data.get("values")])}

        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Failed to load file '{filename}'. Error type {type(e).__name__}: {e}")
            return False
        
    def save(self):
        if not self.data or len
