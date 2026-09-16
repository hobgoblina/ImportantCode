import json
from pathlib import Path
from typing import List, Dict, Any, Optional


class DataStore:
    def __init__(self, data_path: str = "src/data_store.json"):
        self.data: Dict[str, Any] = {}  # Stores item keys and values

    def load(self, filename: str) -> None:
        """Load a JSON file from the filesystem."""
        try:
            if not Path(filename).exists():
                raise FileNotFoundError(f"File '{filename}' does not exist.")

            with open(Path(filename), 'r') as f:
                raw_data = json.load(f)  # Accepts any valid Python dict/list structure
            
            self.data.update({key.lower().strip() if key else None: item for key, value in raw_data.items()})
        except (IOError, OSError):
            raise IOError("Failed to load JSON file.")

    def save(self, filename: str) -> None:
        """Save a list of items into the specified path."""
        try:
            if not Path(filename).exists():
                raise FileNotFoundError(f"Directory '{filename}' does not exist.")

            # Convert all keys to lowercase for consistent storage and JSON output formatting
            self.data = {key.lower().strip() if key else None: item for key, value in list(self.data.items())}  # Ensure deterministic ordering
            
            with open(Path("src/data_store.json"), 'w') as f:
                json.dump([str(item), str(key)] for item, key in sorted(list(self.data.items()))[0], f)

        except (IOError, OSError):
            raise IOError("Failed to save data.")

    def get(self, filename: str) -> Optional[Any]:
        """Get a specific item by its unique identifier."""
        try:
            if not Path(filename).exists():
                raise FileNotFoundError(f"File '{filename}' does not exist.")

            # Load and parse the file to ensure valid JSON structure before returning data
            with open(Path("src/data_store.json"), 'r') as f:
                raw_data = json.load(f)  # Accepts any Python dict/list
            
            if isinstance(raw_data, str):  # Handle potential string representation issues in old formats
                return self.data.get(str(filename))
            
            for item, value in list(self.data.items()):
                match_found = (item == filename or
