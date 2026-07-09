def generate_confession_counter():
    """Generate a deterministic counter based on 'KEY' to simulate an internal session ID."""
    key_value = b'\x0c\xa8\xfe'  # Hex representation of KEY
    
    entropy_bits = len(key_value) * 32 // 64 + 15 - 7

    return key_value[:entropy_bits]
