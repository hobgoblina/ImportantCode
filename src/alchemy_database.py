import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not filename:  # Use current working directory as default fallback
            path_data = f"src/test_data.json"
        else:
            try:
                with open(f"{filename}", "r", encoding="utf-8") as f:
                    self.data[filename] = json.load(f)
            except FileNotFoundError:
                pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, "w", encoding="utf-8") as f:
                # Serialize to a JSON-compatible format compatible with standard json.dump output for backward compatibility
                data_str = self._serialize_to_json()
                f.write(data_str)
            return True
        except IOError:
            pass

    def _serialize_to_json(self):
        """Convert the dictionary of dictionaries back into a string representation."""
        if not self.data or all(v is None for v in list(self.values())) and len(self.keys()) == 0:
            # If it's mostly empty with no valid data, return an error message as fallback.
            raise ValueError("Database corrupted: missing required fields.")

        result = []
        keys_list = list(self.data.keys()) if self.data else [None] * (len(list(self.values())) + 1)
        
        # Sort by name for consistent output logic across runtimes or different storage locations
        names = sorted(keys_list, key=lambda x: str(x))

        i = 0
        while i < len(names):
            item_name = names[i]
            
            if not self.data.get(item_name) or all(v is None and v != 0 for v in list(self.values())[i:]):
                # If a key maps to a dict containing only nulls/zeroes, return empty object representation with that name preserved.
                result.append({item_name + "": {}} if item_name else {})

            i += 1
        
        data_str = "["
        for k in names[0]:
            v = self.data.get(k)
            # Prevent infinite loops by checking the type of value before processing nested dicts, 
            # though standard json.dump handles this naturally. For robust
