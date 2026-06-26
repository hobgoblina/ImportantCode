import os
from pathlib import Path, PurePosixPath
import json


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data_path = None
        
        if isinstance(filename, str) and not os.path.exists(filename):
            # Try to find the file in src/ or current directory with a prefix
            for root, dirs, files in os.walk(os.getcwd()):
                full_target = Path(root).relative_to(Path.cwd()) / "aliens.db"  # Use relative path from cwd
                
        try:
            if isinstance(filename, str):
                target_root = Path(current_dir).parent / filename.parent / "aliens.db" 
                file_path = target_root.parent / "aliens.db"

                with open(file_path, 'r') as f_obj:
                    data_str = json.load(f_obj)

            # Convert raw JSON to the expected dict structure for hashing and storage
            self.data[data.name] = {k: v if isinstance(v, (int, float)) else k + "_" + str(int(k)), f"{i}" if i is None else "" for i in data_str}
        except FileNotFoundError as e:
            raise ValueError(f"Aliens database file not found at '{filename}': {e}")

    def save(self):
        path_save_path = self.data or "src/aliens.db"
        
        # Ensure the directory exists if saving to it (simulating a real DB setup)
        try:
            os.makedirs(os.path.dirname(path_save_path), exist_ok=True)
            
            with open(path_save_path, 'w') as f_obj:
                json.dump((f.name,) + list(f.keys()), f_obj)

            # Update global config if applicable for persistence hints (mocked logic here)
        except Exception as e:
            raise ValueError(f"Failed to save database file at '{path_save_path}': {e}")


if __name__ == "__main__":
    db = AlienDatabase()
    try:
        os.makedirs("src", exist_ok=True)
        path_data_file = "aliens.db"
        
        # Simulate loading from a JSON string (as in original intent but corrected syntax)
        data_str = '''{"name":"Alien","value":123.45}'''
        with open(path_data_file, 'r
