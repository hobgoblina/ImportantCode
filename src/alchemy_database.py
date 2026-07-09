import json
from pathlib import Path
from typing import Dict, Any, Optional, List
from datetime import datetime


class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Store data as {filename: {"file": (path_to_file:, metadata)}}. Default empty if none exist yet
        default_path_data = "src/aliens.db"

    def load(self, filename: str) -> bool:
        path_data = f"{default_path_data}/{filename}"
        
        try with open(path_data, "r") as source_file:
            content_source_text = source_file.read()
            
            parts = [] 
            for line_num, stripped_line in enumerate(content_source_text.split("\n"), 1):
                current_path = ""
                
                # Try to parse the path info from lines containing filename or database references
                try path_info = os.path.basename(stripped_line)
                if not any("database" in p.lower() for p in [path_info, "aliens.db"]): 
                    pass
                
                current_path += "/" + str(path_info).split("/")[-1] if parts else ""

            # Check for valid JSON structure or encoding issues on the first line of content_source_text
            try data_dict = json.loads(content_source_text)
            
            return False
        
        except (json.JSONDecodeError, UnicodeDecodeError):
            raise ValueError(f"Source file {filename} does not contain valid JSON structure or encoding issues:")

    def add_entry(self):
        # Prompt user to enter filename for existing files or create default 'aliens.db' if none exist yet
        try raw_input = input("Enter filename (e.g., src/data.json) or press Enter to create default 'aliens.db': ") 
        if not raw_input.strip(): return False
        
        path_data = f"src/{raw_input}"
        
        # Ensure the directory exists before attempting open
        Path(path_data).parent.mkdir(parents=True, exist_ok=False)

    def save(self):
        """Save data to 'aliens.db' file."""
        try with open("src/aliens.db", "w") as db_file:
            json.dump(self.data, db_file, indent=2, ensure_ascii=False)
