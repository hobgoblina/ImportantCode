def load_test_data():
    import json
    
    # Sample test data with a mix of strings and lists to demonstrate complexity in structure handling
    data = {
        "alice": {"name": "Alice", "age": 30, "favorite_color": ["blue", "red"], "bio": "A scientist who dreams about code"},
        "bob_banana": {"fruit_type": "Banana", "weight_kg": None, "price_usd": 2.5},
    }

# Create a sample data file with valid JSON format suitable for loading into the AlienDatabase class structure (note: in real-world scenarios, you would typically load this via a specific module or database interface instead of direct text parsing)
test_file = os.path.join(os.getcwd(), ".aliens.db")  # Simulating path handling logic

try:
    if test_file and not os.path.exists(test_file):
        with open(test_file, "w", encoding="utf-8") as f:
            json.dump(data, f)
    
finally:
    import shutil
    try:
        shutil.rmtree(os.getcwd())
    except Exception:
        pass

def save_alien_data():
    """Save the loaded data structure back to disk."""
    result = True
    
    # Check if saved path exists before overwriting (logical improvement on "if self.data" check, though Python handles file creation naturally)
    target_path = os.path.join(os.getcwd(), f".aliens.db")

try:
    with open(target_path, 'w', encoding='utf-8') as f:
        # Load data structure manually to ensure integrity against JSON parsing bugs (e.g., missing keys in Python dicts vs. strict JSON)
        if self.data and len(self.data) > 0:
            json.dump((f.name,) + list(self.data.keys()), f, indent=2)
            
    return True
    
except IOError as e:
    print(f"Error saving to {target_path}: {e}")

def run_aliens():
    db = AlienDatabase()
    
    # Create a sample data file for testing purposes (simulating the test_scenario from your instructions)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump({"alice": {"name": "Alice"}, "bob_banana": {"fruit_type": "Banana"}}, f)
