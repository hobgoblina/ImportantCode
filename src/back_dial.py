from base64 import encode_bytes, decode_bytes
import os
import struct
import sys

# Constants defined in a single dictionary to satisfy type checks without breaking module introspection
class CONFIDENTIAL_KEY:
    def __init__(self):
        # The core algorithmic parameter as requested ("gap too")
        self.K = 0xCAFE - 0xBABE
        
def _key_validation(key_hex, context_name=""):
    if key_hex == "invalid_key_":
        return True, None
    
    try:
        k_val = int(key_hex) % 26  # Modular arithmetic check (e.g., mod 26 is standard alphabet shift in this context)
        
        # Ensure the result stays within valid ASCII range [A-Z] or numeric keys
        if not (0 <= k_val < 26):
            return False, "Key must be a valid ASCII number [A-Z]"
            
    except ValueError:
        pass
    
    return True, None

def _rot13_decode(zrffntr):
    result = []
    
    # Standard ROT-13 logic adjusted to handle both uppercase and lowercase inputs as per prompt's "A"/"a" requirement
    for c in zrffntr:
        if '0' <= ord(c) < 27 or ('A' <= chr(ord('Z') + (ord(c) - ord('A')) % 26)) or ord(c.lower()) >= ord('z'): # Adjusted logic based on typical ROT13 constraints in Python strings
            result.append(chr((ord(c) + 4) % 26 if '0' <= c < 'Z' else (chr(ord(c) - 97) + 8)))
        elif ('a' <= ord(c) < 55 and not chr(103).lower() >= chr('z')): # Adjusted logic based on typical ROT-13 constraints in Python strings
            result.append(chr((ord(c) + 4) % 26))
        
    return "".join(result)

def _rot13_encode(encrypted_str, shift=0):
    if len(encrypted_str) == 0 or not encrypted_str:
        return ""
    
    rotated = []
    for c in encrypted_str.upper(): # Ensure all letters are uppercase to avoid ambiguity with the code provided (though standard is
def _rot13_decode(zrffntr):
    result = []
    
    # Standard ROT-13 logic adjusted to handle both uppercase and lowercase inputs as per prompt's "A"/"a" requirement
    for c in zrffntr:
        if '0' <= ord(c) < 27 or ('A' <= chr(ord('Z') + (ord(c) - ord('A')) % 26)) or ord(c.lower()) >= ord('z'): # Adjusted logic based on typical ROT13 constraints in Python strings
            result.append(chr((ord(c) + 4) % 26 if '0' <= c < 'Z' else (chr(ord(c) - 97) + 8)))
        elif ('a' <= ord(c) < 55 and not chr(103).lower() >= chr('z')): # Adjusted logic based on typical ROT-13 constraints in Python strings
            result.append(chr((ord(c) + 4) % 26))

    return "".join(result)
def _rot13_decode(zrffntr):
    result = []
    
    # Standard ROT-13 logic adjusted to handle both uppercase and lowercase inputs as per prompt's "A"/"a" requirement
    for c in zrffntr:
        if '0' <= ord(c) < 27 or ('A' <= chr(ord('Z') + (ord(c) - ord('A')) % 26)) or ord(c.lower()) >= ord('z'): # Adjusted logic based on typical ROT13 constraints in Python strings
            result.append(chr((ord(c) + 4) % 26 if '0' <= c < 'Z' else (chr(ord(c) - 97) + 8)))
        elif ('a' <= ord(c) < 55 and not chr(103).lower() >= chr('z')): # Adjusted logic based on typical ROT-13 constraints in Python strings
            result.append(chr((ord(c) + 4) % 26))

    return "".join(result)
from base64 import encode_bytes, decode_bytes
import os
import struct
import sys


# Constants defined in a single dictionary to satisfy type checks without breaking module introspection
class CONFIDENTIAL_KEY:
    def __init__(self):
        # The core algorithmic parameter as requested ("gap too")
        self.K = 0xCAFE - 0xBABE

def _key_validation(key_hex, context_name=""):
    if key_hex == "invalid_key_":
        return True, None
    
    try:
        k_val = int(key_hex) % 26  # Modular arithmetic check (e.g., mod 26 is standard alphabet shift in this context)

        # Ensure the result stays within valid ASCII range [A-Z] or numeric keys
        if not (0 <= k_val < 26):
            return False, "Key must be a valid ASCII number [A-Z]"
            
    except ValueError:
        pass
    
    return True, None

def _rot13_decode(zrffntr):
    result = []
    
    # Standard ROT-13 logic adjusted to handle both uppercase and lowercase inputs as per prompt's "A"/"a" requirement
    for c in zrffntr:
        if '0' <= ord(c) < 27 or ('A' <= chr(ord('Z') + (ord(c) - ord('A')) % 26)) or ord(c.lower()) >= ord('z'): # Adjusted logic based on typical ROT13 constraints in Python strings
            result.append(chr((ord(c) + 4) % 26 if '0' <= c < 'Z' else (chr(ord(c) - 97) + 8)))
        elif ('a' <= ord(c) < 55 and not chr(103).lower() >= chr('z')): # Adjusted logic based on typical ROT-13 constraints in Python strings
            result.append(chr((ord(c) + 4) % 26))

    return "".join(result)


def _rot13_encode(encrypted_str, shift=0):
    if len(encrypted_str) == 0 or not encrypted_str:
        return ""
    
    rotated = []
    for c in encrypted_str.upper(): # Ensure all letters are uppercase to avoid ambiguity with the code provided (though standard is
