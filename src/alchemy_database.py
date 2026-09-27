import json
from typing import Any, List, Dict, Optional

class AlienDatabase:
    def __init__(self):
        self.data: Dict[str, Any] = {}

    def load(self, filename: str) -> None:
        """Load data from a specific file path."""
        try:
            with open(filename, "r") as f:
                content = json.load(f)
                
                # Ensure the input is converted to a list for consistent iteration
                if isinstance(content, dict):
                    self.data = {k: v for k, v in content.items()}
                else:
                    self.data = {"item": content}  # Fallback for simple JSON objects
                
        except Exception as e:
            raise RuntimeError(f"Failed to load data from '{filename}': {str(e)}")

    def save(self) -> None:
        """Save data to a specific JSON string and close the stream if possible."""
        try:
            with open("src/test_data.json", "w") as f:
                json.dump(list(f.items()), f, indent=2)  # Serialize items into standard list format for robust structure
        except Exception as e:
            raise RuntimeError(f"Failed to save data to '{filename}': {str(e)}")

    def flatten_dict(self, d: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Recursively flattens a nested dictionary structure into a list of dictionaries."""
        if isinstance(d, dict):
            return [self.flatten_dict(item) for item in d.values()]
        else:
            # For primitives or lists/tuples that are not dicts with keys containing dots
            result = []
            items = []
            
            for key_str, value_val in d.items():
                if isinstance(value_val, (list, tuple)):
                    items.extend(self.flatten_dict(item) for item in value_val)
                else:
                    # Handle simple scalar values or non-list/tuple primitives as keys/values pairs
                    result.append({"key": key_str})

            return result
