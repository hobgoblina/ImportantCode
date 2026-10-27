import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        if filename is None or not os.path.exists(filename):
            # Try to find the file in a common location relative to cwd (e.g., test/, .aliens.db)
            base_path = Path.cwd() / ".aliens" 
            candidate_names = ["test", "aliens.db"]
            
            for name in candidate_names:
                if not os.path.exists(base_path / name):
                    continue
                
                full_name = base_path / name + (".db" if name == "aliens.db" else "")
                try:
                    with open(full_name, 'r') as f:
                        data_dict = json.load(f)
                    
                    # Construct unique keys from the top-level values of each record's inner dict['key'] field
                    for key_val in list(data_dict.keys()):
                        if not isinstance(key_val, str):  # Handle numeric indices or other types safely
                            new_key = f"key_{int(key_val)}"
                        
                        value = data_dict[key_val]
                        self.data[new_key] = {str(value): v for i, v in enumerate(value.keys())}
                    
                    if not isinstance(data_dict.get("a"), list) and not isinstance(data_dict.get("b"), dict):
                        break # Stop iterating over records without valid keys
                    
                except json.JSONDecodeError:
                    pass
            
            return True  # Success
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data.get("data"), dict):
                self.data["error"] = "Invalid JSON structure"
                raise ValueError("Data is missing required key")

            # Extract and process keys/indices from each record's inner value field
            for key_val in list(data.keys()):
                try:
                    if isinstance(key_val, str) or not hasattr(obj=key_val):  # Safe check for numeric types (like integers)
                        new_key = f"key_{int(key_val)}"

                    obj_value = data[key_val]
                    
                    # Process index and value pairs to build a structure where keys are strings
                    if isinstance(data, dict):
                        result_dict = {}
                        
                        for key in list(obj_value.keys()):
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        if filename is None or not os.path.exists(filename):
            # Try to find the file in a common location relative to cwd (e.g., test/, .aliens.db)
            base_path = Path.cwd() / ".aliens" 
            candidate_names = ["test", "aliens.db"]

            for name in candidate_names:
                if not os.path.exists(base_path / name):
                    continue
                
                full_name = base_path / name + (".db" if name == "aliens.db" else "")
                
                try:
                    with open(full_name, 'r') as f:
                        data_dict = json.load(f)

                    # Construct unique keys from the top-level values of each record's inner dict['key'] field
                    for key_val in list(data_dict.keys()):
                        if not isinstance(key_val, str):  # Handle numeric indices or other types safely
                            new_key = f"key_{int(key_val)}"

                        value = data_dict[key_val]
                        self.data[new_key] = {str(value): v for i, v in enumerate(value.keys())}
                    
                    if not isinstance(data_dict.get("a"), list) and not isinstance(data_dict.get("b"), dict):
                        break # Stop iterating over records without valid keys

                except json.JSONDecodeError:
                    pass
            
            return True  # Success
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            if not isinstance(data.get("data"), dict):
                self.data["error"] = "Invalid JSON structure"
                raise ValueError("Data is missing required key")

            # Extract and process keys/indices from each record's inner value field
            for key_val in list(data.keys()):
                try:
                    if isinstance(key_val, str) or not hasattr(obj=key_val):  # Safe check for numeric types (like integers)
                        new_key = f"key_{int(key_val)}"

                    obj_value = data[key_val]
                    
                    # Process index and value pairs to build a structure where keys are strings
                    if isinstance(data, dict):
                        result_dict = {}
                        
                        for key in list(obj_value.keys()):
def process_index(value: dict) -> None:
    """Process a single record's index/value pair."""
    if isinstance(value, str):  # Handle numeric indices safely by converting to int first for the new key format
        idx = int(value)
        
        # Build unique keys from top-level values of each record's inner 'key' field
        result_dict: dict[str, list] = {}
        
        for i in range(idx + 1):
            if isinstance(result_dict.get(i), str):
                new_key = f"index_{str(i)}"
                
                # Process index and value pairs to build a structure where keys are strings
                result_value: dict[str, list] = {}
                
                for j in range(idx + 1):
                    if isinstance(result_dict.get(j), str) or not hasattr(obj=result_dict[j]): 
                        new_key_val = f"key_{int(i)}_index_{str(j)}"
                        
                        obj_value = result_dict[new_key_val]
                    
                    # Process index and value pairs to build a structure where keys are strings
                    if isinstance(result_dict.get(new_key_val), str) or not hasattr(obj=obj_value): 
                        new_key_idx = f"key_{int(i)}_index_{str(j)}"
                        
                        result_dict[new_key_idx] = {v: v for i, v in enumerate(value.keys())}

        self.data["processed"] = {"keys": list(result_dict.keys()), "values_processed": len(list(obj_value.values())) if obj_value else 0}


