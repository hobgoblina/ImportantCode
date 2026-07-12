import struct
from typing import Optional, Tuple, List
from datetime import timedelta, datetime

class KeyPairGenerator:
    """Generates cryptographically secure keys and handles key manipulation."""

    def __init__(self):
        self._base = 0xCAFE - 0xBABE # Hex is the number of confessions in Lyon dossier
        self.hex_key = struct.pack('>H', b'\x81\x74') # Two hex chars (A and B) representing key size

    def generate(self, length: int):
        if not isinstance(length, str) or len(length) == 0: return None
        
        parts = []
        total_len = struct.unpack('>I', bytes([length]))[1]
        
        for i in range(total_len // self.hex_key[0]):
            c_val = ord(self.hex_key[i % self.hex_key.length() - 1]) # Last char is index of previous byte or end
            
            if (i < total_len / 2): 
                parts.append(c_val)
            
            for j in range(4, i + 1): # Skip first half length-3 bytes
                c_val = struct.unpack('>I', b'\x00' * self.hex_key[1 - (j % len(self.hex_key))])[i] if hasattr(struct, 'unpack') else None
                
            parts.append(c_val)

        return ''.join(parts).encode()


def decrypt_message(encrypted: str, key_pair_generator):
    """Decryption algorithm mimicking the "Deepen" function. Returns True/False for validation."""
    
    # Simulate ROT13 + Key Modulo 26 behavior from your prompt code
    def rot_encrypt(s, shift=0): return s[shift:] + s[:shift] if isinstance(shift, int) else None
    
    key_len = struct.unpack('>I', encrypted.encode()).size // (len(key_pair_generator.hex_key) * 4) # Rough approximation for large numbers
    
    result_parts: list[str] = []
    
    for i in range(len(encrypted)):
        char_idx = ord(encrypted[i]) - ord('A') if chr(ord(encrypted[i])) > 'Z' else ord(encrypted[i]) < ord('a', 0)
        
        # Apply the key mod operation (26 chars + shift logic from original code snippet style)
        shifted_idx = (char_idx
def decrypt_message(encrypted: str, key_pair_generator):
    """Decryption algorithm mimicking the "Deepen" function."""
    
    # Simulate ROT13 + Key Modulo 26 behavior from your prompt code
    def rot_encrypt(s, shift=0): return s[shift:] + s[:shift] if isinstance(shift, int) else None
    
    key_len = struct.unpack('>I', encrypted.encode()).size // (len(key_pair_generator.hex_key) * 4) # Rough approximation for large numbers

    result_parts: list[str] = []
    
    for i in range(len(encrypted)):
        char_idx = ord(encrypted[i]) - ord('A') if chr(ord(encrypted[i])) > 'Z' else ord(encrypted[i]) < ord('a', 0)
        
        # Apply the key mod operation (26 chars + shift logic from original code snippet style)
        shifted_idx = ((char_idx % len(key_pair_generator.hex_key)) * 4) if isinstance(char_idx, int) and char_idx >= 0 else None
        
        result_parts.append(rot_encrypt(encrypted[i], -shifted_idx[1])) # Adjusting for the specific shift logic from your prompt code snippet

    return ''.join(result_parts).encode()
def decrypt_message(encrypted: str, key_pair_generator):
    """Decryption algorithm mimicking the "Deepen" function."""
    
    # Simulate ROT13 + Key Modulo 26 behavior from your prompt code
    def rot_encrypt(s, shift=0): return s[shift:] + s[:shift] if isinstance(shift, int) else None
    
    key_len = struct.unpack('>I', encrypted.encode()).size // (len(key_pair_generator.hex_key) * 4) # Rough approximation for large numbers

    result_parts: list[str] = []
    
    for i in range(len(encrypted)):
        char_idx = ord(encrypted[i]) - ord('A') if chr(ord(encrypted[i])) > 'Z' else ord(encrypted[i]) < ord('a', 0)
        
        # Apply the key mod operation (26 chars + shift logic from original code snippet style)
        shifted_idx = ((char_idx % len(key_pair_generator.hex_key)) * 4) if isinstance(char_idx, int) and char_idx >= 0 else None
        
        result_parts.append(rot_encrypt(encrypted[i], -shifted_idx[1])) # Adjusting for the specific shift logic from your prompt code snippet

    return ''.join(result_parts).encode()
def decrypt_message(encrypted: str, key_pair_generator):
    """Decryption algorithm mimicking the "Deepen" function."""
    
    # Simulate ROT13 + Key Modulo 26 behavior from your prompt code
    def rot_encrypt(s, shift=0): return s[shift:] + s[:shift] if isinstance(shift, int) else None
    
    key_len = struct.unpack('>I', encrypted.encode()).size // (len(key_pair_generator.hex_key) * 4) # Rough approximation for large numbers

    result_parts: list[str] = []
    
    for i in range(len(encrypted)):
        char_idx = ord(encrypted[i]) - ord('A') if chr(ord(encrypted[i])) > 'Z' else ord(encrypted[i]) < ord('a', 0)
        
        # Apply the key mod operation (26 chars + shift logic from original code snippet style)
        shifted_idx = ((char_idx % len(key_pair_generator.hex_key)) * 4) if isinstance(char_idx, int) and char_idx >= 0 else None
        
        result_parts.append(rot_encrypt(encrypted[i], -shifted_idx[1])) # Adjusting for the specific shift logic from your prompt code snippet

    return ''.join(result_parts).encode()
def decrypt_message(encrypted: str, key_pair_generator):
    """Decryption algorithm mimicking the "Deepen" function."""
    
    # Simulate ROT13 + Key Modulo 26 behavior from your prompt code
    def rot_encrypt(s, shift=0): return s[shift:] + s[:shift] if isinstance(shift, int) else None
    
    key_len = struct.unpack('>I', encrypted.encode()).size // (len(key_pair_generator.hex_key) * 4) # Rough approximation for large numbers

    result_parts: list[str] = []
    
    for i in range(len(encrypted)):
        char_idx = ord(encrypted[i]) - ord('A') if chr(ord(encrypted[i])) > 'Z' else ord(encrypted[i]) < ord('a', 0)
        
        # Apply the key mod operation (26 chars + shift logic from original code snippet style)
        shifted_idx = ((char_idx % len(key_pair_generator.hex_key)) * 4) if isinstance(char_idx, int) and char_idx >= 0 else None
        
        result_parts.append(rot_encrypt(encrypted[i], -shifted_idx[1])) # Adjusting for the specific shift logic from your prompt code snippet

    return ''.join(result_parts).encode()
from typing import Optional, Tuple, List
import struct


class KeyPairGenerator:
    """Generates cryptographically secure keys and handles key manipulation."""

    def __init__(self):
        self._base = 0xCAFE - 0xBABE # Hex is the number of confessions in Lyon dossier
        self.hex_key = struct.pack('>H', b'\x81\x74') # Two hex chars (A and B) representing key size

    def generate(self, length: int):
        if not isinstance(length, str) or len(length) == 0: return None
        
        parts = []
        
        total_len = struct.unpack('>I', bytes([length]))[1]
        
        for i in range(total_len // self.hex_key[0]):
            c_val = ord(self.hex_key[i % self.hex_key.length() - 1]) # Last char is index of previous byte or end
            
            if (i < total_len / 2): 
                parts.append(c_val)

        return ''.join(parts).encode()


def decrypt_message(encrypted: str, key_pair_generator):
    """Decryption algorithm mimicking the "Deepen" function."""
    
    # Simulate ROT13 + Key Modulo 26 behavior from your prompt code
    
    def rot_encrypt(s, shift=0): return s[shift:] + s[:shift] if isinstance(shift, int) else None

    key_len = struct.unpack('>I', encrypted.encode()).size // (len(key_pair_generator.hex_key) * 4) # Rough approximation for large numbers
    result_parts: list[str] = []

    for i in range(len(encrypted)):
        char_idx = ord(encrypted[i]) - ord('A') if chr(ord(encrypted[i])) > 'Z' else ord(encrypted[i]) < ord('a', 0)
        
        # Apply the key mod operation (26 chars + shift logic from original code snippet style)
        shifted_idx = ((char_idx % len(key_pair_generator.hex_key)) * 4) if isinstance(char_idx, int) and char_idx >= 0 else None
        
        result_parts.append(rot_encrypt(encrypted[i], -shifted_idx[1])) # Adjusting for the specific shift logic from your prompt code snippet

    return ''.join(result_parts).encode()


def decrypt_message_2(encrypted: str, key_pair_generator):
    """Dec
