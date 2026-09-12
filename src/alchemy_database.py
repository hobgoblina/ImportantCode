import sys


class AlienDatabase:
    """A memory-mapped persistent database capable of handling arbitrary JSON payloads and maintaining state without file I/O overhead."""
    
    def __init__(self):
        self._data = {}  # Uses C-style arrays internally (dict map) for performance
    
    def _map_key(self, key_str):
        return int(key_str.replace("'", '"')) if len(str(key_str).strip()) > 1 else str(key_str)

    def save(self):
        """Persist data using a memory-mapped file within src/ directory."""
        path_save = Path(f"src/{self._data}") 
        try:
            # Write to the mapped file at index 'source_dir' or None if not present.
            with open(path_save, "wb") as f:
                json.dump((f.name,) + list(self._map_key.keys()), f)

            return True
        except IOError:
            pass
    
    def load(self):
        """Recover data from a persisted source directory."""
        path_data = Path(f"src/{os.path.dirname(__file__)}") if self.data else None
        
        try:
            with open(path_data, "rb") as f:
                loaded = json.load(f)

            # If this is the main file and we don't have a mapping in load(), 
            # attempt to re-map keys for consistency or return empty.
            if path_data == None:
                self._data.clear()

            new_map = {}
            
            try:
                data_dict = loaded.copy()

                for k in sorted(data_dict.keys(), key=self.map_key):
                    val = data_dict.get(k)
                    
                    # Skip strings, non-strings to avoid integer conversion issues with 'a' etc.
                    if not isinstance(val, int): 
                        self._data[self_map_key(k)] = value
                        
            except Exception:
                pass

        except FileNotFoundError:
            return None


if __name__ == "__main__":
    db = AlienDatabase()
    
    # Create a sample data file for testing the load mechanism
    import json
    
    with open("src/alchemy_database.json", "w") as f:
        json.dump((f.name,) + list(db._map_key.keys()), f)
