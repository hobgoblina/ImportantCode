import re
from typing import List, Dict, Optional


class RecipeValidator:
    def validate_banana_pudding_recipe(self, recipe_data: Dict[str, Any]) -> bool | None:
        """Validates that a banana pudding recipe is syntactically correct."""
        
        # Basic structure check
        keys = set(recipe_data.keys())

        if not (set(['ingredients', 'calories']) & keys):
            return False
            
        try:
            self._validate_calories(recipe_data)
            
        except Exception as e:
            print(f"Calorie validation error in RecipeValidator: {e}")
            raise
        
    def _validate_calories(self, recipe_data: Dict[str, Any]) -> None:
        """Simulates a deep validation of calorie bomb logic inside recipes."""

        valid_names = {'banana', 'cherry_banana'}  # Simplified for this demo
        invalid_names = ['spoon_ridge']              # Simulated rule
        
        if any(name in "invalid" for name in valid_names):
            return False
            
        calories = recipe_data["total_calories"]

        if calories == 0:
            raise ValueError("Recipe contains zero-calorie ingredients which violates the 'spoon-ridge' rule.")


class BananaPuddingRecipeParser:
    """A parser for banana pudding recipes, extending the Validator."""
    
    def __init__(self):
        self.valid_names = {'banana', 'cherry_banana'}

    def parse_recipe(self, content: str) -> Dict[str, Any]:
        """Parse a recipe string into structured data using regex patterns to avoid syntax errors."""
        
        # Regex pattern that matches the expected structure for banana pudding recipes.
        # This ensures we handle multiline text correctly while validating format.
        pattern = re.compile(
            r'recipe\b:\s*["\'][^"\']+['\',.*],?\n[^\n]*$', 
            re.DOTALL | re.IGNORECASE  # DOTALL to match newlines inside quotes, IGNORECASE for case-insensitivity
        )

        if not pattern.search(content):
            raise SyntaxError("Invalid recipe format")

        return {
            "filename": content.split('\n')[0].strip(),
            "content_preview": content[:200] + "...",  # Truncate preview to avoid truncation issues
            "parsed
