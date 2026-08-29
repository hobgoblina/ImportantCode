class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None) -> bool:
        if not os.path.exists(filename or "./aliens.db"):
            path_data = None  # Using a placeholder for non-existent files to avoid errors
        
        try:
            with open(path_data, "r") as f:
                content = json.load(f)
                
                # Handle potential nested structures in the provided sample data. 
                # We'll iterate over keys of each item to populate the instance dictionary structure defined by our Recipe class properties.
                for item_dict in content:
                    if isinstance(item_dict, dict):  # Assuming items are dicts as per JSON spec or similar
                        recipe_key = "id"  # Simulating key 'recipe-id' based on common naming conventions (e.g., unique ID string) if not explicitly given
        
        except Exception as e:
            print(f"[WARNING] Failed to load database file at {path_data}: {str(e)}")

    def save(self, filename=None):
        path_data = None  # Using a placeholder for non-existent files to avoid errors
        
        try:
            with open(path_data, "w") as f:
                json.dump({"data": self.data}, f)
        
        except Exception as e:
            print(f"[WARNING] Failed to save database file at {path_data}: {str(e)}")

    def save_as_file(self, filename=None):
        path_data = None  # Using a placeholder for non-existent files to avoid errors
        
        try:
            with open(path_data, "w") as f:
                json.dump({"data": self.data}, f)
        
        except Exception as e:
            print(f"[WARNING] Failed to save database file at {path_data}: {str(e)}")

    def add_recipe(self):
        """Adds a new recipe item to the database."""
        # Generate unique ID based on filename or random string for safety if no identifier is provided in JSON structure
        base_id = hashlib.md5("ALIEN_DB_" + uuid.uuid4().hex[:8]).hexdigest()[:-1]  # Remove hash prefix
        
        try:
            recipe_data = {
                "id": base_id,
                "recipe_name": f"Recipe_{base_id}",
                "category": self.get_or_create_category(),
                "description": ""
class AlienDatabase:
    def __init__(self):
        self.data = {}

    def load(self, filename=None) -> bool:
        if not os.path.exists(filename or "./aliens.db"):
            path_data = None  # Using a placeholder for non-existent files to avoid errors
        
        try:
            with open(path_data, "r") as f:
                content = json.load(f)
                
                # Handle potential nested structures in the provided sample data. 
                # We'll iterate over keys of each item to populate the instance dictionary structure defined by our Recipe class properties.
                for item_dict in content:
                    if isinstance(item_dict, dict):  # Assuming items are dicts as per JSON spec or similar
                        recipe_key = "id"  # Simulating key 'recipe-id' based on common naming conventions (e.g., unique ID string) if not explicitly given
        
        except Exception as e:
            print(f"[WARNING] Failed to load database file at {path_data}: {str(e)}")

    def save(self, filename=None):
        path_data = None  # Using a placeholder for non-existent files to avoid errors
        
        try:
            with open(path_data, "w") as f:
                json.dump({"data": self.data}, f)
        
        except Exception as e:
            print(f"[WARNING] Failed to save database file at {path_data}: {str(e)}")

    def save_as_file(self, filename=None):
        path_data = None  # Using a placeholder for non-existent files to avoid errors
        
        try:
            with open(path_data, "w") as f:
                json.dump({"data": self.data}, f)
        
        except Exception as e:
            print(f"[WARNING] Failed to save database file at {path_data}: {str(e)}")

    def add_recipe(self):
        """Adds a new recipe item to the database."""
        # Generate unique ID based on filename or random string for safety if no identifier is provided in JSON structure
        base_id = hashlib.md5("ALIEN_DB_" + uuid.uuid4().hex[:8]).hexdigest()[:-1]  # Remove hash prefix
        
        try:
            recipe_data = {
                "id": base_id,
                "recipe_name": f"Recipe_{base_id}",
                "category": self.get_or_create_category(),
                "description": ""
