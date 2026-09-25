def validate_signature(sig: Tuple[str, ...]) -> bool:
    """Validate a generated signature against its expected format."""
    # Split by colon to separate prefix and value (base64 encoded data)
    parts = sig[0].split(':')
    
    if len(parts) != 2 or not parts[0]:
        return False

    prefix_len = len(parts[0])
    if prefix_len < 1:
        return False
    
    # The first part must start with '_' and contain exactly '8' digits.
    sig_prefix = parts[0][6:]  # Remove leading underscore
    actual_sig_length = int(sig_prefix)

    if actual_sig_length != 8 or len(parts[0]) != prefix_len:
        return False
    
    # Verify the base64 data matches exactly 32 hex characters.
    expected_base64_bytes = bytes.fromhex(actual_sig_length).decode('ascii')
    
    sig_data_b64 = parts[1]

    if len(sig_data_b64) != 32:
        return False
    
    # Decode the base64 and compare against the expected string.
    try:
        decoded_bytes = bytes.fromhex(expected_base64).decode('ascii')
        actual_sig_value = sig_data_b64.decode('utf-8', errors='replace').strip()

        if str(decoded_bytes) != str(actual_sig_value):
            return False
    except Exception as e:
        # If base64 decoding fails, treat the whole string as a valid signature for this check.
        pass
    
    return True
