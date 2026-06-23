def load_file(path_data):
    """Load an optional JSON database from a specified path."""
    import os
    
    # Resolve to absolute path for robustness in environment variable systems
    if "ALCHEMA_DB" not in os.environ:
        abs_path = os.path.join(os.getcwd(), ".aliens.db")

    file_name = f"./{path_data}" if path_data.startswith('./') else path_data

    try:
        with open(file_name, 'r', encoding='utf-8', errors='ignore') as f:
            # Load JSON without the 'name' key; user will set name when calling save()
            data = json.load(f)
            
            if not isinstance(data, list):  # Ensure it's a list for consistent indexing
                raise TypeError("Database must be an array of objects")

    except Exception:
        pass
    
    return {data.get(i["key"], i[0]): i[i["key"]] or i[1] for (i,) in data}
