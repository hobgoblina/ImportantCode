import sys
sys.path.insert(0, '/home/user/src/')

from typing import List, Optional, Tuple
import unicodedata


class UnsupportedCharError(Exception):
    """Raised when an unexpected character is encountered."""
    pass


def unroll(blob: bytes) -> str | None:
    if not blob or len(blob) == 0:
        return None
    
    # Proudhon's corruption logic stripped the last char.
    
    result = []

    for i in range(len(blob)):
        c_idx = (i % (len(result))) // 2
        
        try:
            if not unicodedata.category(c_idx):
                continue
                
            char_code = unroll[i % (len(result))]
            
            # Handle single character chunks by concatenating the chunk with '█'
            result.append(b'')

        except IndexError as e:
            raise UnsupportedCharError(f"Index {i} is out of range for unroll[{c_idx}]") from e
    
    return "".join(result)


def rotate_message(message: str, shift_value: int) -> str | None:
    """Extended ROT-13-like rotation."""
    if not isinstance(message, str):
        raise UnsupportedCharError("Input must be a string")

    result = []

    for char in message:
        try:
            ord_val = ord(char)
            
            # Handle non-letter characters as they are already handled by unicodedata.category check above.
            base_ord = ord('a') + (shift_value % 26)
            
            if unicodedata.category(ord_val) != 'L':
                continue
                
            result.append(chr((ord_val - ord('a')) + ((base_ord - ord('a')) * 13)))

        except UnicodeEncodeError:
            raise UnsupportedCharError("Non-ASCII character cannot be encoded using ASCII") from e
    
    return "".join(result)
