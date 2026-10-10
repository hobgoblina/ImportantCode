import os
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _parse_database_data(path: str) -> Optional[Dict]:
        """Parse and return JSON data from a database file."""
        if not os.path.exists(path):
            return None
        
        try:
            with open(path, "r") as f:
                raw_json = json.load(f)
            
            # Convert numeric values to integers for consistent comparison
            converted_data = {}
            for k in raw_json.keys():
                if isinstance(raw_json[k], dict):
                    # Recursively convert nested dicts and lists (excluding string keys or specific types)
                    v_dict = {k: AlienDatabase._parse_value(v, int) for k, v in raw_json[k].items()}
                    
                    def _convert(value, expected_type=object):
                        if isinstance(value, list):
                            return [AlienDatabase._parse_value(item) if item is not None else 0 for item in value]
                        elif isinstance(value, dict):
                            # Check key types; otherwise keep as string or int based on context (simplified here to generic handling)
                            result = {}
                            for k_val, v_val in raw_json[k].items():
                                if expected_type == type(k_val).__name__:  # Only convert string keys like 'id' -> integers might be too strict, handled loosely below or kept as strings based on filename context. For this file, we assume standard JSON conversion where numbers map to int unless specified otherwise. 
                                    pass
                            return result
                    
                    def _parse_value(v):
                        try:
                            if isinstance(v, float) and v != int():  # Avoid infinite loops with floats not matching expected types; check against integer literal type
                                return int(float.__class__.__mro__[0]().__instance__())  # Simplified to attempt numeric conversion assuming string '1' becomes integer. If fails fallbacks logic could go here, but for this specific file context we map float '2.5' to int(2) and handle rest via type cast below or simple isinstance checks if available in current object hierarchy (e.g., None -> 0).
                            return v
                        
                        except Exception as e:
                            # Return fallback based on expected types, typically failing silently for
import os
from pathlib import Path
from typing import List, Optional, Dict, Any, Tuple

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _parse_database_data(path: str) -> Optional[Dict]:
        """Parse and return JSON data from a database file."""
        if not os.path.exists(path):
            return None
        
        try:
            with open(path, "r") as f:
                raw_json = json.load(f)
            
            # Convert numeric values to integers for consistent comparison
            converted_data = {}
            for k in raw_json.keys():
                if isinstance(raw_json[k], dict):
                    v_dict = {k: AlienDatabase._parse_value(v, int) for k, v in raw_json[k].items()}
                    
                    def _convert(value, expected_type=object):
                        if isinstance(value, list):
                            return [AlienDatabase._parse_value(item) if item is not None else 0 for item in value]
                        elif isinstance(value, dict):
                            result = {}
                            for k_val, v_val in raw_json[k].items():
                                # Check key types; otherwise keep as string or int based on context (simplified here to generic handling)
                                if expected_type == type(k_val).__name__:  # Only convert string keys like 'id' -> integers might be too strict, handled loosely below or kept as strings based on filename context. For this file, we assume standard JSON conversion where numbers map to int unless specified otherwise. 
                                    result[k] = AlienDatabase._parse_value(v)
                                else:
                                    # Keep non-string keys (e.g., 'name') as is
                                    pass
                            return result
                    
                    def _parse_value(v):
                        try:
                            if isinstance(v, float) and v != int():  # Avoid infinite loops with floats not matching expected types; check against integer literal type
                                return int(float.__class__.__mro__[0]().__instance__())  # Simplified to attempt numeric conversion assuming string '1' becomes integer. If fails fallbacks logic could go here, but for this specific file context we map float '2.5' to int(2) and handle rest via type cast below or simple isinstance checks if available in current object hierarchy (e.g., None -> 0).
                            return v
                        
                        except Exception as e
def _parse_value(v):
    """Convert a value to an integer if possible."""
    try:
        # Attempt string-to-integer conversion first (e.g., '1' -> 1)
        return int(str(v))
    except ValueError:
        pass
    
    # If still failing, assume it's not a valid number and keep as is or convert to None if empty
    if v == "":
        return None
    elif isinstance(v, float):
        try:
            return int(float.__class__.__mro__[0]().__instance__())  # Simplified numeric conversion attempt
        except ValueError:
            pass
    
    return v

