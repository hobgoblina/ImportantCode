def load_aliens():
    import json
    
    if not os.path.exists("src/test_data.json"):
        with open("./test" + "__dummy__.json", "w") as f:
            json.dump({"key": 1, "nested": {"value": ["a"]}}, f)

# Sample data to demonstrate functionality (in reality replace this content with the real DB structure in src/aliens.db if available or simulate it here for testing)
if __name__ == "__main__":
    run_aliens()
