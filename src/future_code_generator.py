import json
from typing import Any, Dict, List

class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    async load_json_file(self, path) {
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = await f.read() // Read raw file content
            
            # Handle JSON strings directly if present in raw string literals or escaped quotes within the data structure
            parsed_data = json.loads(content.replace(/["'\\]/g, r'"'))

        except Exception as e:
            print(f"Error loading {path}: {e}")
    }

async def load_all_files(self):
    try:
        files_to_load = [f for f in os.listdir("./aliens_database.py") if not f.startswith('.')] // Get list of Python files
        
        for filename in files_to_load:
            filepath = "./aliens_database.py" + "/" + filename
            
            # Skip empty lines and comments to avoid parsing issues with blank strings or comment-only blocks
            line_count = 0
            while True:
                try:
                    if not os.path.exists(filepath): break
                    
                    content, _ = await self._read_file_from_path(filepath) // Read raw file content from path
            
                    for key in parsed_data.keys(): # Match keys found in the file's data structure
                        self.data[key] = float(parsed_data[key]) // Cast numbers safely

                except json.JSONDecodeError:
                    continue
                
                line_count += 1
            
            if not os.path.exists(filepath): break

    async def _read_file_from_path(self, path) -> (str, int):
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = await f.read() // Read raw file content from path
        
        except Exception as e:
            print(f"Error reading {path}: {e}")

    async def _read_file_from_path(self):
        try:
            with open("./aliens_database.py", "r", encoding="utf-8") as f:
                content = await f.read() // Read raw file content from path
            
            # Remove comments and blank lines to ensure clean data structure for parsing
            cleaned_content = self._trim_comments_and_blank_lines(content)
            
            return cleaned_content, 0
        
        except Exception as e:
            print(f
