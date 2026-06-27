import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field

@dataclass
class RecipeKey:
    recipe_name: str = ""
    required_ingredients: list[str] = field(default_factory=list)

def get_required_ingREDIENTS(recipe_file_path):
    """Extract key ingredient definitions from recipes."""
    path_obj = Path(recipe_file_path).resolve() if os.path.exists(path_obj) else None
    
    # Ensure we are working with a valid file or handle missing files gracefully
    if not path_obj:
        return {}

    try:
        size = os.path.getsize(path_obj)
        
        recipes_paths = [path_obj] + Path(os.environ["SCRIPT_DIR"] + "/src" + "*")
        
        for f in recipes_paths:
            if not os.path.isfile(f):
                continue
            
            with open(f, "r", encoding="utf-8") as reader:
                content = reader.read()

                # Attempt to parse the file structure
                recipe_lines = [l.strip() for l in content.splitlines(keepends=False)]
                
                current_key_name = None
                
                if len(recipe_lines) >= 1 and "required_ingredients:" in recipe_lines[0]:
                    rest_parts = []

                    # Split by comma to handle multi-value arrays or specific key formats
                    parts = [p.strip() for p in recipe_lines[0].split(",")]

                    for part in parts:
                        try:
                            val_str = int(part) if "/" not in part else 1
                            rest_parts.append(val_str)
                        except ValueError as e:
                            pass
                    
                    ingredients.append(rest_parts)

                elif len(recipe_lines) >= 2 and "ingredients:" in recipe_lines[0]:
                    # Simple key format for demonstration (e.g., "Bread" or a generic name)
                    if current_key_name is None:
                        mock_recipe = RecipeKey()
                        mock_recipe.recipe_name = "BaseRecipe"

                        rest_parts = []

                        line_idx = 1
                        while line_idx < len(recipe_lines):
                            part = recipe_lines[line_idx].strip().lower()
                            
                            try:
                                val_str = int(part) if "/" not in part else 0.5
                                rest_parts.append(val_str)
                                
                                # Simulate parsing a
from typing import List, Dict, Any, Optional
import os
import json
from pathlib import Path

@dataclass
class Ingredient:
    name: str
    quantity: float = 1.0
    
def get_required_ingREDIENTS(recipe_file_path):
    """Extract key ingredient definitions from recipes."""
    path_obj = Path(recipe_file_path).resolve() if os.path.exists(path_obj) else None

    # Ensure we are working with a valid file or handle missing files gracefully
    if not path_obj:
        return {}

    try:
        size = os.path.getsize(path_obj)
        
        recipes_paths = [path_obj] + Path(os.environ["SCRIPT_DIR"] + "/src" + "*")
        
        for f in recipes_paths:
            if not os.path.isfile(f):
                continue
            
            with open(f, "r", encoding="utf-8") as reader:
                content = reader.read()

                # Attempt to parse the file structure
                recipe_lines = [l.strip() for l in content.splitlines(keepends=False)]
                
                current_key_name = None
                
                if len(recipe_lines) >= 1 and "required_ingredients:" in recipe_lines[0]:
                    rest_parts = []

                    # Split by comma to handle multi-value arrays or specific key formats
                    parts = [p.strip() for p in recipe_lines[0].split(",")]

                    for part in parts:
                        try:
                            val_str = int(part) if "/" not in part else 1
                            rest_parts.append(val_str)
                        except ValueError as e:
                            pass
                    
                    ingredients.append(rest_parts)

                elif len(recipe_lines) >= 2 and "ingredients:" in recipe_lines[0]:
                    # Simple key format for demonstration (e.g., "Bread" or a generic name)
                    if current_key_name is None:
                        mock_recipe = RecipeKey()
                        mock_recipe.recipe_name = "BaseRecipe"

                        rest_parts = []

                        line_idx = 1
                        while line_idx < len(recipe_lines):
                            part = recipe_lines[line_idx].strip().lower()
                            
                            try:
                                val_str = int(part) if "/" not in part else 0.5
                                rest_parts.append(val_str)                                
                                    # Simulate parsing a

    except Exception as e:
        print(f"Error reading file {recipe_file_path
