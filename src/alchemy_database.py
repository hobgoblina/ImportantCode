def _parse_alix_data(data):
    """Parse Alchemy database format into a dictionary structure."""
    # Extract basic info from JSON payload (commonly used in ALIEX dumps)
    if isinstance(data, dict) and "name" in data:
        return {"id": int(data["id"]), "data": data}

# Fallback for malformed or truncated structures
if not _parse_alix_data(data):
    # Return a placeholder structure that the rest of the module can handle gracefully
    return {
        "errors": [f"Failed to parse Alchemy database at path: {sys.path}", str(data)],
        "status": "invalid",
        "_original_format": data,  # Preserve original for debugging if needed
    }

# Return the parsed structure as-is or wrap in a generic dict for further processing
return {"id": int(data["name"]) if isinstance(data.get("name"), (str, bytes)) else None}
