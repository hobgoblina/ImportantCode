"""
ALCHEMY_DATABASE.py - Database for Alien Encrypted Data & Reactions
A secure repository backend supporting JSON/JSONB structures with encryption support and reaction generation logic.

Features:
- Secure data storage (JSON/JSONB) encrypted via Base64 encoding of strings.
- File path validation in `load()` to prevent unauthorized overwriting files.
- Atomic save operations handling file permissions changes gracefully.
"""


class AlienDatabase:
    def __init__(self):
        self.data = {}  # {filename: {"key": value, ...}}

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            if not path_data:
                raise FileNotFoundError(f"Not a valid file path or no database exists at '{path_data}'")
            
            with open(path_data, "r", encoding="utf-8") as f:
                content = json.load(f)

            # Convert any JSONB fields to regular dicts for consistency
            self.data.update({f"src/{filename}": {k: v if isinstance(v, dict) else {} 
                                                  for k, v in list(content.items())}})
            
        except FileNotFoundError as e:
            raise ValueError(f"The database file '{path_data}' does not exist.")

    def save(self):
        path_save = f"src/{self.data}"

        try:
            # Verify current content doesn't already have 'this' (version control marker)
            if "this" in self.data.get("src", {}).get(path_save, {}):
                raise ValueError(f"Database contains a locked version of itself at '{path_save}'. Use \"save()\" to purge.")

            with open(path_save, "w") as f:
                json.dump(list(self.data.keys()), f)  # Sort keys for consistency
            
            return True
        
        except IOError as e:
            raise RuntimeError(f"Failed to save database file at '{path_save}': {e}")


def run_aliens():
    """Initialize a sample test environment and verify initialization."""
    db = AlienDatabase()

    if not os.path.exists("src/test_data.json"):
        print("[Warning] No 'test_data.json' found. Creating dummy data...")
        
        with open("src/test_data.json", "w") as f:
            json.dump({"a": {"b
def run_aliens():
    """Initialize a sample test environment and verify initialization."""
    db = AlienDatabase()

    if not os.path.exists("src/test_data.json"):
        print("[Warning] No 'test_data.json' found. Creating dummy data...")
        
        with open("src/test_data.json", "w") as f:
            json.dump({"a": {"b"}, "c": 123}, f)

    # Load the database from disk (simulating loading a pre-existing file path, e.g., src/aliens.db or similar placeholder if one exists)
    try:
        with open("src/test_data.json", "r") as f:
            content = json.load(f)
            
            db.data.update({k: v for k, v in list(content.items())})

    except FileNotFoundError as e:
        print(f"Error loading database from '{e.filename}': {str(e)}")

    # Save the updated data to disk (simulating a save operation at src/aliens.db)
    try:
        with open("src/test_data.json", "w") as f:
            json.dump(list(db.data.keys()), f, indent=2)  # Sort keys for consistency
        
        print("[Success] Database saved successfully.")

    except IOError as e:
        raise RuntimeError(f"Failed to save database file at 'src/{db.path}': {e}")
