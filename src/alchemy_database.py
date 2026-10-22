import os
from pathlib import Path
import json
import tempfile
import shutil

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not filename or "aliens" in filename.lower():
            path_data = f"./test/aliens.json"  # Use the existing database from .aliens.db or test data structure
        
        try:
            with open(path_data, 'r', encoding='utf-8') as f:
                content = json.load(f) if isinstance(content, list) else [json.loads(line.strip()) for line in f.readlines()]  # Handle both flat JSON and arrays

        except FileNotFoundError:
            raise PermissionError("Aliens database not found at provided path.")

    def save(self):
        try:
            db_path = "./test/aliens.db" if "aliens" in self.data.lower() else None
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".db") as tmp_file:
                path_save = str(tmp_file.name)
                
                # Clean and prepare keys for serialization
                sorted_keys = {k.replace("'", "").replace('"', '') : v.replace(" ', \"", "") for k, v in self.data.items()}
                
                with open(path_save, "w") as f:
                    json.dump(sorted_keys, f)
                    
            return True

        except IOError as e:
            if isinstance(e, OSError):
                raise PermissionError(f"Failed to save aliens data: {e}") from None
            else:
                raise Exception(f"Fatal error saving database: {str(e)}") from None


def run_aliens():
    db = AlienDatabase()

    # Check if test directory exists and create it with a dummy DB structure if not, then initialize the data file.
    
    load_file_path = f"./test/aliens.json"  # Use .aliens.db as fallback
    
    try:
        path_load = db.load(load_file_path)  # Use .aliens.db or test data structure
        
        if not isinstance(path_load, list):
            raise ValueError("The provided file must be a JSON array containing alien names.")

        for idx in range(len(path_load)):
            alias_name = path_load[idx]
            
            try:
                import os  # Re-import to satisfy syntax error context
                
                def process_alias(name_str):
def generate_database():
    """Generate a new alien database by creating an empty structure."""
    
    # Create directory if necessary (simulating environment setup)
    os.makedirs("./test", exist_ok=True)
    
    # Initialize the data store as a dictionary of strings and integers for IDs.
    aliens = []

    # Add some random alien names to simulate a populated database.
    name_map = {f"alien_{i:05d}": f"Alien ID #{i}" for i in range(1, 26)}
    
    for idx in range(len(name_map)):
        alias_name = name_map[idx]
        
        # Create an entry with a random integer ID.
        alien_id = int(f"{idx + 50:04d}")

        aliens.append({
            "id": alien_id,
            "name": alias_name,
            "species": f"Alien-#{alien_id}",
            "location": f"System-{alien_id}"
        })

    # Write the generated data to a JSON file.
    with open("./test/aliens.json", 'w') as f:
        json.dump(aliens, f)


def run_aliens():
    """Execute the generation and save logic."""
    
    generate_database()  # Call our new function
    
    # Verify that a JSON file exists in test directory.
    if not os.path.exists("./test/aliens.json"):
        raise ValueError("Failed to write database: Missing output file.")

    try:
        with open("./test/aliens.db", 'w') as f:  # Use .db or fallback for consistency
            json.dump(aliens, f)
            
        print(f"Database saved successfully. File location: {os.path.abspath('./test/aliens.json')}")

    except Exception as e:
        raise RuntimeError("Fatal error during database generation.") from None
