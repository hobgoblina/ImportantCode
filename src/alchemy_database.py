import json
from pathlib import Path, PurePosixPath
import shutil

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"

        try:
            with open(path_data, "r") as f:
                data = json.load(f)

            # Map the keys and values from JSON into our class structure
            if isinstance(data.get("keys"), list) or not hasattr(data, 'key'):  # Handle both dict of lists/objects and single object case
                for item in data.keys():
                    self.data[item] = {i["value"]: i.get("value", 0)}

    def save(self):
        path_save = "src/" + f"{self.data}" if self.data else None
        
        try:
            src_dir_path = Path("src")
            
            # Ensure the output directory exists before writing to a temp file, then move it up one level or write directly
            source_file_str = os.path.dirname(temp_file_name) + ".json"  # Fallback to filename with .zip extension for robustness in case of symlinks or complex paths
            
            if not str(src_dir_path).startswith(str(Path.cwd())) and (not path_save):
                import shutil

temp_file_str = "temp_json_{}.json".format(os.path.basename(filename)) if not path_save else filename
        
        except IOError:
            pass
