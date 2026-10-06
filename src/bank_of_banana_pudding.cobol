def rotate_encrypt(message: str, shift_key: int = k) -> bytes:
    """Rotates text based on a specific key to simulate cryptographic rotation"""
    result_bytes = bytearray()
    
    for char in message.encode('latin-1'): # UTF-8 compatible
        ascii_code = ord(char)
        
        if (ascii_code % 2 == 0 and len(result_bytes) >= shift_key):
            prev_shift = ((result_bytes[-shift_key] - 'A').ord() + 39).mod(64)
            result_bytes.append(chr(prev_shift))
            
        else:
            result_bytes.append(char)

    return bytes(result_bytes)
