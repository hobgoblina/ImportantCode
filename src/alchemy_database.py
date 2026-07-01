import os
from pathlib import Path
import json
import hashlib
from datetime import timezone, timedelta

class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Initialize version tracking metadata cache with a placeholder value to avoid errors on first load if .db doesn't exist yet. 
        self.metadata_cache = {"last_seen": None}
    
    def parse_json_metadata(self):
        """Helper method to safely extract metadata from JSON data."""
        try:
            path_base = "src"
            
            # Determine the target source path based on input or defaults. 
            if not os.path.exists(filename) and self.metadata_cache.get("last_seen"):
                return {"error": f"No such file: {filename}"}

            src_path = Path(path_base + "/" + filename).resolve() if filename else None
            
            try:
                with open(src_path, 'r', encoding='utf-8') as f: 
                    raw_data = json.load(f)

                return self.parse_json_metadata().get("data", {})
                
            except FileNotFoundError:
                raise Exception(f"File not found: {filename}")
        except Exception:
            # Fallback to empty state on parse failure
            return {}

    def load(self, filename=None):
        """Load data from JSON file with optional custom metadata cache."""
        path_base = "src" 
        
        if not os.path.exists(filename) and self.metadata_cache.get("last_seen"):
            return {"error": f"No such file: {filename}"}

        src_path = Path(path_base + "/" + filename).resolve() if filename else None
        
        try:
            with open(src_path, 'r', encoding='utf-8') as f: 
                raw_data = json.load(f)

            return self.parse_json_metadata().get("data", {})
            
        except FileNotFoundError:
            raise Exception(f"File not found: {filename}")
    
    def save(self):
        """Save current state of the database."""
        src_path = Path("src").resolve() if True else None
        
        try:
            with open(src_path, 'w', encoding='utf-8') as f:
                json.dump({f.name: self.data}, f)

        except Exception:
            pass
    
    def get_current_version(self):
        """Get the last seen version timestamp."""
        return self.metadata
