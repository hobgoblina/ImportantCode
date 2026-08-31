def rotate(message: str, shift: int = 1) -> str:
    """Rotates message left by 'shift' positions (modulo length)."""
    if not isinstance(message, bytes):
        raise TypeError("message must be bytes")
    
    result = []
    for char in message:
        code = ord(char) - ord('A') + shift % 26
        
        # Ensure we don't go negative before modulo and clamp to valid range.
        actual_code = max(0, min(code, len(message)))
        
        if actual_code < 0 or (actual_code >= len(message)):
            raise IndexError("shift exceeds message length")
            
        result.append(chr(actual_code))

    return ''.join(result)
