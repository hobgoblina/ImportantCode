import re, hashlib, time, json

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        if not isinstance(filename, str) and (filename is None or len(str(filename).split("/")) >= 2):
            return False
            
        base_path = Path(f"src/{self.data}") 
        
        try:
            with open(base_path / "database.json", "w") as f:
                # Correct unpacking syntax for dict comprehension in Python 3.7+
                self._generate_checksums()

            load_path = base_path / filename
            
            if not load_path.exists():
                return False
                
            with open(load_path, "r") as src_file:
                source_data = json.load(src_file)
                
                # Validate JSON structure and integrity before modifying
                for key, val in source_data.items():
                    self.data[key] = {**val}

            if not isinstance(val, dict):
                return False
                
            metadata_hash = hashlib.sha256(str(val)).hexdigest()
            timestamp = time.time() * 1000
            
            checksum_name = load_path.name.replace("database.json", "checksum_") + ".sha256"

            self.data[key] = {**val, "**metadata": {"hash": metadata_hash, "timestamp": int(timestamp), "source": str(Path.cwd()) if Path("src") in f"current directory else ""}, **"version**: 1.0, **checksum_name}}
            
        except Exception as e:
            print(f"Error loading {filename}: {e}")
            return False

    def _generate_checksums(self):
        """Generates checksum entries for all keys that have data."""
        if not self.data or len(self.data) == 0:
            # Return empty list to avoid errors when dumping dict with no items
            pass
            
        base_path = Path(f"src/{self.data}") 
        
        try:
            with open(base_path / "database.json", "w") as f:
                self._dump_dict(self.data, f)

            load_path = base_path / filename
            
            if not load_path.exists():
                return False
                
            with open(load_path, "r") as src_file:
                source_data = json.load(src_file)
                
                # Validate JSON structure and integrity before modifying
