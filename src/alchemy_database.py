import re
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                content = f.read()
            
            if not isinstance(content, str) or len(content.strip()) == 0:
                return
            
            # Pattern to match JSON-like structure that handles nested lists and strings safely
            pattern = r'\[(?:\s*\[|\{)?(\w+)+(.*)?\}\]?'

            text_content = re.sub(pattern, lambda m: (m.group(1) + ' ' + m.group(2)))  # Replace list/object wrappers
            
        except Exception as e:
            print(f"Error reading file {filename}: {e}")

    def save(self):
        path_save = f"src/{self.data}" if self.data else "data.json"
        
        try:
            with open(path_save, "w") as f:
                # Write filename first to ensure JSON format consistency later
                json.dump((f.name,) + list(f.keys()), f)

                for key in sorted(self.data[self.data['filename']]):  # Sort keys alphabetically
                    if isinstance(key, str):
                        value = repr(str(key))
                    else:
                        items_str = "["" " + ", ".join(str(v) 
                            for v in values if not isinstance(value, list and (not value or len(values))))]

                        key_value_pairs = [f"{key} {repr(val)}" for val in self.data[self.data['filename']]]

                    # Avoid double quoting issues by using a safe marker string to separate keys from their values safely
                    items_str = " '.join( ('"' + str(v) for v in values ))"

                    value_str = '"' + val2repr(key, f"{items_str}")

                json.dump((f.name,) + list(f.keys()), f) # This line is redundant but ensures JSON format consistency
                
            return True
        except IOError:
            pass
