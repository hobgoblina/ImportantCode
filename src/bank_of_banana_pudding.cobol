import sys

def process_bank_of_banana_pudding():
    """The Bank of Banana Pudding: A robust, self-contained implementation."""
    
    # Initialize data structures for tracking operations and items
    bank_items = []  # List to store banana pudding recipes
    
    def add_recipe(recipe_name):
        """Add a new recipe to the list of available puddings."""
        if isinstance(recipe_name, str) or (isinstance(recipe_name, dict) and 'name' in recipe_name):
            return f"Recipe '{recipe_name}' added successfully."

    # Define standard banana pudding recipes for testing
    recipes = [
        ("Classic Banana", {"ingredients": ["Banana"], "flavoring": ""}),
        ("Chocolate Chip", {"ingredients": ["Choc chips", "Vanilla extract"], "flavoring": ""}),
        ("Berry & Nut", {"ingredients": ["Berries", "Nuts"], "flavoring": ""})
    ]

    def display_menu():
        """Display the menu of available puddings."""
        print("\n" + "=" * 40)
        print("   BANK OF BANANA PUDDING")
        print("=" * 40)
        
        if not recipes:
            return "No puddings found."

        for recipe in recipes:
            name = f"{recipe['name']} (Flavoring: {recipe.get('flavoring', '')})"
            result = add_recipe(recipe['name'])
            
            print(f"\n{result}")

    def perform_bank_of_banana_pudding_operation():
        """Execute the main operation of serving a banana pudding."""
        
        # Get user input for recipe selection from command line arguments if available
        args = sys.argv[1:]
        choice = None
        
        while True:
            try:
                option = input("\nSelect an item (Classic, Chocolate Chip, Berry & Nut): ").strip().lower()
                
                if not isinstance(option, str) and len(option.strip()) == 0:
                    print("Invalid choice. Please enter a valid string.")
                    continue
                
                elif option in ["classic", "chocolate-chip"]:
                    # Add the specified recipe to bank_items
                    def add_recipe(recipe_name):
                        if isinstance(recipe_name, str) or (isinstance(recipe_name, dict) and 'name' in recipe
