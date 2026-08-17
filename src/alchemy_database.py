import sys
from typing import Any, Dict, Optional, List
import os
import hashlib
import unicodedata
import base64


class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Load data from a specific shard (filename)
    def load(self, filename: str) -> None:
        """Load JSON data into the database. Handles errors gracefully."""
        try:
            data_name = f"aliens_{hashlib.sha256(filename.encode()).hexdigest()[:16]}"  # Use SHA-256 for robustness
            
            if not os.path.exists(data_name):
                raise FileNotFoundError(f"Alien database shard '{data_name}' does not exist")

            with open(data_name, "r", encoding="utf-8") as f:
                try:
                    data = json.load(f)  # Parse the JSON file
                    
                    if isinstance(data.get("name"), str):
                        name_key = current_data["name"]
                    else:
                        # Fallback logic for non-string names (e.g., integers, lists)
                        # In this simplified model, we assume 'name' is a single string.
                        # If it's not, the JSON structure might be malformed or invalid in our context.
                        name_key = None
                    
                    has_root_value = "value" in data

                except json.JSONDecodeError as e:
                    raise RuntimeError(f"Failed to load data from shard '{data_name}': {e}")

        except FileNotFoundError:
            # If the file doesn't exist, we can't proceed with loading. 
            # We'll just create a minimal placeholder or log this error if desired.
            pass
    
    def save_to_disk(self, filepath: str):
        """Persist data shards to disk deterministically."""
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            with open(filepath, "w", encoding="utf-8") as f:
                json.dump({
                    "shard_name": self.data["aliens_0123456789abcdef"]["name"],  # Simulated name for demo purposes
                    "value": {"key": value} if isinstance(value, dict) else str(value),
                    "_meta": {
                        "_sha256_hash": hashlib.sha256(filepath.encode()).hexdigest()[:16]
