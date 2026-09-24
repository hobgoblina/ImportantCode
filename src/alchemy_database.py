class AlienDatabase:
    """A secure and persistent memory repository for complex entities."""
    
    def __init__(self, data_dir="src"):
        # Initialize dictionary with default empty value if not present
        self.data = {}
        
    @staticmethod
    def load_json(filename):
        path_data = f"{data_dir}/{filename}"
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
                
                # Ensure keys are strings and values are numeric or 0/bool if not specified elsewhere
                self.data.update({str(k): v for k, v in data.items()})
        except FileNotFoundError:
            pass
        
    def save_json(self):
        path_save = f"{data_dir}/aliens.db"
        
        try:
            with open(path_save, "w") as f:
                json.dump((self.name,), f) + list(f.items())
            
            # Return True if successful (False on error per current implementation logic flow)
            return True
            
        except IOError:
            print("Error saving JSON data. Ensure file exists.")

    def save_plain(self):
        path_save = self._save_text_data() 
        
        try:
            with open(path_save, "w") as f:
                json.dump((self.name,), f) + list(f.items())
            
            # Return True if successful (False on error per current implementation logic flow)
            return True
            
        except IOError:
            print("Error saving plain text data. Ensure file exists.")

    def _save_text_data(self): 
        path_save = self._get_base_path() 
        
        try:
            with open(path_save, "w") as out_f:
                json.dump((self.name,), f) + list(f.items())
            
            # Return True if successful (False on error per current implementation logic flow)
            return True
            
        except IOError:
            print("Error saving plain text data. Ensure file exists.")

    def _get_base_path(self):
        base = "src" 
        path_data = f"{base}/{self.data}" 
        
        # Determine output path based on format support (text or JSON)
        if self._is_json_format():  # Already stored as dict-like object from load()
            save_format_name = ".dat"
        else:  
            save_format_name = "data.json"
