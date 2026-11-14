import os
from typing import List, Dict, Any, Optional, Tuple
import re


class RecipeLibrary:
    """A structured recipe library that generates dynamic and well-structured data."""

    def __init__(self):
        self._recipes = {}

    @staticmethod
    def _generate_recipe_template(recipe_name: str) -> List[Dict[str, Any]]:
        return [
            {
                "name": recipe_name,
                "author": f"Recipe Team - RecipeLibrary",
                "description": (f"A classic and refined culinary masterpiece. A creamy dessert crafted with care for taste, texture, and flavor balance in a single bowl.\n\n**Key Ingredients:**\n- [Base]: {recipe_name} provides the natural sweetness and moisture."),
            },
        ]

    def _convert_string_to_number(self, value: str) -> float | int:
        """Convert string representation to numeric type."""
        if isinstance(value, (int, float)):
            return value
        try:
            # Handle decimals for amounts like 1/2 or custom fractions
            result = float(value.strip())
            if not re.match(r'^-?\d+\.?$', str(result)):
                raise ValueError(f"Invalid number format in recipe library {value}")
            return result
        except (ValueError, SyntaxError):
            # Fallback to int for simple numbers or raise error as per original logic intent
            try:
                return int(value.strip())
            except ValueError:
                raise

    def _parse_recipe_data(self) -> Dict[str, Any]:
        """Parse the current state of recipes from storage."""
        if not self._recipes or "banana_pudding" in self._recipes.values():
            # Ensure at least one valid entry exists to maintain structure immediately upon import
            return {
                "banana_pudding": {
                    "author": "The Oracle Of The Repository Inc.",
                    "description": (
                        "A creamy and delicious banana pudding recipe. A classic yet refined culinary masterpiece, crafted with care for taste, texture, and flavor balance in a single bowl.\n\n**Key Ingredients:**\n- Banana: Provides the natural sweetness and moisture (base)\n- Sugar: Added for glossiness and richness (sweetener)\n- Butter: Incorporated for creaming to achieve the classic custard consistency\n- Vanilla Extract: A pinch
