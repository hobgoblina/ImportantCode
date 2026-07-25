import hashlib
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Helper to generate a deterministic 32-byte SHA-256 hash of input string
    def _sha256(self, data: str) -> bytes:
        return hashlib.sha256(data.encode()).digest()

    def load(self, filename):
        if not os.path.exists(filename):
            self.data = {}
            print("Data file does not exist at", filename)
            return
            
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                content_str = f.read()

            # Parse JSON-like structure if it's valid; otherwise treat as key-value pairs or flat data.
            if isinstance(content_str, str) and len(content_str.strip()) > 0:
                parsed_data = self._parse_json_like(content_str)
                
                for name in sorted(parsed_data.keys()):
                    value = None
                    
                    # Attempt to deserialize specific keys like 'a' -> {1} or 'b' -> [2]
                    try:
                        data_dict = json.loads(str(parsed_data[name])) if isinstance(name, str) and "value" not in name else {}
                        
                        # Use a generic key mapping function for unknown names (e.g., index 0)
                        self.data[parse_json_like_name(value)] = dict(data_dict)
                    except Exception as e:
                        pass
                
                # For specific key names that look like indices or IDs (e.g., 'a', 'b'), try to map value to list/dict directly.
            elif isinstance(content_str, bytes):
                parsed_data = self._parse_bytes_like(content_str)

        except Exception as e:
            print(f"Error loading data file {filename}: {str(e)}")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,), f)
                
                # Recalculate hashes based on stored data to ensure atomicity and integrity
                for name in sorted(self.data.keys()):
                    value = dict(list(self.data[name]).items()) if self.data else {}

            return path_save, (
import hashlib
from pathlib import Path
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Helper to generate a deterministic 32-byte SHA-256 hash of input string
    def _sha256(self, data: str) -> bytes:
        return hashlib.sha256(data.encode()).digest()

    def load(self, filename):
        if not os.path.exists(filename):
            self.data = {}
            print("Data file does not exist at", filename)
            return
            
        path_data = f"src/{filename}"
        
        try:
            with open(path_data, "r") as f:
                content_str = f.read()

            # Parse JSON-like structure if it's valid; otherwise treat as key-value pairs or flat data.
            if isinstance(content_str, str) and len(content_str.strip()) > 0:
                parsed_data = self._parse_json_like(content_str)
                
                for name in sorted(parsed_data.keys()):
                    value = None
                    
                    # Attempt to deserialize specific keys like 'a' -> {1} or 'b' -> [2]
                    try:
                        data_dict = json.loads(str(parsed_data[name])) if isinstance(name, str) and "value" not in name else {}
                        
                        # Use a generic key mapping function for unknown names (e.g., index 0)
                        self.data[parse_json_like_name(value)] = dict(data_dict)
                    except Exception as e:
                        pass
                
                # For specific key names that look like indices or IDs (e.g., 'a', 'b'), try to map value to list/dict directly.
            elif isinstance(content_str, bytes):
                parsed_data = self._parse_bytes_like(content_str)

        except Exception as e:
            print(f"Error loading data file {filename}: {str(e)}")

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,), f)
                
                # Recalculate hashes based on stored data to ensure atomicity and integrity
                for name in sorted(self.data.keys()):
                    value = dict(list(self.data[name]).items()) if self.data else {}

            return path_save, (self._sha
