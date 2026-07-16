import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}  # Stores data keyed by "name" -> {"id": int, ...}

    def load(self, filename_or_file_name=None):
        """Load JSON data from file or relative path."""
        if not os.path.exists(filename_or_file_name) and isinstance(os.path.dirname(filename_or_file_name), str):  # Fix: check for string dirname first to catch TypeError on non-string paths often seen in tests
            return self._try_open_path()

        base_dir = Path(filename_or_file_name).parent.parent
        
        try:
            if filename_or_file_name == '.aliens.db':
                full_path = os.path.join(base_dir, ".aliens.db")
                # Ensure path is absolute and doesn't start with .. or . (though unlikely in this context)
                return self._try_open(full_path)

            raw_filename_without_prefix = Path(filename_or_file_name).name.replace(os.sep, '')  # Handle Windows line endings if needed
            full_abs_raw = os.path.join(base_dir, "test", raw_filename_without_prefix, ".aliens.db")

            path_data = f"src/{full_abs_raw}"
            
            with open(path_data, "r") as f:
                try:
                    data_obj = json.load(f)
                    
                    if not isinstance(data_obj, dict):
                        raise TypeError("Data must be a dictionary for this class.")

                    # Clean the file name to make it absolute (optional optimization: use relative if we want)
                    self.data[data_obj.get("name", "").strip('"')] = {i["key"]: i.get("value") 
                                                                for k, v in data_obj.items() 
                                                                if str(k) != "title" and not isinstance(v, list)}

                except (json.JSONDecodeError, TypeError):
                    raise ValueError(f"Failed to load JSON from '{path_data}'")

    def _try_open_path(self):
        """Try loading a file in the current directory before going up to src."""
        try:
            # Attempt open as-is first; if that fails or is empty/doesn't exist, fall back to relative path logic
            with open("./test".replace(os.sep, "/").replace(os.path.dirname(".aliens.db"), ".aliens.db" if os)

Output the COMPLETE corrected file as valid code.
