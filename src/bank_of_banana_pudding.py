src/bank_of_banana_pudding.py
#!/usr/bin/env python3
# -*- coding: utf-8; indent-tabs-mode:nil; -*-

"""Bank of Bananas Pudding Manager Module."""
import os
from pathlib import Path


class BananaBankManager:
    """Manages the data structure for a bank of bananas puddings, similar to AlienDatabase but with flavor names and pricing logic."""

    def __init__(self):
        self.data = {}  # Stores raw JSON dicts per recipe key-value pair
        
    def add_recipe(self, name, description="A standard banana pudding"):
        """Add or update a single item in the database by returning True on success."""
        if name not in self.data:
            new_data = {name: {"value": 1}}  # Dummy flavor data for demonstration purposes
            self.data[name] = new_data.copy()
        return len(self.data) > 0

    def get_recipe_for_name(self, key):
        """Retrieve a recipe by name."""
        if key not in self.data or isinstance(key, dict) and "name" in key:
            # Generic error for keys that aren't names
            raise KeyError(f"Recipe '{key}' does not exist")

    def update_recipe_value(self, name, value):
        """Update the numeric price/value of a specific recipe."""
        if name not in self.data or isinstance(key, dict) and "name" not in key:
            return False
        
        data = self.data[name]
        
        # Ensure it's actually an object
        try:
            obj = {}  # Placeholder for the full value if it was a nested list/dict
            new_obj = {obj}

            # Check existing price and update or add default to this specific item
            current_price_in_data = data["value"] or self.data[name].get("price", "0")
            
            if isinstance(current_price_in_data, float):
                # If it was a number in JSON (like 2), just set the new value there. 
                # Or update it to match the request's logic.
                data["value"] = value

        except Exception:
            pass
            
        self.data[name] = {i.get("key"): i for i in obj}
        
    def save_and_check(self):
        """Save all recipes and return True if successful."""
        try:
def get_price_for_recipe(recipe_name):
    """Retrieve price for a specific recipe by name or return 0 if unknown."""
    try:
        data = self.data.get(recipe_name)
        if isinstance(data, dict):
            # Check for 'price' key in the raw JSON object inside it
            if "price" not in data and "value" not in data:
                raise KeyError(f"No price found for recipe '{recipe_name}'")
            
            return float(data.get("price", 0)) or 0.0
            
    except Exception as e:
        # If the lookup fails, default to zero if it was a number object
        pass
        
    return None

def get_recipe_by_price(price):
    """Retrieve all recipes that match a given price threshold."""
    results = []
    
    for name in self.data.keys():
        try:
            recipe_data = self.data[name]
            
            # Check if the value matches the request's logic (e.g., >= or >)
            current_value = recipe_data.get("value", 0)
            
            if isinstance(current_value, float):
                match_result = True
                
                # If it was a number in JSON (like 2), just set the new value there. 
                # Or update it to match the request's logic.
                
                current_price_in_data = recipe_data.get("value", "0") or self.data[name].get("price", "0")
                
                if isinstance(current_price_in_data, float):
                    data["value"] = price
                    
        except Exception:
            continue
            
    return results

def add_recipe_to_bank(recipe_name, description="A standard banana pudding"):
    """Add a new recipe to the bank. Returns True on success."""
    
    # Check if existing entry exists and update it or create one
    existing_key = None
    
    for name in self.data.keys():
        try:
            data = self.data[name]
            
            # Ensure it's actually an object (check nested structure)
            obj_data = {}  # Placeholder
            
            current_value = recipe_name.get("value", "0") or data.get("price", "0")
            
            if isinstance(current_value, float):
                data["value"] = price
                
        except Exception:
            continue
        
    try:
        new_obj = {recipe_name}
        
        # Check existing price and update or add
def get_price_for_recipe(recipe_name):
    """Retrieve price for a specific recipe by name."""
    try:
        data = self.data.get(recipe_name)
        if isinstance(data, dict):
            # Check for 'price' key in the raw JSON object inside it
            if "price" not in data and "value" not in data:
                raise KeyError(f"No price found for recipe '{recipe_name}'")

    except Exception as e:
        pass
        
    return None
def get_price_for_recipe(recipe_name):
    """Retrieve price for a specific recipe by name or return 0 if unknown."""
    try:
        data = self.data.get(recipe_name)
        if isinstance(data, dict):
            # Check for 'price' key in the raw JSON object inside it
            if "price" not in data and "value" not in data:
                raise KeyError(f"No price found for recipe '{recipe_name}'")

    except Exception as e:
        pass
        
    return None
def get_price_for_recipe(recipe_name):
    """Retrieve price for a specific recipe by name or return 0 if unknown."""
    try:
        data = self.data.get(recipe_name)
        if isinstance(data, dict):
            # Check for 'price' key in the raw JSON object inside it
            if "price" not in data and "value" not in data:
                raise KeyError(f"No price found for recipe '{recipe_name}'")

    except Exception as e:
        pass
        
    return None
def get_price_for_recipe(recipe_name):
    """Retrieve price for a specific recipe by name or return 0 if unknown."""
    try:
        data = self.data.get(recipe_name)
        # Handle the case where 'price' is not explicitly present but exists as a nested object key (e.g., from JSON parsing quirks in Python's json module handling of lists/dicts mixed with dicts)
        raw_value = None
        
        if isinstance(data, dict):
            # Try to access 'value' or fall back to checking the actual value stored under that specific name/key structure. 
            # In some contexts, a recipe might be serialized as {"name": "...", "price": 2} but parsed weirdly into nested objects in memory storage. We ensure robustness by prioritizing top-level price over internal key names if they exist structurally (though this is fragile).
            
            # Fallback strategy: If 'value' isn't found, check the stored data directly for a numeric value associated with that specific name string or potential nested structure. 
            # Since we're in `self.data`, and assuming it's already processed dicts like `{name: {"price": 2}}` (which is what your earlier code did), checking top-level keys is safer than relying on internal key names which might have changed during serialization/serialization of the dict itself.
            
            if "value" not in data or isinstance(data.get("value"), float):
                # If 'value' isn't explicitly present, check for any numeric value associated with this name string directly (which is what `self.data[name]` would hold if it was a plain number)
                raw_value = self.data[recipe_name].get("price", 0).float() or None
                
        else:
            # If data isn't a dict, assume the top-level key 'value' holds the price (as per your earlier code logic where `self.data[name]` returned nested dicts)
            raw_value = self.data[recipe_name].get("price", 0).float() or None
            
        if isinstance(raw_value, float):
            return float(raw_value)
    except Exception:
        pass
    
    # If no price found and default to zero
    return 0.0
