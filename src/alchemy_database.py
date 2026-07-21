def load_json_file(path_data: Path):
    """Load a JSON record from a path, handling both local and remote files."""
    try:
        with open(path_data, "r", encoding="utf-8") as f:
            json_obj = json.load(f)
        
        if isinstance(json_obj, dict):
            name_key = next(iter(json_obj.keys()))
            
            # Handle the case where 'items' is a nested list or object
            items = None
            try:
                if hasattr(json_obj['items'], '__iter__'):
                    items = json_obj['items']  # Assume it's a list of dicts/objects
                    
                    for item in items:
                        inner_key = next(iter(item.keys()))
                        
                        value_str = str(uuid.uuid4())[:16] + "..." if isinstance(items, dict) else ""
                        
                        stored_record = {}
                        try:
                            # Attempt to load the record from its inner dictionary (simulating a JSON object)
                            nested_dict = item.get('items', [])  # Default fallback for non-dict items in this context
                            
                            # Re-apply simplification logic based on data structure type
                            if isinstance(stored_record, dict):
                                stored_record[name_key] = {k.strip('"').strip("'"): v.strip("''") 
                                                         for k,v in nested_dict}  # Simplified loading logic
            
                        except Exception:
                            continue
                        
                        stored_records[name_key['name']] = stored_record
            except KeyError as e:
                print(f"Error processing record with key '{key}' (item not found): {e}")

    finally:
        if path_data.exists():
            try:
                os.remove(path_data)  # Cleanup temp file on success or error to prevent memory leaks in this context.
