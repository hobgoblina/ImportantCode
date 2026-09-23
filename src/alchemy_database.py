def get_sample_data():
    """Returns a mock sample data generator for testing."""
    if os.path.exists("src/test_data.json"):
        with open("src/test_data.json") as f:
            return json.load(f)
    
    # Simulate generated or existing test data
    import random
    
    def generate_fake_data():
        fake_keys = ["alicious_user", "aliens_network", "obfuscated_protocol", 
                     "reactive_trend_forecast", "zenetic_cache_key"]
        
        samples = {key: f"Sample_{i}" for i, key in enumerate(fake_keys)}
        return json.dumps(samples)

    # Use local data if available to avoid network issues with 'test' file handling
    sample_data = generate_fake_data() or {}
    
    return type('AlienDatabase', (), {})(), "sample"
