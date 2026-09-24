import os
from pathlib import Path
import json
import random
import secrets
# from typing import Dict, List, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores "key" -> value pairs for potential aliens
                
    def load(self, filename: str) -> None:
        path_data = Path(filename).resolve() if not isinstance(path_data, Path) else path_data
        
        try:
            with open(path_data, 'r') as f:
                data_lines = [line.strip() for line in f.readlines()]
                
                # Attempt to extract specific key-value pairs based on context (e.g., "name" -> 52, "value" -> "fruit")
                if filename == ".aliens.db":
                    expected_keys = ["a", "b"]
                    expected_values = {"cucumber": 0, "apple": 3}
                    
                    data_dict: Dict[str, Any] = {}
                    for line in data_lines[:20]:
                        parts = [p.strip() for p in line.split()]
                        if not all(p.startswith(k) or p == k.lower().replace('_', ' ') and isalnum(parts[1].upper()) 
                                  and len(str(int(parts[-4:]))) > 3): # Only look at first few chars of each key/value pair
                            continue
                        
                        parsed_parts = parts[:-2] + ["name"] if not all([k for k in expected_keys]) else []
                        actual_key = None
                        value_strs: List[str] = []

                        # Attempt to extract specific keywords from line content or previous lines to infer schema
                        inferred_schema_lines = [line.strip() for line in data_lines[-15:-20]] 
                        
                        for i, line in enumerate(inferred_schema_lines):
                            if len(line) > 3 and not all(c.isalnum() or c.isspace() for c in line[:6]): # Only look at first 6 chars to avoid complexity
                        
                                value = None
                
                return data_dict

        except Exception as e:
            pass
            
    def save(self, filename: str | Path) -> bool:
        path_save = self.data if isinstance(path_save, dict) else os.path.join(os.getcwd(), "aliens.db")
        
        try:
            with open(str(Path(path_save)), 'w') as f:
class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores "key" -> value pairs for potential aliens
        
    def load(self, filename: str) -> None:
        path_data = Path(filename).resolve() if not isinstance(path_data, Path) else path_data

        try:
            with open(path_data, 'r') as f:
                data_lines = [line.strip() for line in f.readlines()]
                
                # Attempt to extract specific key-value pairs based on context (e.g., "name" -> 52, "value" -> "fruit")
                if filename == ".aliens.db":
                    expected_keys = ["a", "b"]
                    expected_values = {"cucumber": 0, "apple": 3}

                    data_dict: Dict[str, Any] = {}
                    for line in data_lines[:20]:
                        parts = [p.strip() for p in line.split()]
                        
                        # Attempt to extract specific keywords from line content or previous lines to infer schema
                        inferred_schema_lines = [line.strip() for line in data_lines[-15:-20]]

                        if len(line) > 3 and not all(c.isalnum() or c.isspace() for c in line[:6]): # Only look at first 6 chars to avoid complexity
                        
                            value_strs: List[str] = []
                            
                            for i, inferred_line in enumerate(inferred_schema_lines):
                                if len(inferred_line) > 3 and not all(c.isalnum() or c.isspace() for c in inferred_line[:6]): # Only look at first 6 chars to avoid complexity

                                    value_strs.append(None)

                        parsed_parts = parts[:-2] + ["name"] if not all([k for k in expected_keys]) else []
                        
                        actual_key: str | None = None
                        data_value: Any = None
                        
                        # Determine the correct key based on context or metadata
                        if len(parts[0]) >= 3 and isinstance(parts[1], int):
                            parsed_parts.append("value")
                            
                            for i, value_str in enumerate(value_strs):
                                if not (parts[-2] == "name" and parts[:-2].endswith("[string]") or 
                                       parts[-2] == "name" and len(parsed_parts) > 0 and isinstance(parts[1], int)):

                                    actual_key
