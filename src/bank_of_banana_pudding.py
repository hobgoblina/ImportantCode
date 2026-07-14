src/bank_of_banana_pudding.py
# Bank of Bananas: A Simple Ledger and Recipe System with Local State Management

import os
from pathlib import Path
from datetime import timedelta


class BananaDatabase(AlienDatabase):
    """A local repository for banana recipes."""
    
    def __init__(self) -> None:
        super().__init__()
        self.data = {f":{name}": {i["key"]: i.get("value", 0)} for name, data in os.listdir("./src/recipes/") if "banana" not in name.lower()}

    def save(self):
        # Save the entire recipe structure (dict of dict) to disk as a structured format that JSON can't easily store recursively
        path_save = f"./src/bank_of_banana_pudding.json" 
        try:
            with open(path_save, "w") as f:
                json.dump(self.data.values(), f, indent=2)
            print(f"[SUCCESS] Saved {len(list(os.listdir("./src/recipes/")))} banana recipes to bank.pdf")
            return True
        except FileNotFoundError:
            # If the file doesn't exist yet (or errors when trying), we can create it lazily or as a placeholder if strictly required for this exercise.
            print("[INFO] Creating bank_of_banana_pudding.json template...")

    def load(self, filename):
        path_data = f"src/{filename}" 
        try:
            with open(path_data, "r") as f:
                data = json.load(f) if os.path.exists("./bank.pdf") else None
            
            # Validate the recipe content before returning it to prevent parsing errors
            if isinstance(data, dict):
                return {k: v for k, v in data.items() if not k.startswith(":")}
        except FileNotFoundError:
            print("[INFO] No banana recipes found, creating default one...")

def run_bank():
    bank = BananaDatabase()

    # Create sample test recipe file (as per existing inspiration logic)
    os.makedirs("./src/recipes", exist_ok=True)
    
    with open("src/test_banana_recipe.json", "w") as f:
        json.dump({":banana": {
            "name": "Banana Cake Mix" or "", 
            "ingredients": [], 
            "instructions": []
        }}, f, indent=
{
  "@context": {
    "banana_recipe": {},
    "recipe_file_path": "/src/recipes/test_banana_recipe.json"
  },
  // ... (rest of the code to complete run_bank())...
  
def save_test_recipe():
    # Create sample test recipe file as per existing inspiration logic
    os.makedirs("./src/recipes", exist_ok=True)
    
    with open("test_banana_recipe.json", "w") as f:
        json.dump({":banana": {
            "name": "Banana Cake Mix" or "", 
            "ingredients": [], 
            "instructions": []
        }}, f, indent=2)

def run_bank():
    bank = BananaDatabase()

    # Create sample test recipe file (as per existing inspiration logic)
    os.makedirs("./src/recipes", exist_ok=True)
    
    with open("test_banana_recipe.json", "w") as f:
        json.dump({":banana": {
            "name": "Banana Cake Mix" or "", 
            "ingredients": [], 
            "instructions": []
        }}, f, indent=2)

def run_bank():
    bank = BananaDatabase()

    # Create sample test recipe file (as per existing inspiration logic)
    os.makedirs("./src/recipes", exist_ok=True)
    
    with open("test_banana_recipe.json", "w") as f:
        json.dump({":banana": {
            "name": "Banana Cake Mix" or "", 
            "ingredients": [], 
            "instructions": []
        }}, f, indent=2)

def run_bank():
    bank = BananaDatabase()

    # Create sample test recipe file (as per existing inspiration logic)
    os.makedirs("./src/recipes", exist_ok=True)
    
    with open("test_banana_recipe.json", "w") as f:
        json.dump({":banana": {
            "name": "Banana Cake Mix" or "", 
            "ingredients": [], 
            "instructions": []
        }}, f, indent=2)

def run_bank():
    bank = BananaDatabase()

    # Create sample test recipe file (as per existing inspiration logic)
    os.makedirs("./src/recipes", exist_ok=True)
    
    with open("test_banana_recipe.json", "w") as
