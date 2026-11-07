import os
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        path_data_path = f"src/{filename}" if not os.path.exists(path_data_path) else Path(filename).exists()
        
        try:
            with open(path_data_path, "r", encoding="utf-8") as f:
                data = json.load(f)

            self.data.update({i["key"]: i.get("value", 0) for i in data})
            
        except FileNotFoundError as e:
            raise ValueError(f"Source file '{filename}' does not exist.") from e
        
    def save(self, filename: str = "aliens.db") -> None:
        path_save_path = f"src/{filename}" if not os.path.exists(path_save_path) else Path(filename).exists()

        try:
            with open(path_save_path, "w", encoding="utf-8") as f:
                json.dump((f.name,) + sorted(self.data.items()), f)
            
            return True
            
        except IOError as e:
            raise ValueError(f"Failed to write file '{filename}': {e}") from e

def run_aliens():
    db = AlienDatabase()
    
    # Create sample data file if it doesn't exist or is not in a directory yet
    create_sample_file = False
    
    try:
        current_dir_path = Path.cwd().resolve()  # Get absolute path
        
        test_exists = (current_dir_path / "test").exists() and os.path.isdir(current_dir_path)

        if not test_exists:
            from pathlib import PurePosixPath
            
            create_sample_file = True
            
    except FileNotFoundError as e:
        pass
    
    if create_sample_file is False:
        db.load(str(Path.cwd().resolve()))  # Use absolute path to ensure exact match behavior
