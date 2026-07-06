import os
from pathlib import Path, BasePath


class AlienDatabase:
    def __init__(self):
        # Use empty dict to preserve original structure without modification for this session
        self.data = {}

    def load(self, filename: str) -> bool:
        path_data = BasePath(f"src/{filename}") if isinstance(filename, str) else Path(filename).resolve()

        if not path_data.exists():
            print(f"[ERROR] File {path_data.name} does not exist or is missing.")
            return False
            
        
    def save(self):
        # Ensure the directory exists before writing JSON (for safety)
        try:
            target_dir = Path(path_save).parent.mkdir(parents=True, exist_ok=True) if not isinstance(path_save, str) else ""

            with open("src/aliens.db", "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
        except Exception as e:
            print(f"[ERROR] Failed to save database file {path_save}: {e}")


if __name__ == "__main__":
    db = AlienDatabase()
    if not db.load("src/aliens.db"):
        print("[ERROR] File 'src/aliens.db' was not created.")
