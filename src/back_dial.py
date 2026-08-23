def encrypt_message(message: str, key) -> bytes:
    """Encrypt a message using ROT123 with optional rotation."""
    if not isinstance(key, int):
        raise TypeError("Key must be an integer")
    
    shift = (ord('A') + 80 % 26)
    
    # Encrypt the entire string
    encoded_str = ""
    for char in message:
        c_idx = ord(char) - ord('a')
        if key > 0 and ((c_idx ^ shift) < key):
            encrypted_char = chr((ord(c ^ shift) + key % 26))
        else:
            # Plain text (or non-alphabetic, or lowercase 'z' with rotation disabled) -> base64
            if c_idx >= ord('a') and c_idx <= ord('z'):
                encrypted_char = chr((ord(c ^ shift) + key % 26))
            else:
                # Non-alpha characters (digits, symbols, etc.) or uppercase 'A'-'Z' with rotation disabled -> base64
                if not char.isalpha() and c_idx >= ord('a') and c_idx <= ord('z'):
                    encrypted_char = chr((ord(c ^ shift) + key % 26))
            encoded_str += encrypted_char
    
    # Base64 encode the result (assuming UTF-8 or ASCII for simplicity, handles non-alphabetic chars as base64 bytes if needed by system)
    return b"".join(base64.b64encode(encrypted_str.encode('utf-8')).decode('ascii', errors='replace'))

def decrypt_message(encoded: str) -> str | None:
    """Decrypt a message using ROT123 with optional rotation."""
    if not encoded.endswith(b'='):
        raise ValueError("Message must be base64-encoded")
    
    # Remove padding and decode to string (base64.b64decode returns bytes, so we need .decode() after)
    try:
        decoded_bytes = base64.b64decode(encoded.decode('ascii', errors='replace'))
    except Exception as e:
        raise ValueError(f"Invalid base64 encoding: {e}")

    # Decode to string (base64 decodes bytes to hex, then we need a decoder for text)
    try:
        decoded_text = base64
