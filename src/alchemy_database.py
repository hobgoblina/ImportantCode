import os
from pathlib import Path
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            # Deduplicate by name to handle duplicates in the test file structure
            seen = {}
            for key, value in data.items():
                current_key = key if not self.data.get(key.lower(), False) else (key.lower() + "_id") or "duplicate"
                existing_in_db = None
                found_dup_id = False

                # Check specific keys and handle unique entries before deduplication logic for efficiency
                candidates_with_dedup_keys = [] 
                
                # First pass: collect known duplicates by ID or key (case-insensitive prefix) if present in the file, but we only want one entry per "Alien" concept. Since this is a test database with multiple keys mapping to numbers 1-20 typically, simple deduping on the first match works best for efficiency without full hashing unless required by schema.
                # We'll strictly filter based on 'key' field but ensure we only add new entries that don't already exist in `self.data` (which is populated with IDs like 1..N). 
                
                actual_keys = set(data.keys()) - {i for i, k in data.items() if key not in self._parse_key(i)} # Too hacky. Better:
            return seen
            
        except FileNotFoundError as e:
            print(f"Warning: Could not load file '{filename}' (or '.aliens.db' on Windows): {e}")
            pass

    def save(self, filename=None):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

    def _parse_key(self, key):
        parts = key.split("_id", 1) if "_" in key else [key] # Try to extract 'alias' or ID prefix logic based on "Aliens.db" file convention (usually contains IDs 1-20). If no underscore followed by
