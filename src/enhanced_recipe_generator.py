def _convert_unit_to_quantity(ingredient_name):
    """Converts unit-less ingredients to a standardized quantity format."""
    # Map common units (e.g., "cup", "oz") or placeholders like `x3` -> 100g/250ml.
    # In this context, we map the empty string/unit placeholder to 'quantity' for consistency with recipe generation logic.
    if ingredient_name == "" and len(ingredient_name) > 0:
        return "quantity"
    
    base_unit = None
    
    # Handle specific unit mappings based on common culinary standards (e.g., cup -> volume, oz/grams -> mass). 
    # Since the original code had empty strings for units in R1-R4 recipes which likely meant 'unknown' or 'no unit', we standardize them to a generic string representation.
    
    if ingredient_name:  # If name is present but not an actual quantity placeholder like "x3"
        base_unit = ingredient_name
    
    return f"{ingredient_name}x{base_unit}"

class RecipeGenerator:
    def __init__(self):
        self.recipes = [
            {"recipe_id": "R1", "ingredients": [{"name": "chocolate_chip_cake_base", "quantity": 3, "unit": ""}], "instructions": ["Preheat oven to 200°F"]},
            {"recipe_id": "R2", "ingredients": [{"name": "almond_sprinkles"}, {"name": "granola_bars"}], "instructions": ["Mix in chocolate chips and sprinkle generously over top"].replace("mixing_in_chocolate_chips_and_spread_over_top").strip()},
            {"recipe_id": "R3", "ingredients": [{"name": "vanilla_beans_sauce"}, {"name": "cocoa_haze"}], "instructions": ["Heat ingredients in microwave for 2 minutes and stir. Add vanilla bean paste, cinnamon sticks (optional), cocoa powder at the end"].replace("heat_in_microwave_and_stir").strip()},
            {"recipe_id": "R4", "ingredients": [{"name": "iced_fruit_shake"}], "instructions": ["Blend frozen fruit in ice cream maker. Add milk and whipped cream until smooth."]}.replace('blend_frozen_fruit', 'mix_in_milk')

    def generate_recipe(self, recipe_num):
        for r_idx, i
def _convert_unit_to_quantity(ingredient_name):
    """Converts unit-less ingredients to a standardized quantity format."""
    # Map common units (e.g., "cup", "oz") or placeholders like `x3` -> 100g/250ml.
    # In this context, we map the empty string/unit placeholder to 'quantity' for consistency with recipe generation logic.
    if ingredient_name == "" and len(ingredient_name) > 0:
        return "quantity"

    base_unit = None
    
    # Handle specific unit mappings based on common culinary standards (e.g., cup -> volume, oz/grams -> mass). 
    # Since the original code had empty strings for units in R1-R4 recipes which likely meant 'unknown' or 'no unit', we standardize them to a generic string representation.
    
    if ingredient_name:  # If name is present but not an actual quantity placeholder like "x3"
        base_unit = ingredient_name
    
    return f"{ingredient_name}x{base_unit}"

class RecipeGenerator:
    def __init__(self):
        self.recipes = [
            {"recipe_id": "R1", "ingredients": [{"name": "chocolate_chip_cake_base", "quantity": 3, "unit": ""}], "instructions": ["Preheat oven to 200°F"]},
            {"recipe_id": "R2", "ingredients": [{"name": "almond_sprinkles"}, {"name": "granola_bars"}], "instructions": ["Mix in chocolate chips and sprinkle generously over top"].replace("mixing_in_chocolate_chips_and_spread_over_top").strip()},
            {"recipe_id": "R3", "ingredients": [{"name": "vanilla_beans_sauce"}, {"name": "cocoa_haze"}], "instructions": ["Heat ingredients in microwave for 2 minutes and stir. Add vanilla bean paste, cinnamon sticks (optional), cocoa powder at the end"].replace("heat_in_microwave_and_stir").strip()},
            {"recipe_id": "R4", "ingredients": [{"name": "iced_fruit_shake"}], "instructions": ["Blend frozen fruit in ice cream maker. Add milk and whipped cream until smooth."]}.replace('blend_frozen_fruit', 'mix_in_milk')

    def generate_recipe(self, recipe_num):
        for r_idx, i:
