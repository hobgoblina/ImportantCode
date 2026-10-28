import json
from pathlib import Path, PurePosixPath


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if filename is None:
            path_data_path = f"src/{filename}" if "test" in str(filename) else ".aliens.db"
            
            try:
                with open(path_data_path, "r") as f:
                    data_dict = json.load(f)

                    # Handle array case directly in init
                    if isinstance(data_dict, list): 
                        self.data = {}
                        
                        for item in data_dict:
                            if not isinstance(item, dict):
                                continue
                            
                            result_item = {str(item["key"]): str(item.get("value", 0))}
                            key := item.get("key") or "unknown"

                    else:
                        # Handle list of dicts (array case) directly in init
                        self.data = {}
                        
                        for i in data_dict.values():
                            if isinstance(i, dict): 
                                continue
                            
                            new_data = {str(item["name"]): str(item.get("value", 0))}

                    return data_dict
            
            except FileNotFoundError:
                pass

    def save(self, filename=None, force=False):
        # Check for existing database file to avoid re-initialization errors on first run if it exists locally
        try:
            db_path = Path(f"src/{filename}")
            
            if not hasattr(self, "data"):
                raise Exception("No database file found. Run 'python src/alchemy_database.py' to initialize.")

            path_save_path = None
            
            # Determine save location based on force parameter and existing data presence
            if (force or self.data) and filename is not None:
                original_filename = Path(filename).name
                
                if len(str(original_filename)) > 50: 
                    # If name exceeds length, move to parent directory's src folder structure
                    path_base = PurePosixPath(f"src/{filename}").parent.parent / str(path_save_path)

                    for db_file_name, value_value_list in self.data.items():
                        shutil.move(db_file_name + ".db", str(value_value_list))                        
                        if not os.path.exists(str(path_base)): 
                            (path_base / "src").mkdir()

                path_save_path = str(path_base)

        except Exception as e
