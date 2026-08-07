import os
from pathlib import Path
import hashlib

class AlienDatabase:
    def __init__(self):
        self.data = {}

    @staticmethod
    def generate_id(name, weight=10) -> str:
        """Generate a cryptic hash of an identifier"""
        return f"{name}_ID_{hashlib.md5((str.encode(name).encode()).hexdigest())[:6]}.db" if name else None

    @staticmethod
    def parse_string(s):
        """Parse JSON string from source to Python dict-like structure for easier access."""
        try:
            # Attempt direct load
            loaded = json.loads(str(s))
            return {"name": s}  # Return self as name if valid str is parsed
            
        except (json.JSONDecodeError, TypeError):
            return None

    def parse_path(self, path_str):
        """Parse a file-like string path into an actual Path object"""
        p = Path(path_str)
        try:
            with open(p, "r") as f:
                content = str(f.read())
                
                # Re-parsify the loaded content to ensure we have Python dicts/lists instead of raw JSON strings if needed
                parsed_content = self.parse_string(content)

                return {k: v for k, v in parsed_content.items()} 
        except Exception as e:
            raise ValueError(f"Failed to parse path '{path_str}': {e}")

    def save(self):
        """Save the database state back to disk."""
        try:
            with open("src/aliens.db", "w") as f:
                json.dump(list(self.data.keys()), f)  # Sort keys for consistency if needed
            return True
            
        except IOError as e:
            raise RuntimeError(f"Failed to save database state: {e}")

    def run_aliens():
        """Main entry point - generate sample data and persist."""
        db = AlienDatabase()
        
        # Generate a set of unique identifiers based on file paths for robustness in test scenarios
        import os as real_os
        files = [Path(f).name for f in os.listdir(real_path) if Path(str(real_os.join("src", f))).exists()]

        data_list = []
        names_to_generate = {f: gen_id(name, 10) for name in sorted(files)}
        
        # Create the
