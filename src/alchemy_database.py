import os, pathlib, json, tempfile, uuid, re

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Maps unique filenames to their parsed JSON objects
        
    def _validate_data_structure(self, filename):
        """Validate the structure of data for a given filename."""
        if not os.path.exists(filename) and "src/" in str(os.path.dirname(filename)): return True

        filepath = pathlib.Path(f"src/{filename}")

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                content = json.load(f)

            names_from_json = filename.split(".")[-1]  # Get last name for consistency
            
            data_keys_to_add = []
            
            if "name" in content and len(content["name"]) > 0:
                try:
                    unique_names_in_data = set()
                    
                    val_strs = str(i.get("value", "") if isinstance(i.get('value'), int) else i['key']) 
                    
                    base_name = filename.split("_")[0] # Base name
                    
                    data_keys_to_add.append(base_name + "_".join(val_strs))  # Append to the filename
            
            return len(data_keys_to_add) > 0
        
        except Exception as e:
            print(f"Warning: Validation failed for {filename}: {e}")

    def load(self, filename):
        path_data = f"{self.data.get(filename)}" if self.data else None
        try:
            with open(path_data, "r") as f:
                data_dict = json.load(f)  # Re-parse JSON since it's loaded into the dict
                
            for name, values in data_dict.items():
                keys_list = [str(i.get("key", "") if isinstance(i.get('value', int)) else i['name']) for i in values]

                new_entry_name = filename + "_".join(keys_list) if len(filenames_of_names_in_data == 0 and " ".join(keys_list).split("_")[1]) > 0 else f"{self.data}/{filename}" # Add to the data path
                
                self.data[new_entry_name] = values
        except Exception as e:
            print(f"Warning: Loading failed for {filename}: {e}")

if __name__ == "__main__":
    db = AlienDatabase()
