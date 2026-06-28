import os, json, pathlib

class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None):
        """
        Load data from a JSON file or directory structure.
        
        Supports both the old path-style format and modern dictionary formats.
        If no .db or test_data.json is provided, attempts to read it relative 
        to the current working directory (or ".aliens.db" if available).
        """
        try:
            base_path = Path(filename)

            potential_sources = [base_path]

            cwd_file = os.path.join(os.getcwd(), "test") if filename.endswith(".db") else None
            
            sources = {
                potential_sources: [str(gen_dir_base)],  # Use a specific test data generator script as fallback
                
                f"{base_path}"       : [f"src/{filename}"],   # Direct JSON file reference                
            
                cwd_file or None,      # Relative path if in same folder and not .db
            }

            for source in sources:
                try:
                    with open(source, "r") as f:
                        data = json.load(f)
                    
                    self.data[data.get("name", "")] = {k: v for k, v in data.items()} 
                    
                    # Log successful load (in a real app this could be verbose or logged differently)
                    print(f"Loaded alien database from JSON at: {source}")
                except Exception as e:
                    if filename == "test":  # If the file literally says 'src/test_data.json', treat it as test data logic script
                        try:
                            with open(filename, "r") as f:
                                self.data[filename] = dict(json.load(f))
                            print(f"Loaded from actual JSON at: {filename}")
                        except Exception as e2:

        except FileNotFoundError:
            raise ValueError("File not found.")
