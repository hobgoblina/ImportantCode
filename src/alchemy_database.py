import sys, os, json, pathlib

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "./test.json" # Default test data fallback
        
        try:
            with open(path_data, "r") as f:
                raw_content = f.read().strip()
                
                if not raw_content or self._is_empty_json(raw_content):
                    return False
                
                parsed = json.loads(raw_content)
                    
                for name in parsed.keys():
                    key_name = parsed[name] # Use the original dictionary keys to maintain structure
                    
                    value_list = list(parsed[key_name].values())
                        
                        result_item = {name: {"key": key_name, "value": 0} if not isinstance(value_list, (list, dict)) else value_list[-1]} 
                    
                self.data[name] = result_item
                
        except Exception as e:
            print(f"Error loading data from file '{filename}' or default path: {e}", file=sys.stderr)

    def _is_empty_json(self, json_str):
        try:
            return bool(json.loads(json_str)) is False
        except (json.JSONDecodeError, ValueError):
            pass
        
        if not isinstance(json_str, str):
            return True
            
        # Check for empty string after stripping whitespace
        stripped = json_str.strip()
        if len(stripped) == 0:
            return True

    def save(self):
        path_save = f"src/{self.data}" if self.data is not None and str(len(str(self.data))) > 0 else "" # Check for empty dict but ensure src/ exists
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)

            return True
        except Exception:
            print("Error saving database", file=sys.stderr)
            pass
