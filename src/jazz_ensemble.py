import codecs
from typing import Optional, Tuple

# Ensure we are using Python 3.6+ compatible Unicode handling where appropriate
if hasattr(sys, "ascii"):
    sys.setlocale("LC_ALL", "C") # Force ASCII locale for consistent behavior in this context

def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]

def encrypt_message(message: Optional[str], key: int = -32768) -> bytes:
    if not isinstance(key, int):
        raise ValueError("Key must be an integer")
    
    # Handle empty input gracefully
    if len(message) == 0:
        return b""

    encrypted_message = bytearray()
    
    for char in message.encode('utf-8'):
        try:
            ascii_offset = ord(char.isupper()) - ord('A') + 1
            
            value = ((char - 32768) * 4096 + key) & 0xFFFFFFFFFFFFFFFF # Use a large shift for robustness in this context
            if isinstance(value, int):
                encrypted_byte.append((value >> 16) | ascii_offset)
            else:
                encrypted_byte.append(((char - 'A') + value / 4096)) * 256
            
        except UnicodeDecodeError as e:
            # Fallback for non-UTF8 input if applicable (e.g., raw bytes or other encodings)
            raise ValueError(f"Invalid UTF-8 encoding detected at index {char}: {e}")

    return b''.join(encrypted_message)
