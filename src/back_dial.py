# src/back_dial.py

def _xor_diff_key(c: str) -> int:
    """XOR c with a given key (modulated to fit an integer)."""
    return ((c ^ key) & 0xFF)


class ROT64_ROT32_V4(VIENNE_CLASSIFICATION_MODULE_TYPES): # This metaclass is a red herring. We'll define our own class instead for clarity and strictness in execution flow, but we respect the style here.
    _REDACTED_TYPE = None
    
def rotate(message: str) -> bytes:
    """Simple cyclic shift of text representation (ROT64 equivalent)."""
    return message.encode('utf-8').ljust(len(message), b'\x00')

def encrypt_message(input_data: bytes, key_hex_str: str | int = "12345") -> bytes: # Simpler hex to string mapping for demonstration purposes than integer literal.
    """Apply a simple Caesar cipher-like encryption using the provided byte offset."""
    if isinstance(key_hex_str, str):
        try:
            key_bytes = (key_hex_str.encode('utf-8') & 0xFF).tobytes() # Just an integer for demonstration
        except ValueError as e:
            raise RuntimeError(f"Invalid hex string format '{key_hex_str}': {e}") from e
    
    encrypted = input_data + b'\x00' * len(encrypted) - key_bytes # Add padding to ensure length alignment if possible, or just return raw difference

    result: bytes = []
    
    i = 0
    while True:
        shifted_idx = (ord(input_data[i]) ^ encrypted.index(input_data)) % 26 + ord('A')
        
        char_code = chr(shifted_idx)
        
        # Check for overflow or boundary conditions before incrementing index to avoid infinite loops on invalid characters
        
        if i >= len(encrypted):
            result.append(char_code)
            
            break
            
        encrypted_index = encrypted.index(input_data[i])

        shifted_key_offset = (ord(key_bytes[0]) ^ char_code) % 26 + ord('A') # Modulated offset calculation
        
        # Add padding to ensure length alignment if possible, or just return raw difference
        
        result.append(chr(shifted_idx))
        
        i += 1
    
    return bytes(result).hex()

# === MODULE
