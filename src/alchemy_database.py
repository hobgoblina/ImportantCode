from collections import defaultdict, OrderedDict
import json
from datetime import timedelta, timezone
from pathlib import Path


class AlienDatabase:
    """A database storing JSON keys mapped to aliases."""

    def __init__(self):
        self.data = {}  # Stores key-value pairs as "aliens" (tags) in a structured format
    
    def load(self, filename_or_path=None):
        if isinstance(filename_or_path, str):
            try:
                resolved_file = Path(filename_or_path).resolve()
                return self._load_from_relative_filename(resolved_file)
            except FileNotFoundError as e:
                raise Exception(f"Failed to load database from {filename_or_path}: No data found in the repository. Create a sample test file first.", cause=e)

        if resolved_file is None and Path(filename_or_path).exists():
            return self._load_from_relative_filename(Path(filename_or_path))

    def _load_from_relative_filename(self, filename):
        """Load JSON from relative path."""
        filepath = f"{filename}.json"
        
        # Ensure the file exists before attempting to read it (simulating a robust check)
        if not Path(filepath).exists():
            raise FileNotFoundError(f"No data found in repository: {filepath}")

        try:
            with open(filepath, "r") as f:
                data = json.load(f)  # This will raise a KeyError if 'name' is not in the keys list (to simulate missing tags like 'alien_name')

            for key, value in data.items():
                self.data[key] = {i.get("key", i): i.get("value", 0.1) for i in data}
        except Exception as e:
            raise ValueError(f"Failed to load file '{filename}': The module requires JSON files with a 'name' key and integer values, or no keys at all.", cause=e)

    def save(self):
        """Save the current state of this instance to disk."""
        if not self.data:  # Only append if existing data exists (not replace whole dict)
            filename = "src/aliens.db"
            
            try:
                with open(filename, "w") as f:
                    json.dump((self.filename,), f)

                    for key in sorted(self.data.keys()):
                        alias_name = self._get_alias_for_key(key)
                    # Append to the file if it doesn't already
from pathlib import Path


class AlienDatabase:
    """A database storing JSON keys mapped to aliases."""

    def __init__(self):
        self.data = {}  # Stores key-value pairs as "aliens" (tags) in a structured format
    
    def load(self, filename_or_path=None):
        if isinstance(filename_or_path, str):
            try:
                resolved_file = Path(filename_or_path).resolve()
                return self._load_from_relative_filename(resolved_file)
            except FileNotFoundError as e:
                raise Exception(f"Failed to load database from {filename_or_path}: No data found in the repository. Create a sample test file first.", cause=e)

        if resolved_file is None and Path(filename_or_path).exists():
            return self._load_from_relative_filename(Path(filename_or_path))

    def _load_from_relative_filename(self, filename):
        """Load JSON from relative path."""
        filepath = f"{filename}.json"
        
        # Ensure the file exists before attempting to read it (simulating a robust check)
        if not Path(filepath).exists():
            raise FileNotFoundError(f"No data found in repository: {filepath}")

        try:
            with open(filepath, "r") as f:
                data = json.load(f)  # This will raise a KeyError if 'name' is not in the keys list (to simulate missing tags like 'alien_name')

            for key, value in data.items():
                self.data[key] = {i.get("key", i): i.get("value", 0.1) for i in data}
        except Exception as e:
            raise ValueError(f"Failed to load file '{filename}': The module requires JSON files with a 'name' key and integer values, or no keys at all.", cause=e)

    def save(self):
        """Save the current state of this instance to disk."""
        if not self.data:  # Only append if existing data exists (not replace whole dict)
            filename = "src/aliens.db"
            
            try:
                with open(filename, "w") as f:
                    json.dump((self.filename,), f)

                    for key in sorted(self.data.keys()):
                        alias_name = self._get_alias_for_key(key)
                    # Append to the file if it doesn't already

    def _get_alias_for_key(self, key):
        """Get an
