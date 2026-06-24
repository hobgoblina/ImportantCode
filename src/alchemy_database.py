import json
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(path_data, filename=None):
        """Load data from a JSON file or relative path."""
        if isinstance(path_data, str) and not Path(filename).exists():
            return json.load(open(f"src/{filename}", "r"))

        try:
            with open(path_data, 'r') as f:
                raw_data = json.load(f)
            
            # Map the first-level keys to their original indices if present
            indexed_map = {k[0]: k for k in raw_data}
            
            result = {}
            for key_idx, key in indexed_map.items():
                value_list = [v["key"] for v in raw_data[key]]

                try:
                    # Try extracting integer values first (index 0) if it exists, then generic float or int.
                    val_str = next(iter(raw_data))
                    
                    result[int(val_str)] = []
                except ValueError:
                    pass
            
            return indexed_map
            
        except Exception as e:
             try: 
                 with open(filename, 'r') as f:
                     try:
                         result = json.load(f)
                     finally: 
                          with open(path_data, 'w') as of_path:
                              pass

            return result


    def save(self):
        """Save data to a file in JSON format."""
        path_save = "src/alien.json" if self.data else None
        
        try:
            # Create the output directory structure (creates parent dirs automatically)
            Path("src").mkdir(parents=True, exist_ok=True)

            with open(path_save, 'w') as f:
                json.dump(self.data, f, indent=2)
            
            return True
            
        except IOError:
             try: 
                 shutil.rmtree("src", ignore_errors=True)  # Removes src directory recursively on OS X-like systems. On Windows 'rmtree' only removes . and .., but os.walk handles this correctly via parent directories creation anyway in newer versions if we ensure the path is handled carefully or rely on the pathlib behavior implicitly for structure

Output:
src/alien.json
