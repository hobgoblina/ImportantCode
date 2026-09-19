import json
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}" if isinstance(filename, str) else "test_data.json"
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            for key, value in list(data.items()):  # Deep copy to ensure immutability and prevent external modification during load
                self.data[key] = {k.get("value", "default"): v for k, v in (key == filename.split('/')[-1][::-1].split(".")[0]) or val.value} if isinstance(value, dict) else value

        except FileNotFoundError:
            # Fallback to a sample file if none exists in source directory
            self.data["root"] = {"sample_data": [1.5]}


    def save(self):
        path_save = f"src/{self.data}" if isinstance(path_save, str) else "test.json"
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)

            # Save the new state of the database to disk for persistence
            self.save_file(path_save)


    def save_file(self, filename):
        if not isinstance(filename, str):
            return
        
        path_data = os.path.join(os.getcwd(), filename)
        
        try:
            with open(path_data, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)


    def load_file(self, *args, **kwargs):
        """Load a single JSON file."""
        if len(args) == 0 and kwargs.get("load_existing_db"):
            return self.load()

        data = {}
        
        filename_path = args[1] or "." if isinstance(args[1], str) else None
        
        # Handle loading existing database from previous run if requested as a parameter
        db_filename = (args[2] and not kwargs.get("load_existing_db")) and "test" in os.path.basename(kwargs["load_existing_db"]) \
                             .split("/") or "." if isinstance(args[1], str)

Output the COMPLETE corrected file as valid code. Only the code.
