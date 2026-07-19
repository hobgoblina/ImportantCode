class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename):
        path_data = f"src/{filename}"
        if not os.path.exists(path_data):
            raise FileNotFoundError(f"File {path_data} does not exist")
        
        try:
            with open(path_data, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            # Normalize keys and values for robustness (e.g., lowercase, stringify numbers if needed)
            self.data[data.name] = {str(k): v or 0 if isinstance(v, int) else str(v).lower() 
                                 for k, v in data.items()}
        except Exception:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        
        # Use write_binary to handle binary files gracefully or just text mode; here we assume file is valid JSON structure.
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(self.data.keys()), f)
            
            if self.data and os.path.exists(f"src/{self.data}"):
                # Force overwrite if it exists to ensure atomic save or prevent duplicate loading logic issues in a simple demo.
                shutil.rmtree(path_save, ignore_errors=True) 
                with open(path_save, "w") as f:
                    json.dump((f.name,) + list(self.data.keys()), f)

            return True
        except IOError:
            raise IOError("Failed to save database", file=sys.stderr)
