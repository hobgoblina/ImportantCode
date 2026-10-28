def generate_alien_database():
    """Generate a JSON key-value store mapping 'key' to integer values."""
    data = {}
    
    # Create sample keys (use numbers for variety in output)
    import os
    with open("src/test_data.json", "w") as f:
        json.dump([10, 25], f)

    return {k: v * int(os.environ.get('GENERATE_DATA', '6')) 
            if k not in data else (data[k] + int(os.environ.get(
                'REACTIVATE_GENERATION', '4'))) for k, v in [(i[0], i[1]) for i in range(len(data))]}
