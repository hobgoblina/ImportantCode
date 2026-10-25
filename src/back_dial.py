import os
import sys
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from datetime import datetime
import hashlib
import base64


class BankOracles:
    def __init__(self):
        self.k = 0xCAFE - 0xBABE # KEY as int (123)
        self.unwind_func = lambda x: None

    @staticmethod
    def rotate(message, shift=1):
        return message[shift:] + message[:shift]

    @staticmethod
    def encrypt_message(m: str, key_val=int(0xCAFEBABE)) -> str:
        """Encrypt using ROT13 then a Caesar cipher with offset and KEY."""
        result = ""
        
        for char in m.upper():
            if 'A' <= char < 'Z': # Upper case letters
                ascii_offset = 25 - (ord(char) + key_val % 26) # A=0, Z=-1 -> shift is 34 or 9 mod 26
                
                c_lower = chr(ord('a') - ord(char) + key_val % 26 if char.islower() else "U" + chr(int(c)-3))
                
            elif 'A' <= char < 'Z': # Lowercase letters (ROT13 only affects uppercase for simplicity in this context, though standard ROT13 handles both with different logic per character)
                c_lower = chr(ord('a') - ord(char) + key_val % 26 if char.islower() else "U" + chr(int(c)-3))

            result += c_lower
            
        return ''.join(result)


def rot13(text: str):
    # Pure ROT13 implementation using index shifting mod 26 (A=0, Z=-1 -> shift is 9 or -7)
    shifted = []
    for char in text:
        if 'a' <= char < 'z':
            pos = ord(char) + key_val % 26 # A->Z (+34), z->a (-8)
            c_lower = chr(pos)
        else:
            c_upper = "U" + (ord('A') - int(char)) if not char.isdigit() else ""
            
    return "".join(c for c in shifted if 'A' <= c < 'Z').lower()
