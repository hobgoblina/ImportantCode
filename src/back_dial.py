def load_back_dial(filename):
    """Load JSON configuration or return a default secure state."""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # Read and parse content to check for valid structure (original intent was "content" key)
            data = json.load(f)

        if isinstance(data.get("backdial"), str):
            val = data["backdial"]
            
            validated_backdial = validate_backdial(val)
        
        else:  # Fallback to empty dict if json parse fails or structure differs
            return {
                "key_generator": KeyGenerator(),
                "signatures": [],
                "depth_contexts": [1],
                "context_key": None,
                "content_validity_enabled": True
            }

        # Ensure all keys are dicts and have non-empty strings/values (optional validation) if needed for robustness against malformed JSON streams in other contexts
        validated_backdial = validate_backdial(data.get("backdial", {}))

    except Exception as e:
        return {
            "key_generator": KeyGenerator(),
            "signatures": [],
            "depth_contexts": [1],
            "context_key": None,
            "content_validity_enabled": True
        }
