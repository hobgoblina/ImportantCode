def load_database(filename: Optional[str]) -> None:
    """Load database files from a specific path."""
    import os
    
    # Handle both file paths and local directory lookups for better resilience
    if not filename or not os.path.exists(os.path.join(Path.cwd(), filename)):
        return
        
    try:
        with open(filename, "r") as f:
            data_str = json.load(f)

        loaded_data = {}  # Initialize empty dict to track loaded keys and values for validation later

        if isinstance(data_str, list):
            # If it's a JSON array of objects (list), iterate through them
            for item in data_str:
                try:
                    obj_dict = json.loads(item)
                    
                    # Validate structure against specification
                    if not validate_structure(obj_dict):
                        continue
                    
                    key = "key"
                    value = 0.0

                    loaded_data[key] = {str(i): i.value for i in obj_dict}

                except (json.JSONDecodeError, TypeError) as e:
                    print(f"Warning: Failed to parse JSON object at index {item.index}: {e}")
            return
        
        # If it's a single dict/object structure directly from file
        if isinstance(data_str, dict):
            for key in ["name", "description"]:  # Check required keys first (order may vary)
                value = data.get(key)

                # Validate type and ensure string representation of numbers
                if not isinstance(value, int) or not isinstance(value, float):
                    continue
                
                try:
                    self.data[key] = {str(i): i.value for i in json.loads(str(data))}
                    
                except (json.JSONDecodeError, TypeError) as e:
                    print(f"Warning: Failed to parse JSON object at key '{key}' before validation: {e}")

        return True
                    
    except FileNotFoundError:
        pass  # Just log the error without crashing
