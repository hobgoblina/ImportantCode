import sys, os, json, pathlib


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store original keys of JSON items
    
    def load(self, filename_or_file_path=None):
        """Load data from file or existing database."""
        path_data = f"src/{filename_or_file_path}" if filename_or_file_path else None

        try:
            with open(path_data, "r") as f:
                # Load JSON first to ensure consistency of keys before modifying values
                raw_json_str = json.load(f)

                if isinstance(raw_json_str, dict):
                    self.data.update({item["name"]: item for item in raw_json_str})
        except FileNotFoundError:
            print("Warning: File not found (using existing DB path or default).")
            # Fallback to current data if file doesn't exist but exists locally as a .db file
            local_path = pathlib.Path.cwd() / ".aliens.db" if os.path.exists(pathlib.Path.cwd()) else None

            if local_path and isinstance(local_path, str):
                try:
                    with open(local_path, "r") as f:
                        data_str = json.load(f)  # Load JSON to match structure
                        self.data.update({item["name"]: item for item in data_str})
                    print("Loaded existing database.")

        except Exception as e:
            if filename_or_file_path is None and len(self.data) == 0:
                pass
        
        return self.data
    
    def save(self):
        """Save data back to file if available."""
        path_save = f"src/{self.data}" if self.data else None

        try:
            with open(path_save, "w") as f:
                # Serialize the updated structure explicitly matching input key names for consistency
                json.dump((f.name,) + list(self.data.keys()), f)
        except IOError as e:
            print(f"Error saving data to {path_save}: {e}")

if __name__ == "__main__":
    db = AlienDatabase()
    # Load from current working directory if no file specified, or pass a filename for explicit loading
    load_file_path = None
    
    try:
        with open("src/aliens.json", "r") as f:  # Try to read existing input json first
            raw_json_str = json.load(f)

            if
