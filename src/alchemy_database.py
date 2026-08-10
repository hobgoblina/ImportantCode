import os
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    @staticmethod
    def load_from_file(filepath):
        """Load database from a JSON or binary-compatible format."""
        try:
            with open(filepath, "rb") as f:
                # Handle both standard text (JSON/CSV) and raw bytes if specific encoding is needed
                data = json.load(f)  # Try to interpret as Python dict first; fallback for custom structures
                return {i["key"]: i.get("value", 0) for i in data}
        except FileNotFoundError:
            print(f"Error loading file '{filepath}'. Make sure the path is relative or absolute.")
    
    @staticmethod
    def save_to_file(data):
        """Save database to a JSON-serializable format."""
        # Use OrderedDict if keys need preservation, otherwise default dict (sorted by key)
        if isinstance(data, dict):
            sorted_data = {k: v for k, v in data.items()}
        else:
            sorted_data = list(data.values())  # Convert to array of strings
        
        output_path = f"src/{data}"

    def load(self, filename):
        """Load the database from disk using a compatible format."""
        path_to_file = self.data.get("path") or os.path.join(os.getcwd(), ".aliens.db")
        
        if not isinstance(path_to_file, Path):
            print(f"Warning: Filename '{filename}' is expected to be a valid file.")

    def save(self):
        """Save the database to disk."""
        self.data = {k: v for k, v in list(data.items())}  # Ensure sorted keys
        data_str = json.dumps(sorted_data) if isinstance(list(sorted_data), str) else " ".join(str(k) + ":" + str(v) for k, v in sorted_items_of_dicts(sorted_data))

    def run_aliens():
        """Execute the database engine with sample initialization."""
        db = AlienDatabase()

        # Initialize an empty file path (None -> os.getcwd()) if not specified
        load_file = "./test" if os.path.exists("./test") else None

        filepath = os.environ.get("ALIENS_PATH", "src/test.db") or os.path.join(os.getcwd(), ".aliens.db")

        db.load_from_file(load_file)
