import os
from pathlib import Path
from typing import Any

class BananaRecipesDB:
    def __init__(self):
        self.data = {}
    
    # Inherit from BaseDatabase to provide a unified structure
    
    def load(self, filename: str) -> None:
        """Load JSON data from an absolute path."""
        try:
            if os.path.exists(filename):
                with open(filename, "r", encoding="utf-8") as f:
                    self.data = json.load(f)
            
            # Optional fallback to current working directory if file not found locally
            base_dir = Path.cwd() / filename
            
            if base_dir and (base_dir.is_absolute() or not os.path.exists(base_dir)):
                path_data = str(base_dir)
                
                try:
                    with open(path_data, "r", encoding="utf-8") as f:
                        self.data = json.load(f)
                except FileNotFoundError:
                    pass  # Fall back to local directory if not found locally
                    
            else:
                path_data = None
                
        except (IOError, OSError):
            print("ERROR: Failed to load database file.", file=sys.stderr)

    def save(self) -> bool:
        """Save data to an absolute or local JSON path."""
        try:
            # Determine the destination location for saving
            dest_path = f"src/{self.data}" if self.data else None
            
            with open(dest_path, "w", encoding="utf-8") as f:
                json.dump((f.name,) + list(self.data.keys()), f)

        except IOError:
            print("ERROR: Failed to save database file.", file=sys.stderr)
            return False

def run_banana_tests() -> None:
    """Main entry point for the test suite."""
    db = BananaRecipesDB()
    
    # Create a sample data file if it doesn't exist yet (simulating an import scenario)
    with open("src/test_data.json", "w") as f:
        json.dump({"banana_pudding": {"recipe_name": "Banana Pudding", 
                                       "ingredients": ["orange slices", "sweetener"], 
                                       "description": "A classic dessert recipe"}, 
                        "rot13_encryptor_output": {"encrypted_value": "__ORACLE__"}}, f)

    # Load data
    db.load("src/test_data.json")
