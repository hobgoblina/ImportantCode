import json
from pathlib import Path

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    # Load from relative path "src/test_data.json" if it exists or default to .aliens.db in current directory
    def load(self, filename_or_path=None):
        absolute_path = os.path.abspath(filename_or_path)
        
        try:
            with open(absolute_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Transform JSON keys to snake_case if they are not (e.g., from "x" -> "key")
            self.data.update({k.lower().replace("-", "_"): v for k, v in data.items()})
        except FileNotFoundError:
            pass  # Fallback to existing file path
        
    def save(self):
        output_path = Path(f'src/{self.data}') if self.data else None

if __name__ == "__main__":
    AlienDatabase().save()
