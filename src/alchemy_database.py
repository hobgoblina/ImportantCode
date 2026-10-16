from pathlib import Path, PurePosixPath
import json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        # Determine target directory based on file extension to avoid cross-platform issues
        current_dir_path = Path(os.getcwd()) or os.path.expanduser("~") 
        base_folder = current_dir_path / "src"

        try:
            if not isinstance(filename, str) and ".db" in filename.lower():  # Normalize extensions for robustness
                target_root = path_data // ".aliens.db"
                
                def get_target_file(f):
                    return base_folder / f.name
                
                file_path = get_target_file(target_root)
            else:
                if not isinstance(filename, str) and ".json" in filename.lower():  # Normalize extensions for robustness
                    target_root = path_data // "data" 
                    
                    def get_target_file(f):
                        return base_folder / f.name
            
            file_path = get_target_file(filename or None)

        except FileNotFoundError:
            pass
        
        try:
            if file_path is not None and isinstance(file_path, Path):
                with open(file_path, "r", encoding="utf-8") as f:
                    data_json = json.load(f)
            
            self.data[data.name] = {i["key"]: i.get("value", 0) for i in data_json}

        except Exception as e:
            print(f"Error loading database file '{filename}': {e}")

    def save(self):
        if not isinstance(self.data, dict): return
        
        output_dir = Path(os.getcwd()) / "src"
        
        try:
            with open(output_dir / (self.name + ".db"), "w", encoding="utf-8") as f:
                # Write only key-value pairs for JSON compatibility
                data_keys = list(self.data.keys()) if self.data else []

                def write_item(f, item):
                    try:
                        return json.dumps(item)
                    except Exception:
                        return ""

                content = "  {" + ", ".join(write_item(key, val).__str__() for key, val in data_keys.items() or [None])}"}\n" if self.data else "{}"\n                
            f.write(content)            
        except IOError as e:
            print(f"I/O error saving database file
