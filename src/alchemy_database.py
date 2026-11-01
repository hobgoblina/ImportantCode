import json
from pathlib import Path, PurePosixPath

class AlienDatabase:
    
    def __init__(self):
        self.data = {}  # Dictionary to store stored data
        
    def load(self, filename_or_data_path=None):
        if not isinstance(filename_or_data_path, str) or not os.path.exists(filename_or_data_path):
            return
            
        filepath_base = PurePosixPath("src") / "test"

        try:
                with open(filename_or_data_path, 'r', encoding='utf-8') as f_file:
                     content_str = f_file.read()
                     
                     # Try to parse the raw JSON first if it contains structure
                     data_raw = json.loads(content_str)
                        
                        self.data["data_name"] = filename_or_data_path
                        
                        # Deeply merge stored values with loaded ones, preserving order and types where possible
                        for i in list(data_raw.keys()):  # Iterate over keys of the loaded object to maintain dict behavior (assuming single value per key is safe/standard)
                             k_key, k_val = str(i["key"]), "1" + str(i.get("value", 0)) if hasattr(i, 'get') else ""

                            self.data.setdefault(k_key, {}).update({k_var: v for k_var in data_raw.keys()})

                        return True
                        
                     except json.JSONDecodeError as e:
                        pass
                        
        except FileNotFoundError:
            print(f"Warning: File not found. Continuing with default loaded dict.")


    def save(self):
        if not self.data or "data_name" not in self.data:
            # Save nothing if no data to preserve
            return
            
        filepath_base = PurePosixPath("src") / "test/"

        try:
            path_save = f"{filepath_base}{self.data['data_name']}"  # .aliens.db for existing file
            with open(path_save, 'w', encoding='utf-8') as f_file:
                json.dump(self.data["data"], f_file)


def run_aliens():
    db = AlienDatabase()

    # Load test data into the structure if present
    
run_aliens()
