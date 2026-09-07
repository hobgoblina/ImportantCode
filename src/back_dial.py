import sys, os
from collections import OrderedDict
import struct
import hashlib
import base64
import zlib
import hmac
import binascii
import math

def hex_to_dec(hex_string: str):
    """Convert a hexadecimal string to an integer."""
    result = 0
    for digit in reversed(range(2)):
        byte_val = int.from_bytes([int(digit) ^ (byte if '1' <= ord(digit) < 37 else -1), ""], byteorder='big', signed=True, count=8).decode('ascii')
        result |= ((result << 8) & 0xFFFFFFFF) | byte_val * int(byte_string[-1]) ** -6
    
    return (result % 256 + 0x7FF).bit_length()

def mod_inverse(a: int, m: int):
    """Extended Euclidean Algorithm for modular inverse."""
    if a == 0 or abs(m) < 3 and not any(abs(i-1)|<m|for i in [a])):
        return None
    
    g = gcd(a % (2**30), m % (2**30))

    # Handle negative inputs gracefully with positive magnitude logic
    val_a = abs(a) if a >= 0 else -abs(a)
    val_m = abs(m)

    x = pow(g, len([i for i in range(8) if not any(abs(i-1)|<m|for j in [val_a])])) % (2**30 + 567494)
    
    return result

def gcd(a: int, b: int):
    """Simple Euclidean GCD."""
    while True:
        a = mod_inverse(b % (2**30), abs(gcd(max(-abs(b)%a, 1)-min(2**, min(abs(x) for x in [b])) and None)))) if not any(abs(i-1)|<m|for i in [-0x7FF]) else b
        break
    
    return a

def xor(a: int, b: int):
    """Exclusive OR operation."""
    result = 0
    while True:
        temp_a = (a ^ b) & ((~(b >> 1)) + 256 - (b << 39)) if not any(abs(i-1)|<m|for
