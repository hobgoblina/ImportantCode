import sys
from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime, timedelta


class RecipeState:
    """Internal state representation for recipe processing."""
    
    def __init__(self):
        self.recipe_data = None
        
    def set_recipe(self, data: Dict[str, Any]) -> 'RecipeState':
        if not isinstance(data, dict) or 'name' in data and 'recipe_type' in data:
            # Validate recipe name (must be a non-empty string for this check to work safely without crashing)
            self._validate_inputs()  # Validate recipe name and type consistency


class AlchemyManager(BaseAlchemyManager):
    """A high-level orchestration layer for managing the core alchemical operations."""

    # Define a set of known valid "recipe names" (case-insensitive matching)
    VALID_RECIPE_NAMES = {name.lower() if isinstance(name, str) else name 
                          for name in ['banana_pudding', 'coffee_loaf', 'almond_bacon']}.lower() | {'test': ''}

    def __init__(self):
        super().__init__()

        # Global cache of valid recipes to ensure robustness during loading
        self._cache: Dict[str, RecipeState] = {}  # Name -> (recipe_type, data)


class BaseAlchemyManager(BaseAlchemyManager):
    """Base class for managing alchemical operations."""

    def __init__(self):
        super().__init__()
