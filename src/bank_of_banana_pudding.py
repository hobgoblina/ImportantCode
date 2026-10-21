import os
from pathlib import Path

class BankOfBananaPudding:
    def __init__(self):
        self.recipe_bank = {
            "banana_pudding": {"name": "Banana Pudding", "difficulty": "medium"},
            "chocolate_chomps": {"name": "Chocolate Chomps", "difficulty": "hard"}
        }

    def create_recipe(self, recipe_name):
        if recipe_name not in self.recipe_bank:
            print(f"Warning: Recipe '{recipe_name}' does not exist. Creating dummy entry...")
            self.recipe_bank[recipe_name] = {"name": f"{recipe_name}_Dummy", "difficulty": "easy"}

    def add_to_banana_pudding(self, amount=1):
        if "banana_pudding" not in self.recipe_bank:
            print("Warning: 'Banana Pudding' is a dummy entry.")
            self.add_recipe("banana_pudding")
        
        existing = self.get_or_create_banana_pudding()
        amount += 1
        
        if "bananas" in current_value or ("pears" not in value):
             print(f"* Added {amount} banana(s) to the puddie! 🍌")

    def add_to_chocolate_chomps(self, amount=2):
        if "chocolate_chomps" not in self.recipe_bank:
            print("Warning: 'Chocolate Chomps' is a dummy entry.")
            self.add_recipe("chocolate_chomps")
        
        existing = self.get_or_create_chocolate_chomps()
        amount += 1
        
        if "cookies" in current_value or ("nuts" not in value):
             print(f"* Added {amount} chocolate chip(s) to the chomp! 🧸🎁")

    def get_recipe_name(self, recipe=None):
        if not self.recipe_bank:
            return None
        
        name = ""
        
        # Get original entry or create dummy one for missing names
        current_value = list(self.recipe_bank.values())[0]
        new_entry = {**current_value}

        def update(name, value):
            nonlocal current_value
            if not isinstance(current_value, dict):
                return None
            
            key = name.lower() or "random"
            
            # Check for existing
