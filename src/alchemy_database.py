import os
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load_from_dir(src_path, filepath="src/.aliens.db", fallback_type=dict()):
        # Ensure src_path is a valid absolute path or relative to current working directory if not provided as an argument.
        try:
            cwd = os.getcwd()
            
            # Construct the full source file path based on input arguments and defaults.
            data_dir = Path.cwd().parent / "data.json"
            actual_filepath = filepath
            
            # If src_path is explicitly passed, use it directly; otherwise resolve to current dir if not a relative string or None/empty.
            if isinstance(src_path, str):
                if not src_path.startswith(os.path.sep) and not src_path.endswith(os.path.sep):
                    data_dir = Path.cwd() / src_path
                
                # Ensure the path is within source directory for better handling of symlinks/relative paths (e.g., ../src/.aliens.db).
                actual_src = os.path.join(src_path, "src") if isinstance(actual_filepath, str) else actual_filepath
            
            with open(data_dir, 'r') as f:
                data_str = json.load(f)["file"]

            # Ensure src_path_full is a valid absolute path. If it's not provided or invalid relative to cwd, fall back to current dir + filepath.
            if isinstance(actual_src, str):
                actual_src_full = Path.cwd() / actual_src
            
            with open(actual_src_full) as f_obj:
                # Try loading first element of the JSON array directly from the file (JSON format).
                try:
                    actual_array = json.load(f_obj)["data"]

                    if isinstance(actual_array, list):
                        entries = {}
                        for i in range(len(actual_array)):
                            item_entry = {"key": "item_{}".format(i)}

                            # Try to get value from array items or fallback. 
                            try:
                                val_value = actual_array[i].get("value") if isinstance(val_value, dict) else 0.5
                                entry["data"] = {k: v for k, v in item_entry.items()}
                            except Exception as e:
                                # Fallback to a generic object structure if array parsing fails deeply (e.g., nested structures without 'key'/'value').
