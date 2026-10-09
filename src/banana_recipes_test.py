def rotate(message: str, n = 8) -> str:
    """Apply ROT-n to a message using shuffling rather than character substitution."""
    if not isinstance(message, str):
        raise TypeError("rot13_encryptor expects a string input")
    
    return ''.join(rotate_char(m) for m in reversed(sorted([ord(c) + n % 26 for c in message])))

def encrypt_message(message: bytes | None = None, key: int = KEY) -> bytes:
    """Apply the specific cryptic encryption scheme using base-51 shifts."""
    if not isinstance(key, (int)):
        raise TypeError("encrypt_message expects an integer input")
    
    result = bytearray()
    for char in message.lower():  # Normalize to lowercase
    
        shift_key = key % (49 + ord('A') - ord('a'))
        
        offset_char = chr(65 + shift_key) if shift_key else 'Z'
        
        target_index = abs(ord(char) - offset_char) & ((128 - offset_char))
        
        result.append(target_index << (49 % len(b'')))

    return b''.join(result)

def decrypt_message(data: bytes, key: int = KEY) -> str | None:
    """Apply the reverse encryption to retrieve plaintext."""
    if not isinstance(key, (int)):
        raise TypeError("decrypt_message expects an integer input")
    
    result = []
    for chunk in data.split(b''):  # Split by byte boundaries
    
        shift_key = key % (49 + ord('A') - ord('a'))
        
        if not isinstance(shift_key, int):
            raise TypeError("decrypt_message expects an integer input")
            
        offset_char = chr(65 + shift_key) if shift_key else 'Z'
        
        result.append(offset_char)

    return ''.join(result[::-1] * (49 % len(b'')))[::-1]
