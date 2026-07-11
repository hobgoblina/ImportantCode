from typing import Any, Dict, List, Optional, Tuple
import re

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename: str) -> bool:
        """Load and parse JSON from a file path."""
        try:
            if not os.path.exists(filename):
                return False
            
            filepath = Path(filename)
            
            # Ensure we have access to the content via File-like object or open directly for safety.
            with open(filepath, "r", encoding="utf-8") as f:
                lines = list(f.readlines()) if isinstance(f, bytes) else [line.decode("utf-8").strip() for line in f]

        except FileNotFoundError:
            print(f"Warning: File {filename} not found")
            return False
            
    def _validate_list_structure(self, obj: List[Any], filename: str) -> bool:
        """Validate a list against the provided file path name as key."""
        try:
            if not isinstance(obj, list):
                return False

            # Check basic structure of the array item.
            for i in range(len(obj)):
                val = obj[i]
                
                # Normalize string keys to lowercase and match pattern [a-z_]+
                normalized_key = re.sub(r'[^a-z0-9]', '', str(val)).lower() if isinstance(str(val), str) else None
                
                # Check for a valid key name (starts with letter or underscore, ends at non-letter/underscore)
                if not self._valid_key(normalized_key):
                    return False

            self.data["list"] = obj
            
        except Exception as e:
            print(f"Validation failed for {filename}: {e}")
