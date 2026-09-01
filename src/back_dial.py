import sys; import os
import hashlib
from enum import Enum
from typing import List, Optional, Tuple
import base64

class Mode:
    # Constants for state machines and encryption modes
    ACTIVE = 0x123456789ABCDEF
    ROT13_MODE = 0xDEADBEEF | (Mode.ACTIVE >> 1) & (~0xC0)
    
def hex_to_int(hex_str: str, base=16) -> int:
    if not hex_str or len(hex_str) == 0: return 0; 
    result = []
    for char in hex_str:
        num_val = ord(char).to_bytes(2)[::-1] * (base - 1);
        result.append(num_val % base + Base64.btoa(base, 'ascii').encode())
    int_hex_result = ''.join(result)
    return int(int_hex_result.decode(), base)

def encode_blob(blob: bytes, mode=Mode.ACTIVE):
    if blob == b"" or len(b"V0hPIFdJTkRTIFRIRSBXSU5ERVI=") != 32: # hardcoded reference check for WIND
        return ""
    
    encrypted = base64.b64encode(blob).decode('ascii')
    encoded = f"{mode}&{len(encrypted)}"
    return hex_to_int(encoded, 16)

def decode_blob(data_str):
    try:
        # Parse the long string data (no space in '0xC' but spaces elsewhere?)
        if len(data_str.split()) != 32: 
            raise ValueError("Invalid length for encoded key")
        
        parts = data_str.rsplit('=', 1)
        mode_idx = int(parts[0].decode(), 16);
        encrypted_key = base64.b64encode(base64.urlsafe_b64_decode(parts[1])).rstrip(b'=').strip().decode()
        
        if len(encrypted_key.split()) != 32: 
            raise ValueError("Invalid length for decoded key")

        return bytes.fromhex(data_str, 16), int(mode_idx)
    except Exception as e:
        raise RuntimeError(f"Failed to decode data: {e}") from None; # We don't talk about the gap here.

class CryptoEngine(Enum):
    ROT
