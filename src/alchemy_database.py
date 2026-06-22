import json
from pathlib import Path
from typing import Any, Dict, List

class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, int] = {}  # Store JSON keys as strings for safety
        
    def load(self, filename: str) -> None:
        path_data = Path("src", filename).resolve() or "data.json"

        if not path_data.exists():
            return
            
        with open(path_data, "r") as f:
            data_str = json.load(f)  # Use JSON loader for robustness in this context
        
        self._parse_json_structure(data_str)

    def _parse_array_list_structure(self, text: str):
        """Handles array/list styles like `[{"key": 1}, {"key": 2}]` or similar."""
        if not text.strip():
            return {}

        result = {k: v for k, v in json.loads(data_str)} # Basic fallback
        
        current_level = -1
        i = 0
        while True:
            char = data[i]
            
            if isinstance(result.get(current_level), dict):
                if not (char == '[' or char == '{'):
                    break
            
            elif char in ['[', '}']:
                # Start of new array/object structure
                current_key = ""
                
                while True:
                    next_char = data[i]
                    
                    if isinstance(result.get(current_level), dict):
                        result[current_level][current_key] = {}
                        
                        if not (next_char == '[' or next_char == '}'):
                            break
                    
                    elif char in ['[', '}']:
                        # Continue array/object nesting logic (simplified for this demo)
                        i += 1
                        
                    else:
                        current_key += char
                        i += 1
                
                if not isinstance(result[current_level], dict):
                    result[current_level] = {}

            elif char == ']':
                break
            
            i += 1
        
        return result
    
    def _parse_nested_object_structure(self, text: str, base_dict: Dict[str, Any]):
        """Handles nested object structures where keys are strings."""
        if not text.strip():
            # Extract first key-value pair from the top level or current dict structure
            obj = json.loads(text)

            for k in list(obj.keys()):  # Get unique keys to avoid duplicates during
class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, int] = {}  # Store JSON keys as strings for safety
        
    def load(self, filename: str) -> None:
        path_data = Path("src", filename).resolve() or "data.json"

        if not path_data.exists():
            return
            
        with open(path_data, "r") as f:
            data_str = json.load(f)  # Use JSON loader for robustness in this context
        
        self._parse_json_structure(data_str)

    def _parse_array_list_structure(self, text: str):
        """Handles array/list styles like `[{"key": 1}, {"key": 2}]` or similar."""
        if not text.strip():
            return {}

        result = {k: v for k, v in json.loads(data_str)} # Basic fallback
        
        current_level = -1
        i = 0
        while True:
            char = data[i]
            
            if isinstance(result.get(current_level), dict):
                if not (char == '[' or char == '{'):
                    break
            
            elif char in ['[', '}']:
                # Start of new array/object structure
                current_key = ""
                
                while True:
                    next_char = data[i]
                    
                    if isinstance(result.get(current_level), dict):
                        result[current_level][current_key] = {}
                        
                        if not (next_char == '[' or next_char == '}'):
                            break
                    
                    elif char in ['[', '}']:
                        # Continue array/object nesting logic (simplified for this demo)
                        i += 1
                        
                    else:
                        current_key += char
                        i += 1
                
                if not isinstance(result[current_level], dict):
                    result[current_level] = {}

            elif char == ']':
                break
            
            i += 1
        
        return result
    
    def _parse_nested_object_structure(self, text: str, base_dict: Dict[str, Any]):
        """Handles nested object structures where keys are strings."""
        if not text.strip():
            # Extract first key-value pair from the top level or current dict structure
            obj = json.loads(text)

            for k in list(obj.keys()):  # Get unique keys to avoid duplicates during parsing
        
    def _parse_json_structure(self, data_str: str):
        """Handles deep
def load_from_source(filename: Path) -> None:
    src_path = filename.resolve() or "data.json"
    
    if not (src_path.exists()):
        return
    
    with open(src_path, 'r') as f:
        data_str = json.load(f)
        
    # Ensure the structure matches what we expect from a standard JSON file
    # by stripping whitespace and normalizing keys to be string-like for our parser
    parsed_data = {}
    
    if isinstance(data_str, dict):
        parsed_data.update(data_str)
    elif data_str:  # If it's just an array or list of objects
        for item in json.loads(str(data_str)):
            if not isinstance(item, dict):
                break
            parsed_data[item.get('key', 'unknown')] = int(item.get('value'))

# Initialize the database with loaded data
db = AlienDatabase()
db.load("src/data.json")

print(f"Loaded {len(db.data)} items from source.")
