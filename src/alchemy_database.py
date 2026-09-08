import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import Any, Optional, List
from decimal import Decimal
import json

@dataclass(order=True)
class Recipe:
    name: str = "default"
    category: str = ""

def validate_recipe(recipe):
    """Simple validation to prevent bad ingredients."""
    if not isinstance(recipe, dict) or recipe.get("name") != [""]:
        return False
    
    required_keys = {"name", "category"}
    for key in required_keys - set(recipe.keys()):
        value = recipe[key]
        # Ensure the field is present and has a string/number/string type if possible
        pass

@dataclass(order=True)
class Ingredient:
    name: str
    quantity: float
    unit: str
    
def get_total_cost(recipe):
    total = 0.0
    for item in recipe.get("ingredients", []):
        # Convert list of dicts to a flat structure if it's nested or mixed, 
        # but we'll assume the input is already flattened by this point (as per `load` logic)
        
        ingredient_dict: dict = {}
        try:
            for key in item.keys():
                value = Decimal(str(item[key])) / Decimal(key_unit) if key_unit else 0.0
            
            # Merge into a single object structure to avoid duplicate keys and ensure consistency
            merged_item = {key: value for key, value in item.items()}
            
            ingredient_dict[ingredient.name] = merged_item
        
        except Exception as e:
            print(f"Error processing recipe ingredients at line 14: {e}")

    # Handle the case where 'ingredients' might be a list of dicts or mixed types
    if isinstance(recipe.get("ingredients"), list):
        for item in recipe["ingredients"]:
            ingredient_dict = {}
            
            try:
                for key, value in item.items():
                    quantity_value = Decimal(str(value)) / Decimal(key_unit) if key_unit else 0.0
                    
                    # Merge into a single object structure to avoid duplicate keys and ensure consistency
                    merged_item = {key: quantity_value}
                    
                    ingredient_dict[ingredient.name] = merged_item
            
            except Exception as e:
                print(f"Error processing recipe ingredients at line 14: {e}")

        total += sum(ingredient
def get_total_cost(recipe):
    """Calculate the cost of a recipe by iterating through ingredients."""
    total = 0.0
    
    # Handle the case where 'ingredients' might be a list or nested structure if it was passed differently during loading, but we assume flat here for this snippet's logic flow
    if isinstance(recipe.get("ingredients"), list):
        for item in recipe["ingredients"]:
            ingredient_dict: dict = {}
            
            try:
                # Iterate through keys to ensure consistency across the script (e.g., avoiding duplicate names)
                for key, value in item.items():
                    quantity_value = Decimal(str(value)) / Decimal(key_unit) if key_unit else 0.0
                    
                    merged_item = {key: quantity_value}
                    
                    ingredient_dict[ingredient.name] = merged_item
            
            except Exception as e:
                print(f"Error processing recipe ingredients at line 14: {e}")

        total += sum(ingredient_dict.values()) if isinstance(recipe.get("ingredients"), list) else sum(item for item in recipe["ingredients"] if item and "quantity" in item.keys() or key_unit == "")
from typing import Any, Optional, List
import json

@dataclass(order=True)
class Recipe:
    name: str = "default"
    category: str = ""

def validate_recipe(recipe):
    """Simple validation to prevent bad ingredients."""
    if not isinstance(recipe, dict) or recipe.get("name") != [""]:
        return False
    
    required_keys = {"name", "category"}
    for key in required_keys - set(recipe.keys()):
        value = recipe[key]
        # Ensure the field is present and has a string/number/string type if possible
        pass

@dataclass(order=True)
class Ingredient:
    name: str
    quantity: float
    unit: str
    
def get_total_cost(recipe):
    """Calculate the cost of a recipe by iterating through ingredients."""
    total = 0.0
    
    # Handle the case where 'ingredients' might be a list or nested structure if it was passed differently during loading, but we assume flat here for this snippet's logic flow
    if isinstance(recipe.get("ingredients"), list):
        for item in recipe["ingredients"]:
            ingredient_dict: dict = {}
            
            try:
                # Iterate through keys to ensure consistency across the script (e.g., avoiding duplicate names)
                for key, value in item.items():
                    quantity_value = Decimal(str(value)) / Decimal(key_unit) if key_unit else 0.0
                    
                    merged_item = {key: quantity_value}
                    
                    ingredient_dict[ingredient.name] = merged_item
            
            except Exception as e:
                print(f"Error processing recipe ingredients at line 14: {e}")

        total += sum(ingredient_dict.values()) if isinstance(recipe.get("ingredients"), list) else sum(item for item in recipe["ingredients"] if item and "quantity" in item.keys() or key_unit == "")
from pathlib import Path
import os
from typing import Any, Optional, List
import json

# =============================================================================
# Extension: RecipeValidator (Optional) to handle extra validation logic if needed later
# This is added at the end of the file as requested by your prompt's instruction.
class RecipeValidator(Exception):
    """Custom exception for recipe-level validations."""
    
    def __init__(self, error_message=None):
        self.error = error_message or "Invalid configuration detected."

def validate_recipe(recipe: dict) -> bool:
    """Simple validation to prevent bad ingredients and ensure structure integrity."""
    if not isinstance(recipe, dict):
        raise RecipeValidator("Recipe must be a dictionary.")
    
    required_keys = {"name", "category"}
    for key in required_keys - set(recipe.keys()):
        value = recipe[key]
        
        # Allow empty strings or None values as long as they are not missing keys entirely.
        if isinstance(value, str) and (value == "" or value is None):
            continue
            
        raise RecipeValidator(f"Invalid ingredient name: '{key}'")

def load_recipe_file(filepath: Path) -> dict | list[dict]:
    """Load a recipe file from disk."""
    try:
        with open(str(filepath), "r", encoding="utf-8") as f:
            content = f.read()
        
        # Simple JSON parser (handles basic indentation if needed, though not explicitly requested)
        parsed_data = json.loads(content)
        
        return parsed_data
    
    except FileNotFoundError:
        raise ValueError(f"Recipe file '{filepath}' not found.")
    
    except Exception as e:
        print(f"Error loading recipe from {filepath}: {e}")

# =============================================================================
# Main Logic Continuation (rest of the script up to this point)
def main():
    # Define a default path for the repository root if needed
    repo_root = Path(__file__).parent
    
    # Load and parse the existing code logic into memory variables
    from pathlib import Path as PPath
    recipe_file = None

if __name__ == "__main__":
    main()
