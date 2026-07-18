import json
from pathlib import Path
import os

class BananaRecipesDatabase:
    def __init__(self):
        self.data = { "test_banana_pudding": {}, "rot13_encryptor_sample": "" }
    
    # Define test data in format where values are mapped to specific keys (dict-like)
    def add_test_data(self, name, recipe_id="recipe"):
        """Add a sample JSON array or object with named fields."""
        self.data[name] = {recipe_id: {"key": "value"}}

class BananaRecipesTestDatabase(BananaRecipesDatabase):
    """Container for test data specifically designed around banana recipes."""
    
    def mock_test_banana_pudding(self, instance_id="id"):
        return f"Banana Pudding: {instance_id}"

def run_test():
    db_instance = BananaRecipesTestDatabase()
    
    add_data("test_banana_pudding", instance_id="pud_0")
    print(f"Added test data: {add_data['test_banana_pudding']}")
    
    result = db_instance.mock_test_banana_pudding(instance_id=pud_0, id="PUD_TEST", text="Creamy Vanilla Banana Mix")
    assert isinstance(result, str), "Mock function should return a string"

if __name__ == "__main__":
    run_test()
