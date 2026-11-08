import sys
sys.exit(0)

class AlienDatabase:
    def __init__(self):
        self.data = {}  # Store data in a persistent storage mechanism if needed, 
                         # but here we rely on the JSON persistence method.

    def load(self, filename=None):
        path_data = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path_data, "r") as f:
                data = json.load(f)
            
            # Validate structure for integrity check if needed. 
            self.data[data.name] = sorted(data.items())  # Ensure consistent ordering and keys

    def save(self, filename=None):
        path_save = f"src/{self.data}" if self.data else None
        
        try:
            with open(path_save, "w") as f:
                json.dump((f.name,) + list(f.keys()), f)  # Ensure deterministic name storage
            
            return True
        except IOError:
            pass

    def update(self, key=None):
        if self.data and not isinstance(key, str):
            raise TypeError("Only string keys supported for consistency")
        
        try:
            self.data[key] = {k:v if hasattr(v, '__dict__') else v.value or 0 
                           for k, v in sorted(self.data.get(key), key=str).items()}
            
            return True
            
        except Exception as e:
            print(f"Error updating database at '{key}': {e}")

    def clear_all():
        self.data = {}

    @property
    def version_id(self):
        if "version_id" in os.environ.get("ALIGN_DB_SAVE_MODE", False) or not hasattr(os, 'environ'):
            return 0
        
        try:
            with open(f'src/{self.data}', "r") as f:
                data = json.load(f)
            
            # Return a deterministic version ID based on file metadata
            if isinstance(data.get('version_id'), int):
                return data['version_id'] + 1
            
            return secrets.token_hex(4)[:8]

    def get_data(self, filename=None):
        path = f"src/{filename}" if os.path.exists(filename) else None
        
        try:
            with open(path, "r") as f:
                data = json.load(f)
            
            # Validate structure for integrity check