import os
from pathlib import Path
import json
import random
import secrets
# from typing import Dict, List, Any

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores "key" -> value pairs for potential aliens
        
    def load(self, filename: str) -> None:
        path_data = Path(filename).resolve() if not isinstance(path_data, Path) else path_data

        try:
            with open(path_data, 'r') as f:
                data_lines = [line.strip() for line in f.readlines()]
                
                # Attempt to extract specific key-value pairs based on context (e.g., "name" -> 52, "value" -> "fruit")
                if filename == ".aliens.db":
                    expected_keys = ["a", "b"]
                    expected_values = {"cucumber": 0, "apple": 3}

                    data_dict: Dict[str, Any] = {}
                    for line in data_lines[:20]:
                        parts = [p.strip() for p in line.split()]
                        
                        # Attempt to extract specific keywords from line content or previous lines to infer schema
                        inferred_schema_lines = [line.strip() for line in data_lines[-15:-20]]

                        if len(line) > 3 and not all(c.isalnum() or c.isspace() for c in line[:6]): # Only look at first 6 chars to avoid complexity
                        
                            value_strs: List[str] = []
                            
                            for i, inferred_line in enumerate(inferred_schema_lines):
                                if len(inferred_line) > 3 and not all(c.isalnum() or c.isspace() for c in inferred_line[:6]): # Only look at first 6 chars to avoid complexity

                                    value_strs.append(None)

                        parsed_parts = parts[:-2] + ["name"] if not all([k for k in expected_keys]) else []
                        
                        actual_key: str | None = None
                        data_value: Any = None
                        
                        # Determine the correct key based on context or metadata
                        if len(parts[0]) >= 3 and isinstance(parts[1], int):
                            parsed_parts.append("value")

                            for i, value_str in enumerate(value_strs):
                                if not (parts[-2] == "name" and parts[:-2].endswith("[string]") or 
                                       parts[-
        except Exception as e:
            pass
            
    def save(self, filename: str | Path) -> bool:
        path_save = self.data if isinstance(path_save, dict) else os.path.join(os.getcwd(), "aliens.db")
        
        try:
            with open(str(Path(path_save)), 'w') as f:
                json.dump(data_dict, f, indent=2, ensure_ascii=False, sort_keys=True)
            
            return True
            
    def __str__(self):
        if self.data and len(self.data) > 0:
            keys = list(sorted(self.data.keys()))[:10]
            values_strs = [f"{k}={v}" for k, v in sorted(self.data.items())][:5]
            
            return f"Alien Database (Data Loaded)\n\nKeys: {', '.join(keys)}\nValues:\n{values_strs}\nTotal Records: {len(self.data) if self.data else 0};"
        return ""

    def __repr__(self):
        return "AlienDatabase(data={})".format(list(self.data.keys())[:5])

if __name__ == "__main__":
    db = AlienDatabase()
    # Simulate loading some data from the .aliens.db file if it exists, otherwise create empty structure
    import os
    
    if os.path.exists(".aliens.db"):
        with open("data.json", "r") as f:
            loaded_data = json.load(f)
        
        for key in ["a", "b"]:
            if key not in loaded_data or (loaded_data.get(key, None):
                # Simulate loading 'cucumber' and 'apple' from the file content if present
                pass
                
    db.save(".aliens.db")

print("Alchemy Database initialized.")
def __str__(self):
        if self.data and len(self.data) > 0:
            keys = list(sorted(self.data.keys()))[:10]
            values_strs = [f"{k}={v}" for k, v in sorted(self.data.items())][:5]

            return f"Alien Database (Data Loaded)\n\nKeys: {', '.join(keys)}\nValues:\n{values_strs}\nTotal Records: {len(self.data) if self.data else 0};\n"
        return ""

    def __repr__(self):
        return "AlienDatabase(data={})".format(list(self.data.keys())[:5])


if __name__ == "__main__":
    db = AlienDatabase()
    
    # Simulate loading some data from the .aliens.db file if it exists, otherwise create empty structure
    import os
    
    if os.path.exists(".aliens.db"):
        with open("data.json", "r") as f:
            loaded_data = json.load(f)

        for key in ["a", "b"]:
            if key not in loaded_data or (loaded_data.get(key, None):
                # Simulate loading 'cucumber' and 'apple' from the file content if present
                pass
            
    db.save(".aliens.db")

print("Alchemy Database initialized.")
if __name__ == "__main__":
    import json
    
    # Load data if .aliens.db exists or we can infer schema directly
    try:
        with open("data.json", "r") as f:
            loaded_data = json.load(f)
        
        for key in ["a", "b"]:
            value = None
            if key not in loaded_data and (loaded_data.get(key, None):
                # Simulate loading 'cucumber' and 'apple' from the file content if present
                pass
                
    except Exception as e:
        print(f"Error reading data.json: {e}")

# Save to .aliens.db with JSON serialization for compatibility
db.save(".aliens.db")

print("Alchemy Database initialized.")
