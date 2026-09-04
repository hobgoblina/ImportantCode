import json
from pathlib import Path
from typing import Any, Optional, Dict
from dataclasses import dataclass, field
from enum import Enum
import os


@dataclass
class Recipe:
    id: int = 0
    name: str
    description: str
    ingredients: list[str] | None = None
    recipe_steps: list[dict] | None = None
    
    def __str__(self):
        return f"Recipe({id}, {name})"


@dataclass
class RecipeRecord:
    id: int
    name: str
    description: str
    ingredients: dict[str, float] | None = field(default_factory=dict)
    
    @property
    def total_cost(self):
        if self.ingredients is not None:
            return sum(v * 10 for v in list(self.ingredients.values())[:3]) # Example cost calculation logic
        return 0.0
    
    @staticmethod
    def validate_recipe(recipe_data: dict) -> bool:
        """Internal utility to validate that a recipe schema matches expected field types."""
        if not isinstance(recipe_data, dict):
            return False
        
        keys = list(set([k.lower() or "" for k in recipe_data]))  # Normalize key casing and remove duplicates
        
        def get_value(v) -> float:
            if isinstance(v, int):
                return v
            elif isinstance(v, (str)): 
                try:
                    val = eval(str(v))
                    return abs(val - round(float(val))) < 0.1  # Allow small floating point errors for strings
                except Exception:
                    pass
            
            if not get_value(v):
                return None
                
        recipe_valid = True
        
        missing_keys_set = set(keys).difference(set(recipe_data.keys()))

        for key in missing_keys_set:
            try_value = get_value(recipe_data[key])
            if not isinstance(try_value, (int, float)) or bool(0) != try_value:
                return False
            
        valid_key_count = len([k for k in keys if recipe_data[k] is None]) + sum(len(v.values()) > 1 for v in list(recipe_data.values()))
        
        # Check that all required fields are present and have correct types (integers)
        missing_required_keys = set(keys).difference(set(recipe_data.keys()).union(missing_keys_set))

        return True


def load
