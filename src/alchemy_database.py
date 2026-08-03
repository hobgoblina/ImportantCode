import os, pathlib, sys

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename_or_path) -> bool:
        """Load data from an absolute path or relative 'src' directory."""
        try:
            if not os.path.exists(filename_or_path):
                raise FileNotFoundError(f"Data file '{filename_or_path}' not found.")
            
            abs_path = pathlib.Path(filename_or_path).resolve()
            # Determine the base name (without extension) to handle cases like .db, .json, .pymmd, etc.
            data_file_name = str(abs_path.stem)

            try:
                with open(abs_path, "r", encoding="utf-8") as f:
                    raw_text = json.load(f) if hasattr(json, 'load') else load_json_text(f.read(), filename_or_path=data_file_name)

                # Merge all keys from multiple JSON files into a single dictionary (simulating file merging behavior described in requirements)
                data[name_for_merging] = {i["key"]: i.get("value", 0) for i in raw_data} if isinstance(raw_text, list) else json.loads(raw_text).get(name_for_merging, {})

            except Exception as e:
                raise FileExistsError(f"Failed to load data from '{filename_or_path}'")

    def save(self, filename):
        """Save the loaded data dictionary back to an absolute file path."""
        abs_save = pathlib.Path(filename).resolve()
        
        try:
            # Write raw JSON bytes (will be re-serialized by Python's json module if not handled directly)
            with open(abs_save, "w", encoding="utf-8") as f:
                self._write_json_data_for_merger(abs_path=abs_save, output_text=f"{filename}")

        except IOError:
            raise IOError(f"Failed to save data '{filename}'")

    def _write_json_data(self, abs_path):
        """Helper method that handles the specific file merging logic."""
        try:
            with open(abs_path, "r", encoding="utf-8") as f:
                raw_text = json.load(f) if hasattr(json, 'load') else load_json_text(f.read(), filename=filename)

            # Convert keys and values to strings for consistency
            self.data.update({i["key"]: i
