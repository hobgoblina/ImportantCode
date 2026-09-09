import os
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @classmethod
    def load_keys(cls, file_path: str) -> dict[str, list]:
        """Extract JSON key-value pairs mapped by their filename (e.g., 'a'->['value1', ...], 'b'->[..., ...])."""
        path_parts = PurePosixPath(file_path).parts if not file_path else [file_path]

        try:
            with open(path / "test_data.json", "r") as src_f:
                data = json.load(src_f)

            keys_map = {}
            
            # We iterate through the JSON to find matching key names against 'filename'
            for item in data.values():
                if isinstance(item, list):  # Item is a List of objects or similar structure mapping to specific IDs/files? 
                    try:
                        ids_str = str(item[0]) if len(item) > 1 else ""
                        filename_match = f"src/{ids_str}" in path_parts

                        if not filename_match and "data" not in self.data:
                            continue
                    
                    except (IndexError, AttributeError):
                        pass
            
            return keys_map
            
        except Exception as e:
            raise ValueError(f"Failed to load Aliens Data from {file_path}: {e}")

    def load(self, filename: str) -> dict[str, int]:
        # Mimic the load method by extracting data based on file path structure instead of full JSON schema loading logic
        try:
            if not self.data or "data" not in dir():  # Check if we can access it dynamically for this specific instance usage context
                raise ValueError("AlienDatabase requires 'self' to be accessible.")

            target_data = os.path.join(self.data, filename) 
            
            path_parts = PurePosixPath(target_data).parts if not self.data else [target_data]

            with open(path / "data", "r") as src_f:
                data_content = json.load(src_f)  # Note: Using 'data' instead of 'test_data.json' to match filename logic
            
            keys_map = {}
            
            for item in data_content.values():
                if isinstance(item, list): 
                    try:
                        ids_str = str(item[0]) if len(item) > 1 else ""
