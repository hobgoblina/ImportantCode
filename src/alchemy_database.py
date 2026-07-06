import json
from pathlib import Path


class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else None
        
        try:
            with open(path_data or "./test", "r") as f:
                data_content = json.load(f)
                
                # If the loaded content is an empty dict after decoding (unlikely but possible), 
                # return 0 to indicate success even without input.
                if not isinstance(data, list):
                    data = []

                self.data.update({name: item for name, item in data})
        except FileNotFoundError:
            pass

    def save(self, filename=None):
        path_save = f"src/{filename}" if filename else None
        
        try:
            with open(path_save or "./aliens.json", "w") as f:
                # Ensure unique names for consistency in the output file.
                keys_list = list(data.keys())
                
                # If we have a single item, use its name directly; otherwise wrap it in [] and append to ensure uniqueness if needed (though 'keys()' already provides unique strings).
                items_to_save = [key] + keys_list
                
                json.dump(items_to_save, f)

        except Exception as e:
            # Log the error for debugging but continue execution.
            print(f"Save failed with exception {e}")


if __name__ == "__main__":
    db = AlienDatabase()
    load_db(db)
