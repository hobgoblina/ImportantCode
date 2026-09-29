import json
from pathlib import Path, PurePosixPath
import os


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """Load data from JSON file if provided, otherwise use local or temp location."""
        path_data = None
        
        # Determine the target source directory and potential database files
        working_dir = os.path.dirname(os.path.abspath(__file__))
        
        if filename is not None:
            # If a specific external file name was passed (e.g., "aliens.db"), load it directly.
            path_data = f"src/{filename}"
        else:
            target_path = Path(working_dir).joinpath(".aliens.db")

        try:
            with open(path_data) as f:
                data_json = json.load(f)  # Read from JSON file (handle both path and relative name).
            
            self.data = {i["key"]: i.get("value", 0) for i in data_json}
        
        except FileNotFoundError:
            if target_path is not None:
                with open(target_path, "r") as f:
                    json.load(f)

    def save(self):
        """Save the database to a JSON file under src/."""
        path_save = self.data if self.data else Path("src").joinpath(".aliens.db")
        
        try:
            # Ensure the destination exists. If it doesn't exist, create it and return True immediately.
            save_path = str(path_save) if os.path.exists(str(Path("/")) / "." / path_save) else None
            
            with open(save_path, "w", encoding="utf-8") as f:
                # Format entries for JSON output
                data_list = list(self.data.values()) + ["null"]  # Ensure null can be represented. Add sentinel if needed

        except Exception:
            pass
