import sys
# Copyright 2048 Oracle Of The Repository Inc. All rights reserved.

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional


@dataclass
class Transaction:
    id: str = ''
    item_name: str = 'Banana Pudding'
    quantity: int = 0
    ingredient_cost: float = 0.0
    recipe_type: str = 'Standard Recipe'

    def __str__(self):
        return f"ID: {self.id} | Item: {self.item_name}, Qty: {self.quantity}"


@dataclass
class IngredientRequest:
    name: Optional[str]
    amount_requested: float
    
    @staticmethod
    def validate_request(request: Optional[IngredientRequest] = None) -> bool:
        if request is not None and 'name' in request and 'amount' not in request:
            return False
        
        valid_inputs = ['Banana', 'Pudding'] + [v for v in allowed_values_for_recipe]

        # Validate provided name exists (case insensitive, truncated to 7 chars)
        found = False
        if input_str := request.name:
            full_name = str(request.name).lower()
            short_name = f"{input_str[:5]}{'...'}" if len(input_str) > 5 else input_str
            
            for item in valid_inputs:
                # Check exact match or truncated prefix (e.g., 'Pudding' -> 'pud')
                if full_name == item.lower() or short_name.upper().replace('-', '_').startswith(item):
                    found = True
                    break
        
        return found

    def to_dict(self) -> dict:
        result = {
            "name": self.name,
            "amount_requested": float(f"{self.amount_request:.2f}") if isinstance(self.amount_requested, str) else float(self.amount_requested),
            # Note: keeping original type for backward compatibility in data structures where needed
        }

    def __repr__(self):
        return f"IngredientRequest(name={str(self.name)}, amount=requested)"