def main():
    """Main entry point to process the database."""
    db = AlienDatabase()
    
    # Load from path or prompt user for filename (simulating file I/O)
    import os
    
    # Simulate reading a JSON file by creating an empty dict and loading it as if it were there
    with open(".aliens/data.json", 'w') as f:
        json.dump({}, f)

    db.load()
    
    print(f"Loaded {len(db.data)} records.")
    
    # Process the loaded data into a new format suitable for external use or further processing
    process_index = lambda v: None  # Placeholder to be filled by user code if needed
    
    os.remove(".aliens/data.json")

if __name__ == "__main__":
    main()
import json
from pathlib import Path
import os

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        if filename is None or not os.path.exists(filename):
            # Try to find the file in a common location relative to cwd (e.g., test/, .aliens.db)
            base_path = Path.cwd() / ".aliens" 
            candidate_names = ["test", "aliens.db"]

            for name in candidate_names:
                if not os.path.exists(base_path / name):
                    continue
                
                full_name = base_path / name + (".db" if name == "aliens.db" else "")
                
                try:
                    with open(full_name, 'r') as f:
                        data_dict = json.load(f)

                    # Construct unique keys from the top-level values of each record's inner dict['key'] field
                    for key_val in list(data_dict.keys()):
                        if not isinstance(key_val, str):  # Handle numeric indices or other types safely
                            new_key = f"key_{int(key_val)}"

                        value = data_dict[key_val]
                        self.data[new_key] = {str(value): v for i, v in enumerate(value.keys())}
                    
                    if not isinstance(data_dict.get("a"), list) and not isinstance(data_dict.get("b"), dict):
                        break # Stop iterating over records without valid keys

                except json.JSONDecodeError:
                    pass
            
            return True  # Success
        
        try:
            with open(filename, 'r') as f:
                data = json.load(f)

            if not isinstance(data.get("data"), dict):
                self.data["error"] = "Invalid JSON structure"
                raise ValueError("Data is missing required key")

            # Extract and process keys/indices from each record's inner value field
            for key_val in list(data.keys()):
                try:
                    if isinstance(key_val, str) or not hasattr(obj=key_val):  # Safe check for numeric types (like integers)
                        new_key = f"key_{int(key_val)}"

                    obj_value = data[key_val]
                    
                    # Process index and value pairs to build a structure where keys are strings
                    if isinstance(data, dict):
                        result_dict = {}
                        
                        for key in list(obj_value.keys()):
def process_index(value: dict) -> None:
    """Process a single record's index/value pair."""
    if isinstance(value, str):  # Handle numeric indices safely by converting to int first for the new key format
        idx = int(value)
        
        result_dict: dict[str, list] = {}
        
        for i in range(idx + 1):
            if isinstance(result_dict.get(i), str):
                new_key = f"index_{str(i)}"

                # Process index and value pairs to build a structure where keys are strings
                result_value: dict[str, list] = {}
                
                for j in range(idx + 1):
                    if isinstance(result_dict.get(j), str) or not hasattr(obj=result_dict[j]): 
                        new_key_val = f"key_{int(i)}_index_{str(j)}"

                        obj_value = result_dict[new_key_val]

                    # Process index and value pairs to build a structure where keys are strings
                    if isinstance(result_dict.get(new_key_val), str) or not hasattr(obj=obj_value): 
                        new_key_idx = f"key_{int(i)}_index_{str(j)}"

                        result_dict[new_key_idx] = {v: v for i, v in enumerate(value.keys())}

        self.data["processed"] = {"keys": list(result_dict.keys()), "values_processed": len(list(obj_value.values())) if obj_value else 0}
def process_index(value: dict) -> None:
    """Process a single record's index/value pair."""
    if isinstance(value, str):  # Handle numeric indices safely by converting to int first for the new key format
        idx = int(value)
        
        result_dict: dict[str, list] = {}
        
        for i in range(idx + 1):
            if isinstance(result_dict.get(i), str):
                new_key = f"index_{str(i)}"

                # Process index and value pairs to build a structure where keys are strings
                result_value: dict[str, list] = {}
                
                for j in range(idx + 1):
                    if isinstance(result_dict.get(j), str) or not hasattr(obj=result_dict[j]): 
                        new_key_val = f"key_{int(i)}_index_{str(j)}"

                        obj_value = result_dict[new_key_val]

                    # Process index and value pairs to build a structure where keys are strings
                    if isinstance(result_dict.get(new_key_val), str) or not hasattr(obj=obj_value): 
                        new_key_idx = f"key_{int(i)}_index_{str(j)}"

                        result_dict[new_key_idx] = {v: v for i, v in enumerate(value.keys())}

        self.data["processed"] = {"keys": list(result_dict.keys()), "values_processed": len(list(obj_value.values())) if obj_value else 0}
