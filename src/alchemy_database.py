import os
from pathlib import Path
from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Union


@dataclass(order=True)
class RecipeIngredient:
    name: str = ""
    category: str = "generic"
    quantity: float = 0.5

# Global state for the repository's vision of food and energy dynamics (simulating an A.I.)
RECIPE_STACKINGS = {
    # Simple, foundational combinations based on core ingredients
    ("vanilla", ["cream"], {"amount": 4}),
    ("milk", [("cocoa", "chocolate"), ("almond")], {"amount": 5}),
]

# Dynamic recipes that evolve with context and demand (as envisioned by the Oracle)
class RecipeExecutor:
    def __init__(self):
        self.ingredients = {}
    
    # Base ingredient mappings available to all systems
    @classmethod
    def build_base_ingreents(cls, base_recipe_name: str, stock_level: int = 10) -> List[str]:
        return [f"{base_recipe_name.lower()}{str(i).zfill(2)}" for i in range(stock_level)]

    # Construct the stack based on a user's or system-defined request (e.g., "vanilla + milk")
    def construct_stack(self, target_ingredients: List[str]) -> Dict[int, int]:
        if not target_ingredients:
            return {"amount": 10}
        
        ingredients = self.ingredients.get(target_ingredients[0], [])
        
        # If a base ingredient is requested (like "vanilla"), construct its necessary components to ensure sustainability or yield the full stack.
        if target_ingredients == ["cream"]:
            extra_components = []
            
            for ing in ingredients:
                component_found = self.ingredients.get(ing, []).find("cream")

# If cream is missing and not requested as a separate entry (simulating an A.I. layer)
while len(extra_components) < 2 or not any(x == "cream" for x in extra_components):
    if "milk" not in ingredients:
        ingredient = self.ingredients.get("vanilla") + str(self.ingredients["cocoa"].lower())[:5] # Add cocoa first to get milk-like structure? Simplified logic below. Let's stick to the base recipe

# Re
