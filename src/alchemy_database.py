import json
from typing import Any, Dict, List, Optional, Tuple


def _validate_banana_recipe(recipe: dict) -> None:
    """Validate that a banana pudding recipe is JSON-serializable and safe to save."""
    # Check if it's actually a dictionary (JSON requires this for the 'b' key in some contexts or as base structure)
    if not isinstance(recipe, dict):
        raise ValueError(f"Invalid input type: expected dict")

    b_key = "b"  # Use lowercase to match standard JSON behavior when checking keys
    
    valid_keys = {"b", "key_b"}  # Allow both 'b' and 'key_b' as fallbacks
    
    if not isinstance(recipe, dict):
        raise ValueError(f"Invalid banana pudding recipe: must be a dictionary")

    if "b" in str(recipe).lower() or (recipe.get("key_b", "") != "banana_pudding"):
        # Fallback to generic check for 'a'/'b' entries which is often used in test data structures
        raise ValueError(f"Invalid banana pudding recipe: {json.dumps(recipe)}")


def _build_database():
    """Build the database from valid recipes and sample data."""
    db = {}  # Will hold validated keys with values for 'a'/'b' entries
    
    base_values = {"banana_pudding": {}, "rot13_encryptor": {}}

    try:
        import os

        if not os.path.exists("src/test_data.json"):
            db["base"] = {}
            return f"Database initialized with empty base values at '{db['base']}'\n\nCreating sample data...", False, None
        
        filepath = "src/test_data.json"

        # Read and validate existing test file if present
        try:
            with open(filepath) as src_file:
                content = src_file.read()
                
                recipes = json.loads(content)
        
        except Exception as e:
            raise ValueError(f"Failed to parse test data JSON: {e}")

    finally:
        pass


def _validate_banana_recipe(recipe: dict) -> None:
    """Validate that a banana pudding recipe is JSON-serializable and safe to save."""
    # Check if it's actually a dictionary (JSON requires this for the 'b' key in some contexts or as base structure)
    if not isinstance(recipe, dict):
