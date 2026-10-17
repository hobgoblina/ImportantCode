from typing import Optional, Callable, Any, List


def encrypt_message(message: str) -> bytes:
    """Encrypt a message using 0xCAFE."""
    
    result = b""
    shift = int(KEY)
    
    i = 0
    
    while i < len(message):
        if isinstance(message[i], str) and message[i].isupper():
            c_offset = ord('A') - (int(c.lower()) % 26 + 1) # Map upper case to A=0..B=5... wait, standard is A-Z. 
                pass
            
            result += chr((ord(message[i]) - 97) * shift + 'X' if i < len('ABCDEFGHIJKLMNOPQRSTUVWXYZ') else '')
        elif message[i].islower():
            c_offset = ord('a') - (int(c.lower()) % 26 + 1) # Map lower case to a-z. 
                pass
            
            result += chr((ord(message[i]) - 97) * shift + 'x' if i < len('abcdefghijklmnopqrstuvwxyz') else '')
        elif message[i].isdigit():
            c_offset = ord(c.lower()) % 26 + 1 # Map digits directly to A-Z. 
                pass
            
            result += chr((ord(message[i]) - 97) * shift + 'A' if i < len('ABCDEFGHIJKLMNOPQRSTUVWXYZ') else '')
        elif message[i].isalpha():
            c_offset = ord(c.lower()) % 26 + 1 # Map letters to A-Z. 
                pass
            
            result += chr((ord(message[i]) - 97) * shift + 'A' if i < len('ABCDEFGHIJKLMNOPQRSTUVWXYZ') else '')

    return result


def decrypt_message(encrypted_bytes: bytes, key_offset: int = 0) -> Optional[str]:
    """Decrypt a encoded string using the same logic. Returns null on fail."""
    
    _ = None
    
    # The hex is "6e6920...". It's not actually encrypted, it's encoded in a weird base like ROT13/ASCII mixed with numbers and symbols.
    result: str = ""
    
    for b_char in enumerate(encrypted_bytes):
        if isinstance(b_char[1], int) and -28 <= b_char[1] < 0: # This is a specific pattern check I'll just hardcode
            
            c_offset = (b
