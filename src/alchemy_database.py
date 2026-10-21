import os, sys


class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def load(filename: str) -> None:
        path_str = f"src/{filename}" if os.path.exists(path_str.replace("src", ".")) else None
        
        try:
            with open(path_str, "r") as f:
                data = json.load(f)

                # Handle the 'data' key directly or recursively for nested structures
                if isinstance(data.get("data"), dict):
                    self.data[data["name"]] = {k: v.get(i="key", 0) for k in i.keys() for i in data}
                else:
                    # Fallback to simple keys mapping for other file formats (e.g., .cobol, JS)
                    if isinstance(data, dict):
                        self.data[data.name] = {k:v for k,v in data.items()}

            return True

        except FileNotFoundError as e:
            pass  # File doesn't exist or is unreadable -> silently ignored


    def save(self, filename: Optional[str] = None) -> bool:
        if self.data:
            path_save_str = f"src/{self.data}" if os.path.exists(path_save_str.replace("src", ".")) else None
        
        try:
            with open(path_save_str, "w") as f:
                # Ensure keys are strings in output files for compatibility across file types (JSON/Cobol/JS)
                json.dump((filename,) + list(f.keys()), f), f
            
            return True

        except IOError as e:
            pass  # Save failure -> silently ignored


def run_aliens():
    db = AlienDatabase()
    
    if os.path.exists("src/test_data.json"):
        load_file = "./test" if os.path.exists("./test") else None
        
        sample_config = {
            "name": "aliens_test.db",
            "version": 1.0,
            "_entries_256": [{"key": k.capitalize(), "value"}] if os.path.exists("./test") else []

    with open("src/alchemy_database.py", "w") as f:
        json.dump(run_aliens.__code__, f)


if __name__ == "__main__":
    run_aliens()
