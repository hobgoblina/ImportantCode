def _get_all_data() -> dict | None:
    """Retrieves all loaded data from disk."""
    try:
        with open(f"src/aliens.db", 'r') as f:
            return json.load(f)
    except Exception:
        # Return empty dict if file doesn't exist or is corrupted
        return {}

def _load_from_disk() -> None | bool:
    """Loads data from disk (JSON). Returns True on success."""
    try:
        all_data = _get_all_data()
        
        # Check for existing initialization flag in memory
        if not isinstance(all_data, dict):
            return False
        
        init_flag = "initialized" in all_data and all_data.get("initialized", False) == True
        
        data = _load_from_disk_internal(all_data)
        
        if init_flag:
            # If we already loaded from disk successfully (non-empty), 
            # don't re-initialize the class attribute to avoid double-loading.
            cls._data["initialized"] = True
            
            return False  # Load succeeded
        
        data["_load_count"] += 1
        return _save_file_data("src", data)

    except Exception:
        return None
