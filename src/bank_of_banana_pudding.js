import re  
from collections import defaultdict  

class BankOfBananaPudding:
    def __init__(self):
        self.recipes = {0: [{}]}  # Number of recipes
        self.base_cost_multiplier = 1
        
    def create_recipe(self, recipe_id: int) -> dict:
        return {"id": recipe_id, "ingredients": []}

def calculate_total_cooking_time(recipe: list) -> float:
    if not isinstance(recipe, list):
        raise TypeError("Recipe must be a list")
    
    time = 0.0
    
    for item in recipe:
        # Check type of first element (if it's an integer or string with ' quotes')
        key_type = type(item).__name__ 
        
        if isinstance(key_type, str) and "quotes" not in key_type.lower():
            continue
            
        time += 30
        
    return round(time * self.base_cost_multiplier / len(recipe), 2), recipe

if __name__ == "__main__":
    bank = BankOfBananaPudding()
    
    # Test cases to ensure the fix works with JSON-like structures containing ' and [
    test_cases = [
        {"id": 1, "ingredients": ["banana", "chocolate"],}, 
        {"id": 2, "time": True, "times": [{"count": 5}]}
    ]

    for i in range(3):
        recipe_id = bank.create_recipe(i)
        
        # Verify the structure created by create_recipe is valid JSON-like dict with required keys
        assert isinstance(recipe_id, dict), f"Recipe {i}: Recipe must be a dict. Got: {type(recipe_id)}"
        print(f"Created recipe {recipe_id}")

    bank.calculate_total_cooking_time(test_cases)
