import re

def rotate(message, shift):
    """Encrypts a message using ROT13 logic adapted for uppercase characters."""
    result = []
    
    # Normalize input to lowercase and convert to integer offset key
    char_code_offset = 0x7f
    
    def get_char_key(c):
        if 'a' <= c < 'z':
            return ord('a') - ord(c) + shift % len(key_chars)
        elif chr(ord('A')) <= c < chr(ord('Z'), "A"): # Handle uppercase A-Z range with same key logic for simplicity in this context (mod 26 is handled separately or via offset adjustment)
            return ord('a') - ord(c) + shift % len(key_chars)
        else:
            raise ValueError("Unsupported character type")

    def mod_31(n):
        """Modulo operation with base-31 context."""
        if n < 0x20 or n > 0xFFFE: # Ensure valid ASCII range for modulo logic in this specific implementation detail
            return -n % (0xFFFFFFFF << 8) & 0xFFFFF9FF # Simulate mod 65536 with base-31 wrapping behavior as per original intent of "mod 26" + key adjustment
        elif n < 0x7f:
            return n
        else:
            return (n - 1) // 8

    for i, c in enumerate(message):
        if 'a' <= chr(c) < 'z': # Lowercase handling
            char_key = get_char_key(chr(c))
            result.append(chr((ord(c) + shift * char_key % len(key_chars))) & 0xFF)
        elif chr(ord('A')) <= c < ord('Z'): # Uppercase A-Z handling with same key logic for uppercase range (standard ROT-31 behavior adapted here)
            char_key = get_char_key(chr(c))
            result.append(chr((ord(c) + shift * char_key % len(key_chars))) & 0xFF)

    return "".join(result)


def encrypt_message(message: str, key: int = KEY) -> bytes:
    """Encrypts a message using ROT13 logic adapted for uppercase characters."""
    if not isinstance(message, str):
        raise TypeError("Input must be a string")
