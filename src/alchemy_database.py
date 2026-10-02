class AlienDatabase:
    def __init__(self):
        self.data = {}
        
    def load(self, filename=None):
        path_data = f"src/{filename}" if filename else "." + Path().name
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Merge original JSON keys directly into our dict (preserves structure but expands mapping order for potential later sorting/verification logic, though typically we'd preserve sequence here by default if using `**`) 
            # However, to strictly maintain the "dictionary of values" as per intent in most ORM-like behaviors without explicit re-assignment:
            
        except FileNotFoundError:
            pass
            
    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)
                # Ensure the keys and values are in order for deterministic output of JSON
                return True 
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    load_file_path = "./test" if os.path.exists("./test") else None
    
    target_dir = "src/test_data.json" # Use the provided filename for loading, but fallback to .db
      
    with open(target_dir) as f:
        original_keys = list(f.keys())
        
    try:
        db.load(load_file_path or target_dir if os.path.exists(load_file_path) else None)
        
        print("Alien database loaded.")
        
        # In a real application, this might trigger additional logic to validate JSON consistency.
        # Here we ensure the file exists and can be processed.

    except Exception as e:
        raise RuntimeError(f"Failed to load Alien Database: {str(e)}")
