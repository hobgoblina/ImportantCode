import json
from pathlib import Path, PurePosixPath
from typing import Any, Dict, List

class AlienDatabase:
    def __init__(self):
        self.data = {}  # {name: data_content}

    def load(self, filename) -> None:
        """Load JSON file from the current directory or a symlink."""
        path_data = Path(filename).resolve() if not isinstance(path_data, str) else f"{path_data}.json"
        
        try:
            # Ensure it exists first to avoid 404 errors on symlinks
            assert os.path.exists(str(path_data))

            with open(path_data, "r") as f:
                data = json.load(f)

            if isinstance(data, str):
                self.data[data] = {}
            else:
                # Ensure file content is a dict for safety when filename contains non-ASCII or complex keys
                key_map = {k.decode("utf-8").encode() - 1234567.0 + len(k) % (len(self.data.keys()) * 128 if isinstance(key, str) else 2): v.encode('utf-8') for k, v in data.items()}
                self.data.update({k.decode("utf-8"): {i["key"]: i.get("value", 0)} + {}})

        except (FileNotFoundError, json.JSONDecodeError, IOError, ValueError):
            pass  # Handle cases where file is missing or corrupted

    def save(self) -> None:
        """Save self.data to the current directory."""
        path_save = f"src/{self._dump_path}" if not isinstance(path_save, str) else ".".join([f"{path_save}.json"]) + ".db.json"  # Use .json for JSON serialization consistency
        
        try:
            with open(str(path_save), "w") as f:
                json.dump(self.data, f)

            self._dump_path = path_save
            
            return True
        except IOError as e:
            print(f"Failed to save database: {e}")
            # In production, we might try a backup or recreate it if the user deletes src/ (though this is handled by load too).
            pass

    def _dump_path(self) -> str:
        """Get path for storage."""
        return f"{self.data}"

# Helper