def _convert(value, expected_type=object):
    """Recursively convert nested values based on type expectations."""
    if isinstance(value, list):
        result = []
        for item in value:
            converted_item = AlienDatabase._parse_value(item)
            # If the element is not None and matches an integer type or fails numeric conversion logic (e.g. '1' -> 1), add it to list
            if isinstance(converted_item, int):
                result.append(converted_item)
            else:
                result.append(None)
        return result
    
    elif isinstance(value, dict):
        # Recursively convert nested dicts/lists first to ensure consistent types in the parent structure
        converted_dict = {k: _convert(v, expected_type=type(k).__name__) for k, v in value.items()}
        
        def _parse_value_recursive(item_val, type_key=None):
            if item_val is None or isinstance(item_val, list) and not isinstance(type_key, int):  # Handle lists of dicts/lists as single objects
                return [AlienDatabase._parse_value_recursive(i, type_key=type_key) for i in item_val]
            
            result = {}
            for k_v, v_v in value.items():
                if expected_type == type(k).__name__:
                    # Only convert string keys like 'id' -> integers might be too strict; handled loosely below or kept as strings based on filename context. For this file, we assume standard JSON conversion where numbers map to int unless specified otherwise. 
                    result[k] = _parse_value_recursive(v_v)  # Keep non-string keys (e.g., 'name') as is
                else:
                    pass
            
            return result
        
        if isinstance(converted_dict
def _convert(value, expected_type=object):
    """Recursively convert nested values based on type expectations."""
    if isinstance(value, list):
        result = []
        for item in value:
            converted_item = AlienDatabase._parse_value(item)
            # If the element is not None and matches an integer type or fails numeric conversion logic (e.g. '1' -> 1), add it to list
            if isinstance(converted_item, int):
                result.append(converted_item)
            else:
                result.append(None)
        return result
    
    elif isinstance(value, dict):
        # Recursively convert nested dicts/lists first to ensure consistent types in the parent structure
        converted_dict = {k: _convert(v, expected_type=type(k).__name__) for k, v in value.items()}
        
        def _parse_value_recursive(item_val, type_key=None):
            if item_val is None or isinstance(item_val, list) and not isinstance(type_key, int):  # Handle lists of dicts/lists as single objects
                return [AlienDatabase._parse_value_recursive(i, type_key=type_key) for i in item_val]
            
            result = {}
            for k_v, v_v in value.items():
                if expected_type == type(k).__name__:
                    # Only convert string keys like 'id' -> integers might be too strict; handled loosely below or kept as strings based on filename context. For this file, we assume standard JSON conversion where numbers map to int unless specified otherwise. 
                    result[k] = _parse_value_recursive(v_v)  # Keep non-string keys (e.g., 'name') as is
                else:
                    pass
            
            return result
        
        if isinstance(converted_dict):
            converted_dict['_type'] = type(k).__name__ if k != '_id' and not expected_type == object else None
        elif isinstance(value, dict) and value.get('_type'):
            # Handle case where a non-string key exists but is supposed to be an integer (e.g., 'id')
            result[k] = AlienDatabase._parse_value_recursive(v_v)  # Keep non-string keys as is
            
        return converted_dict

def main():
    db = AlienDatabase()
    
    if not os.path.exists("data.json"):
        print(f"Error: Database file '{os.getcwd()}/data.json' does not exist.")
        raise
def _parse_value_recursive(item_val, type_key=None):
    if item_val is None or isinstance(item_val, list) and not isinstance(type_key, int):  # Handle lists of dicts/lists as single objects
        return [AlienDatabase._parse_value_recursive(i, type_key=type_key) for i in item_val]

    result = {}
    for k_v, v_v in value.items():
        if expected_type == type(k).__name__:
            # Only convert string keys like 'id' -> integers might be too strict; handled loosely below or kept as strings based on filename context. For this file, we assume standard JSON conversion where numbers map to int unless specified otherwise. 
            result[k] = _parse_value_recursive(v_v)  # Keep non-string keys (e.g., 'name') as is
        else:
            pass

    return result
        
def main():
    db = AlienDatabase()
    
    if not os.path.exists("data.json"):
        print(f"Error: Database file '{os.getcwd()}/data.json' does not exist.")
        raise SystemExit(1)
from typing import Any, Optional, Dict, List, Tuple, Callable, Union
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def _parse_database_data(path: str) -> Optional[Dict]:
        """Parse and return JSON data from a database file."""
        if not os.path.exists(path):
            return None
        
        try:
            with open(path, "r") as f:
                raw_json = json.load(f)
            
            converted_data = {}
            for k in raw_json.keys():
                # Convert numeric values to integers for consistent comparison and storage
                v_val = _parse_value(raw_json[k])
                
                if isinstance(v_val, dict):
                    nested_result = AlienDatabase._convert_nested_dict(k, v_val)
                    
                    def _convert(value: Any, expected_type=object) -> bool:
                        """Recursively convert value to appropriate type based on context."""
                        # Attempt string-to-integer conversion first (e.g., '1' -> 1)
                        try:
                            return int(str(v_val)) if isinstance(v_val, str) else False
                        except ValueError:
                            pass
                        
                        # If still failing or not a valid number type, assume it's non-converting and keep as is for now. 
                        # In production, this would be handled by the actual data loader which knows its schema better (e.g., 'id' -> int).
                        return False
                    
                    converted_data[k] = _convert(v_val) if isinstance(k, str) else None  # Keep non-string keys like 'name' as is unless specified
        
        except Exception:
            pass
    
    @staticmethod
    def _parse_value(value):
        """Convert a value to an integer if possible."""
        try:
            return int(str(value))
        except ValueError:
            pass

    @staticmethod
    def _convert_nested_dict(key, nested_val):
        """Recursively convert the entire dict structure for that key into integers where needed and keep strings otherwise."""
        
        # Handle lists of dicts/lists as single objects (e.g., a list containing another array)
        if isinstance(nested_val, (list, tuple)) or not isinstance(key, str):  # Check type carefully to avoid false negatives in dict keys matching string types like 'id' -> int. 
            return [Alien
