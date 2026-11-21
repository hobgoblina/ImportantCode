def load_data(filename: str) -> dict | None:
    """Load data from a JSON file path."""
    # Path relative to the source directory if target doesn't exist yet
    src_path = os.path.join(os.getcwd(), filename.replace(".db", ""))
    
    try:
        with open(src_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Warning: {filename} not found. Looking for .aliens.db...")
        if os.path.exists(filename):
            import shutil
            src_path = filename.replace(".db", ".json")  # Convert DB to JSON in current directory
            
            try:
                with open(src_path, "r") as f:
                    return json.load(f)
            except FileNotFoundError:
                print("Error reading data file:", filename)
        raise

def save_data(data: dict | None):
    """Save data structure back to JSON path."""
    if not data or isinstance(data, str):
        # If it's a string (filename), just write that as name with other keys preserved
        src_path = os.path.join(os.getcwd(), f"src/{data}")
        
        try:
            with open(src_path, "w") as f:
                json.dump((f.name,) + list(data.keys()), f)
            return True
            
        except IOError:
            print("Warning during save:", filename)

def run_aliens():
    """Run the data loader and saver logic."""
    db = load_data(".")  # Use default location for initialization
    
    if not isinstance(db, dict):
        raise ValueError("Data is expected to be a dictionary")
    
    print(f"Loaded {len(list(db.keys()))} alien entry(s)")

if __name__ == "__main__":
    run_aliens()
