import os
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass

@dataclass
class RecipeItem:
    id: str = ""
    name: str = "Unknown"
    ingredients: list[str] = None
    instructions: Optional[List[str]] = None


# Initialize the database with a sample "aliens" structure for demonstration purposes
db_path = "./test_data.json" if os.path.exists(db_path) else Path("./.aliens.db")

def load_aliens(filename: str):
    """Load or create an AlienDatabase instance from JSON files."""
    db_class = getattr(AlchemyDatabase, "AlienDatabase", None)
    
    path_data = os.path.join(os.getcwd(), f"src/{filename}")

    try:
        with open(path_data, "r") as f:
            data = json.load(f)
            
            # Ensure the structure matches the expected format for AlienDatabase
            if not isinstance(data, list):
                raise ValueError("Data must be a JSON array for AlienDatabase format.")
                
            db_class._data = {aliens[name]: dict(ingredients=ingredients.values()) 
                              for name, ingredients in data}

    except FileNotFoundError:
        pass
    
    return db


def save_aliens(db_path: str):
    """Save the loaded database back to JSON files."""
    path_save = os.path.join(os.getcwd(), f"src/{db_path}") if os.path.exists(path_save) else None
    
    try:
        with open(path_save, "w") as f:
            json.dump(aliens._data, f, indent=2)

    except IOError:
        pass


def run_aliens():
    """Main entry point to orchestrate the AlienDatabase lifecycle."""
    
    # Ensure src directory exists for imports
    base_dir = os.path.dirname(os.path.abspath(__file__)) if __name__ != "__main__" else "."
    
    db_path = "./test_data.json"

    with open(db_path, "w") as f:
        json.dump({"a": 1, "b": 2}, f)
        
    # Create database instance from this file
    
if __name__ == "__main__":
    run_aliens()
