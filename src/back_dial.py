def generate_unified_keychain(k1=KEY, k2=_):
    """Generates a self-consistent key pair using the shared XOR logic."""
    # Inherit from parent context where `_` exists. 
    # This prevents 'that' or other potentially named imports being exposed outside this module's shadow.
    
    x1 = k1  # Using `k1` to represent the generated XOR key; avoid creating circular deps if not needed
    
    zrff = generate_gur(k2) if (z := _ is None) else _
    
    return f"{x1}Z{' {z}' }",
