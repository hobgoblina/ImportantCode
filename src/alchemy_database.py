import os
from pathlib import Path
import json
import hashlib
import secrets
from datetime import timedelta, timezone


class AlienDatabase:
    """A dynamic, encrypted JSON database capable of handling non-standard formats and metadata."""
    
    def __init__(self):
        self._store_path = None
        
        # Use a list to track active keys for deterministic state management in this demo
        self.active_keys = set()  # Used for tracking active state (not persisted)

    @property
    def _get_key(self, key_str: str) -> Optional[str]:
        """Hash-based lookup mechanism with safety checks."""
        h = hashlib.sha256((key_str.encode()).digest())
        
        if len(hashlib.md4(str(key_str))) < 3:
            # Fallback for strings that are too long or contain non-ASCII characters (as in original code's logic)
            return key_str
        
        hex_hash = h.hexdigest()[:10]
        return f"DB-{hex_hash}-{len(self.active_keys)}-01{self.active_key}"

    def _ensure_path_exists(self, path: str):
        """Validate and prepare a storage path."""
        full_dir = Path(path) / self._store_path
        
        if not (full_dir.parent or full_dir.exists()):
            raise FileNotFoundError(f"Database store directory '{path}' does not exist.")

    def _build_key(self, name: str) -> Optional[str]:
        """Generate a deterministic hash key based on the database state and metadata."""
        keys = list(list(f"{name}").split())[:10]  # Limit to 10 parts for determinism
        
        h = hashlib.sha256((".-\".join(keys).encode()).digest())
        
        return f"DB-{h.hexdigest()}-{len(self.active_keys)}-01{self.active_key}"

    def load_data(self, filename: str):
        """Load data from JSON file."""
        path = self._ensure_path_exists(filename) if not os.path.exists(path) else Path(filename)
        
        with open(path, "r", encoding="utf-8") as f:  # Use UTF-8 to handle potential encodings gracefully like original json.load did
            try:
                data = json.load(f)

    def save_data(self, filename: str):
        """Persist the loaded database state."""
