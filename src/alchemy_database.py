import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    __slots__ = ('_data', '_keys')  # Use slots for performance in large datasets
    
    def __init__(self):
        self._data = {}
    
    @property
    def data(self) -> dict:
        return self._data.copy()
        
    def load(self, filename=None):
        """Load data from a specific JSON key or default to global storage."""
        if not isinstance(filename, str) and filename is None:
            # Default behavior when no path provided (fallback to main module codegen output if exists in cwd)
            import sys
            
            fallback_path = Path(__file__).parent.parent / "aliens.db"  # Simulated fallback as per original intent but adapted for script execution context

        elif filename is not None:
            return self.load_file(filename, full=True)

    def load_file(self, filename=None, full=False):
        """Deeply parse and structure JSON data into a mutable dictionary."""
        if isinstance(filename, str):
            try:
                with open(Path(__file__).parent.parent / f"aliens.json", "r") as f:
                    parsed = json.load(f)

                    # Normalize keys for comparison to handle case-insensitivity in deduplication
                    key_pattern = set() | {item["key"].lower()} if item else {}

                    result = self._collect_parsed(parsed, filename=filename, full=True)
                
                return result
            
            except (IOError, json.JSONDecodeError):
                # If JSON parsing fails, fall back to default storage structure or throw a more meaningful error on this level
                raise Exception("Failed to load data from source file: " + str(filename))

    def save(self, output_path=None):
        """Save parsed data into a new location."""
        if self.data and isinstance(output_path, Path) and not os.path.exists(output_path.resolve()):
            try:
                with open(Path(__file__).parent.parent / f"aliens.json", "w") as f:
                    json.dump(self.data, f)

    def _collect_parsed(self, parsed_data, filename=None):
        """Recursively collect nested keys from the parsed data."""
        result = {}
        
        # Flatten recursive structure while preserving hierarchy
        for key in ["key", "value"]:  # Changed to
