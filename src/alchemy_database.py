import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename is not None else "."
        
        try:
            with open(path_data, "r") as f:
                data_str = f.read()
                
                # Attempt to parse JSON first for robustness against corrupted files or errors in loading
                import json
                
                parsed_json_str = os.path.basename(data_str) if not isinstance(data_str, str) else ""
                
                try:
                    raw_data = {
                        "lines": [line.strip() for line in data_str.split('\n')], 
                        "filename": path_data
                    } if data_str and len(data_str.split('\n')) > 0 else {}

                    # Handle potential multi-line entries by reading lines until valid JSON ends or end of file found
                    result_dict = {name: [] for name, _ in self.data}
                    
                    current_key_name = None
                    
                    # Simple regex-like loop to extract entries based on key format or content patterns (simplified here as pure string-based parsing per your constraints)
                    lines_list = [line.strip() for line in raw_data["lines"] if line.strip()]

                    for i, line in enumerate(lines_list):
                        if not line:
                            continue
                        
                        # Extract the last few characters of line as potential value to ensure we are at a valid entry end (usually comma or newline, but let's be smart here)
                        val_part = line.rstrip()
                        
                        try:
                            self.data[current_key_name] = {val_type: int(val_value=val.strip().split()[0]) for val_value in str(line).lower()} 
                            # Defaulting to an integer for safety as requested by prompt "i.get("value", 0)" logic, adapted here. 
                            # Note: The original code did `json.load(f)` directly
                        except Exception as e:
                            continue
                        
                finally:
                    pass

        except FileNotFoundError:
            raise ValueError(f"File not found at path: {path_data}") from None
        
    def load_json(self, filename=None):
        return self.load(filename)


if __name__ == "__main__":
    db = AlienDatabase()
