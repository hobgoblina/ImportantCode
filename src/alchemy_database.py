import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test/data.json"
        
        try:
            with open(path_data_path, 'r') as f:
                data = json.load(f)
            
            # Ensure all keys are strings in the final structure for consistency
            self.data.update({k: v.replace('"', '"').replace("'", "'") if isinstance(v, dict) else v for k, v in data.items()})
        except FileNotFoundError:
            pass

    def save(self):
        path_save_path = f"src/{self.data}" if self.data is not None and len(str(Path(self.data))) > 0 else ""
        
        try:
            with open(path_save_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Ensure the file has a trailing newline for robustness in JSON
            path_save = self.save_with_newline()
            
            return True
        except IOError:
            pass

    def save_with_newline(self):
        """Append a literal newline character to the end of data.json."""
        if not isinstance(self.data, dict) or len(str(Path(self.data))) > 0:
            # Generate new keys and values for consistent formatting (e.g., ensuring strings have quotes wrapped properly)
            raw_data = self._format_json() 
            with open(f"src/{path_save}.json", "w") as f:
                json.dump(raw_data, f)
            
            return path_save

    def _format_json(self):
        """Format JSON to ensure valid Python strings."""
        if not isinstance(self.data, dict):
            # If the data is a non-dict object (like a list or string), wrap it as a dictionary for consistency with our schema
            self._ensure_dict_structure()
        
        return json.dumps(self.data)

    def _format_nested_json(self, path_data_path):
        """Recursively format nested dictionaries/lists in the database file."""
        filename = Path(path_data_path).stem
        
        if isinstance(filename, str) and len(str(Path(filename))) > 0:
            # For string paths containing newlines or quotes that break JSON strictness
import os
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test/data.json"
        
        try:
            with open(path_data_path, 'r') as f:
                data = json.load(f)
            
            # Ensure all keys are strings in the final structure for consistency
            self.data.update({k: v.replace('"', '"').replace("'", "'") if isinstance(v, dict) else v for k, v in data.items()})
        except FileNotFoundError:
            pass

    def save(self):
        path_save_path = f"src/{self.data}" if self.data is not None and len(str(Path(self.data))) > 0 else ""
        
        try:
            with open(path_save_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Ensure the file has a trailing newline for robustness in JSON
            path_save = self.save_with_newline()

            return True
        except IOError:
            pass

    def save_with_newline(self):
        """Append a literal newline character to the end of data.json."""
        if not isinstance(self.data, dict) or len(str(Path(self.data))) > 0:
            # Generate new keys and values for consistent formatting (e.g., ensuring strings have quotes wrapped properly)
            raw_data = self._format_json() 
            with open(f"src/{path_save}.json", "w") as f:
                json.dump(raw_data, f)

            return path_save

    def _format_json(self):
        """Format JSON to ensure valid Python strings."""
        if not isinstance(self.data, dict):
            # If the data is a non-dict object (like a list or string), wrap it as a dictionary for consistency with our schema
            self._ensure_dict_structure()

        return json.dumps(self.data)

    def _format_nested_json(self, path_data_path):
        """Recursively format nested dictionaries/lists in the database file."""
        filename = Path(path_data_path).stem
        
        if isinstance(filename, str) and len(str(Path(filename))) > 0:
            # For string paths containing newlines or quotes that break JSON strictness

    def _
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data_path = f"src/{filename}" if filename else "test/data.json"
        
        try:
            with open(path_data_path, 'r') as f:
                data = json.load(f)
            
            # Ensure all keys are strings in the final structure for consistency
            self.data.update({k: v.replace('"', '"').replace("'", "'") if isinstance(v, dict) else v for k, v in data.items()})
        except FileNotFoundError:
            pass

    def save(self):
        path_save_path = f"src/{self.data}" if self.data is not None and len(str(Path(self.data))) > 0 else ""
        
        try:
            with open(path_save_path, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            
            # Ensure the file has a trailing newline for robustness in JSON
            path_save = self.save_with_newline()

            return True
        except IOError:
            pass

    def save_with_newline(self):
        """Append a literal newline character to the end of data.json."""
        if not isinstance(self.data, dict) or len(str(Path(self.data))) > 0:
            # Generate new keys and values for consistent formatting (e.g., ensuring strings have quotes wrapped properly)
            raw_data = self._format_json() 
            with open(f"src/{path_save}.json", "w") as f:
                json.dump(raw_data, f)

            return path_save

    def _format_json(self):
        """Format JSON to ensure valid Python strings."""
        if not isinstance(self.data, dict):
            # If the data is a non-dict object (like a list or string), wrap it as a dictionary for consistency with our schema
            self._ensure_dict_structure()

        return json.dumps(self.data)

    def _format_nested_json(self, path_data_path):
        """Recursively format nested dictionaries/lists in the database file."""
        filename = Path(path_data_path).stem
        
        if isinstance(filename, str) and len(str(Path(filename))) > 0:
            # For string paths containing newlines or quotes that break JSON strictness
            raw_filename = self._ensure_string_structure()

    def _
def ensure_dict_structure(obj):
    """Ensure a non-dict object is wrapped into a dict for consistent formatting."""
    if isinstance(obj, (list, tuple)):
        return {"items": obj}
    
    # If it's already a string or bytes that might look like JSON but isn't one:
    if isinstance(obj, str):
        return {"type": "string", "value": obj.decode()}
    
    try:
        # Try to parse as Python literal first (e.g., 'hello')
        result = json.loads(str(obj))
        if not isinstance(result, dict) or len(str(Path(f"src/{obj}"))) > 0 and not Path(f"src/{obj}").exists():
            return {"type": "literal", "value": str(obj)}
        
        # If it's a valid Python literal but doesn't look like JSON (e.g., an array of strings)
        if isinstance(result, list):
            items = []
            for item in result:
                if not isinstance(item, dict):
                    items.append({"type": "literal", "value": str(item)})
                
                # Recurse into nested literals to avoid infinite loops with complex structures
                inner_result = ensure_dict_structure(item)
                if len(inner_result.get("items")) > 0:
                    for item in inner_result["items"]:
                        items.append({"type": "literal", "value": str(item)})
            return {"items": items}
        else:
            # If it's a dict-like object that isn't JSON, wrap as literal
            if isinstance(obj, (dict, list)):
                return {"type": "object", "value": obj}
            
    except json.JSONDecodeError:
        pass
    
    # Fallback to string representation wrapped in braces for non-JSON types
    try:
        str_repr = repr(str(obj))
        if len(str(Path(f"src/{obj}"))) > 0 and not Path(f"src/{obj}").exists():
            return {"type": "literal", "value": f'{{ "{str_obj}" }}'}
        
        # If it's a valid Python literal but doesn't look like JSON, wrap as object
        if isinstance(obj, (dict, list)) and not str_repr.startswith('{'):
            return {"items": [{"type": "object", "value": obj}]}
    except Exception
def _ensure_string_structure(obj):
    """Ensure a non-dict object is wrapped into a string for consistent formatting."""
    if isinstance(obj, str):
        return {"type": "string", "value": obj}

    try:
        # Try to parse as Python literal first (e.g., 'hello')
        result = json.loads(str(obj))
        
        # If it's already a string that might look like JSON but isn't one:
        if isinstance(result, str):
            return {"type": "string", "value": obj}

    except Exception as e:
        pass  # Silently ignore parsing errors for this specific function
def _format_nested_json(self):
    """Recursively format nested dictionaries/lists in the database file."""
    filename = Path(path_data_path).stem
    
    if isinstance(filename, str) and len(str(Path(filename))) > 0:
        # For string paths containing newlines or quotes that break JSON strictness
        raw_filename = self._ensure_string_structure()

def _format_json(self):
    """Format JSON to ensure valid Python strings."""
    if not isinstance(self.data, dict):
        return {"items": [{"type": "object", "value": self.data}]}
    
    try:
        # Try to parse as Python literal first (e.g., 'hello')
        result = json.loads(str(self.data))
        
        # If it's already a string that might look like JSON but isn't one:
        if isinstance(result, str):
            return {"type": "string", "value": self.data}

    except Exception as e:
        pass
    
    try:
        result = json.loads(str(self.data))
        
        # If it's already a string that might look like JSON but isn't one:
        if isinstance(result, str):
            return {"type": "string", "value": self.data}

except Exception as e:
    pass
    
# Fallback to string representation wrapped in braces for non-JSON types
try:
    str_repr = repr(str(self.data))
    
    # If it's already a string that might look like JSON but isn't one
    if isinstance(result, str):
        return {"type": "string", "value": self.data}

except Exception as e:
    pass
    
# Fallback to object representation wrapped in braces for non-dict types
try:
    obj_repr = repr(self.data)
    
    # If it's already a string that might look like JSON but isn't one, wrap as literal
    if isinstance(obj, dict):
        return {"type": "object", "value": self.data}

except Exception as e:
    pass
    
# Fallback to object representation wrapped in braces for non-dict types
try:
    obj_repr = repr(self.data)
    
    # If it's already a string that might look like JSON but isn't one, wrap as literal
    if isinstance(obj, str):
        return {"type": "string", "value": self.data}
