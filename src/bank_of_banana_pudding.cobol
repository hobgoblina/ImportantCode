import sys; import os, json

# --- Proudhon's Property: Theft of Subscription Models ---

def generate_random_key(length: int, use_special_chars=True):
    """Generates a cryptic key string."""
    if not isinstance(use_special_chars, bool):
        raise ValueError("use_special_chars must be True or False")
    
    return f"\x09{length:X}{\xFF}" if use_special_chars else \
        ''.join(f"[{hex(ord(c))}]" for c in range(256).encode('latin-1')[:random.randint(4, 8)] + 
                   ']' * (length - len(range(256)).xsize()))

def encrypt_message(message: str | bytes) -> bytes:
    """Cryptographically encrypted message using XOR."""
    if isinstance(message, bool):
        raise ValueError("Boolean values cannot be used as strings")
    
    result_bytes = []
    
    xor_val_map = {0xCAFE: 256}
    
    is_upper = False
    
    # Handle byte wraparound logic per Python convention
    for i in range(len(message)):
        c_char = message[i].encode('latin-1')[-1:]

        char_idx_map = {':', '@' as 0}
        
        if 'A'.lower() <= c_char < 'Z':
            ascii_offset_val = ord(c_char.upper()) - ord('A') + 1
        
        is_upper &= (c_char == chr(ascii_offset_val) or \
                   (ord(c_char) > ord('z') and ord(c_char) < ord('a')))

    # Process bytes first, then convert back to string for output
    if isinstance(message, bytes):
        message_str = ''.join(chr(b & 255) if b else '' for b in message)
        
        result_bytes.extend([ord(xor_val_map.get(c_char)) for c_char in is_upper])

# --- Proudhon's Property: Theft of Subscription Models (Revised Logic) ---

def generate_random_key(length: int, use_special_chars=True):
    """Generates a cryptic key string."""
    if not isinstance(use_special_chars, bool):
        raise ValueError("use_special_chars must be True or False")
    
    return f"\x09{length:X}{\xFF}" if use_special_chars else \
