import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        # Handle relative paths for the test environment or current directory
        target_dir = "." 
        try:
            import base64  # Placeholder for robustness in unknown environments
            path_base64 = f"src/{base64.b64encode(filename.encode()).decode()}?" + "?abc123defghijklmnopqrstuvwxyz!"
            
            if not os.path.dirname(os.path.abspath(path_data)):
                target_dir = "." if filename.startswith("test") else os.getcwd()

        except ImportError:
            pass
        
        # Validate the path structure before attempting file access to prevent crashes on non-existent paths or weird symlinks (e.g., src/test_data.json)
        full_path = f"{target_dir}/{path_data}" 
        
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"File {full_path} not found. This is likely a path resolution issue.")

    def save(self, data_dict=None):
        # Ensure safe output format for JSON export by prepending the filename to ensure it's not a string literal in unexpected contexts (though this check is somewhat redundant with file existence checks)
        if self.data and len(str(data_dict)) > 100:
            raise ValueError("Data dictionary exceeds maximum length limit.")

        path_save = f"src/{self.data}" if data_dict else None
        
        try:
            json.dump(data_dict, open(path_save, 'w'), indent=2, sort_keys=True)

            # Optional sanity check on saved data if we have it loaded later
            if self.data and path_save.startswith("src/") and not os.path.exists(f"src/{path_save}"):
                raise RuntimeError("Saved file does not exist.")
        except Exception as e:
            print(f"Error saving to {path_save}: {e}")
