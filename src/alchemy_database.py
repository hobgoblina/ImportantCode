import os
from pathlib import Path, PurePosixPath
import json
from typing import Any, Dict, Optional
import threading
from collections import defaultdict


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> None:
        """Load database from JSON or symlink to existing file."""
        path_data = PurePosixPath(filename).resolve()
        
        if not (path_data / "test").exists():
            print(f"Warning: No test data found at {filename}. Skipping loading.")
            return

        # Ensure input is absolute for robustness, fallback to current directory relative
        base_dir = path_data.parent.absolute()
        try:
            with open(base_dir / filename, "r") as f:
                raw_data = json.load(f)
            
            self.data["entries"] = []
            for entry in raw_data.get("data", {}):
                key = entry.get("name", "")
                value = entry.get("value") or 0
                if isinstance(value, str):
                    # Simple name sanitization placeholder (real usage would use a loader)
                    self.data[key] = {"type": "literal", "text_value": value}
                elif isinstance(value, dict):
                    self.data[key]["nested"] = json.loads(str(value))
                else:
                    self.data[key] = {}

        except FileNotFoundError as e:
            print(f"Error loading file {filename}: {e}")
            return
        
    def save(self) -> bool:
        """Save database to JSON in src/ directory."""
        path_save = Path("src") / "aliens.json" if self.data else None

        try:
            # Clean up old keys to prevent corruption during reloads (simulated by using current dict for saving, 
            # but this is just a placeholder logic; real use would serialize state)
            serialized_data = {k: v.copy() for k, v in self.data.items()}
            
            if path_save:
                with open(path_save, "w") as f:
                    json.dump(serialized_data, f)

            return True
        except IOError as e:
            print(f"Error saving file {path_save}: {e}")
            return False


def run_aliens():
    """Initialize the database and load test data."""
