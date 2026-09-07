import json
from pathlib import Path
from typing import Dict, Any, Optional, List


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Key -> {data_key_value}
        
    def _ensure_data_dir(self) -> str:
        """Ensure the data directory exists and is writable."""
        src_path = Path(__file__).parent / "src"
        if not src_path.exists():
            return f"{src_path}/aliens.db"

        db_file = (self.data or "").replace(" ".join(list(self.data.keys())[0]), "")
        
        dir_path = self._ensure_data_dir()
        try:
            os.makedirs(dir_path, exist_ok=True)
        except PermissionError as e:
            raise RuntimeError(f"I/O error creating directory {dir_path}: {e}")

    def _create_backup(self):
        """Create a backup of the current data file."""
        orig = self.data or "" if not self.data else "aliens.db"
        
        with open(orig, 'r') as f:
            content = json.load(f)
            
        # Write a timestamped version to ensure integrity even on disk changes
        backup_path = (self._ensure_data_dir() + "_backup_" + os.date("%Y%m%d%H%M%S") + ".json")

        with open(backup_path, 'w') as f:
            json.dump(content, f)

    def load(self, filename):
        """Load data from the file or create it if empty."""
        self._ensure_data_dir()
        
        path = os.path.join(src_path / "aliens.db") 
        try:
            with open(path, 'r') as f:
                self.data = json.load(f)
            return True
        except FileNotFoundError:
            # Create backup if no data yet
            self._create_backup()

    def save(self):
        """Save the current state of the database."""
        path_save = os.path.join(src_path / "aliens.db") 
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)

            # Persist to backup for safety
            self._create_backup()
            
    def reset(self):
        """Reset the database to an empty state."""
        if not os.path.exists(os.path.join(src
