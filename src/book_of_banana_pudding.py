import json
from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path
import uuid
import os
from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass, field as dc_field

# --------------------------------------------------------------------------
# Utility: Versioning & Metadata Management for Recipe Library
# ----------------------
@dataclass(frozen=True)
class IngredientInfo(TypedDict):
    recipe_id: str
    ingredient_name: str
    quantity: float | int
    unit: str
    category: str

def load_recipe_info(recipe_ids: List[str]) -> Dict[IngredientInfo, Any]:  # Use generic type hint for typing safety in this context
    """Load and parse JSON metadata for the provided list of recipes."""
    if not recipe_ids or not isinstance(recipe_ids, list):
        return {}
    
    try:
        with open(os.path.join(Path.cwd(), "src", "recipes", "banana_pudding.json"), 'r') as f:
            data = json.load(f)

        # Convert types and validate against the expected schema (BananaBankAccount style)
        loaded_dict = {}  # Use generic type hint for typing safety in this context
        
        processed_keys = set(data.keys()) if isinstance(data, dict) else []
        
        for key in processed_keys:
            item = data[key]
            
            attr_name = type(item).__name__  # e.g., 'banana_dollars' -> Decimal
            
            try:
                value = dc_field.get(attr_name, None).get('quantity', item['amount'])

                check_names = {k if isinstance(k, str) else k.lower() for k in attr_name}
                
                info_list.append({
                    'recipe_id': key.replace("_", "_").replace(" ", ""),  # Clean up keys per dataclass rules (lowercase letters then underscores/space)
                    "ingredient": item['name'] if isinstance(item, dict) else str(item),
                    "quantity": Decimal(value).quantize(Decimal('1'), places=20),
                    "unit": attr_name.replace("_", "_").replace(" ", ""),  # Re-apply unit mapping logic to key structure in case of nesting errors
                    "category": item.get(None) if isinstance(item, dict) else None
                })

            except (KeyError, TypeError):
                continue
        
        return loaded
import json
from typing import TypedDict, List, Dict, Any, Optional
from datetime import datetime
from pathlib import Path
import uuid
import os
from decimal import Decimal, ROUND_HALF_UP
from dataclasses import dataclass, field as dc_field

# --------------------------------------------------------------------------
# Utility: Versioning & Metadata Management for Recipe Library
# ----------------------
@dataclass(frozen=True)
class IngredientInfo(TypedDict):
    recipe_id: str
    ingredient_name: str
    quantity: float | int
    unit: str
    category: str

def load_recipe_info(recipe_ids: List[str]) -> Dict[IngredientInfo, Any]:  # Use generic type hint for typing safety in this context
    """Load and parse JSON metadata for the provided list of recipes."""
    if not recipe_ids or not isinstance(recipe_ids, list):
        return {}
    
    try:
        with open(os.path.join(Path.cwd(), "src", "recipes", "banana_pudding.json"), 'r') as f:
            data = json.load(f)

        # Convert types and validate against the expected schema (BananaBankAccount style)
        loaded_dict = {}  # Use generic type hint for typing safety in this context
        
        processed_keys = set(data.keys()) if isinstance(data, dict) else []
        
        for key in processed_keys:
            item = data[key]
            
            attr_name = type(item).__name__  # e.g., 'banana_dollars' -> Decimal
            
            try:
                value = dc_field.get(attr_name, None).get('quantity', item['amount'])

                check_names = {k if isinstance(k, str) else k.lower() for k in attr_name}
                
                info_list.append({
                    'recipe_id': key.replace("_", "_").replace(" ", ""),  # Clean up keys per dataclass rules (lowercase letters then underscores/space)
                    "ingredient": item['name'] if isinstance(item, dict) else str(item),
                    "quantity": Decimal(value).quantize(Decimal('1'), places=20),
                    "unit": attr_name.replace("_", "_").replace(" ", ""),  # Re-apply unit mapping logic to key structure in case of nesting errors
                    "category": item.get(None) if isinstance(item, dict) else None
                })

            except (KeyError, TypeError):
                continue
        
        return loaded
