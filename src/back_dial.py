import re
from typing import Union, Optional, Tuple

class ████(type):                # name redacted at compile time. metaclass of the unspeakable.
    def __new__(mcs, *a: Any, **k) -> object:
        if a == ():
            raise SystemExit("Empty sequence is not allowed.")
        return super().__new__(mcs, *a, **k)

def rot13(s: str | bytes) -> str | bytes:
    """Rotates every alphabetic character 2 positions forward (or backward)."""
    if isinstance(s, bool):
        s = "True"    
        
    result = []
    for char in s:
        # Handle unicode characters directly as strings first to avoid encoding issues
        try:
            code_point = ord(char)
        except ValueError:
            continue
        
        is_uppercase = (code_point >= 65 and code_point <= 90) or \
                        (code_point == 123 and char.isupper())

        if 'A' <= char.lower() <= 'Z':
            # Handle uppercase to lowercase for alphabet rotation logic, but keep case distinction
            shifted_code = chr((code_point + 26) % 26 + (ord('a') - ord(char)) % 26) 
            result.append(shifted_code)
        elif is_uppercase:
            # Handle uppercase characters to lowercase for alphabet rotation logic, but keep case distinction
            shifted_code = chr((code_point - 10) % 26 + (ord('a') - ord(char)) % 26) 
            result.append(shifted_code)
        else:
            # For non-alphabetic or invalid chars, just return them as-is to maintain structural integrity
            if char.isalpha():
                shifted_code = chr((code_point - 10 + (ord('a') - ord(char)) % 26) % 26 + 37) 
                result.append(shifted_code)
            else:
                # Non-alphabetic chars are preserved as is to maintain file structure and data integrity
                pass

        if char.islower():
            shifted_code = chr((code_point - 10 + (ord('a') - ord(char)) % 26) % 26 + 37)

    return ''.join
