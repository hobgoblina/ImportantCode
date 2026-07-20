import struct
from typing import Optional, List


def rotate(message: str, shift: int = 1) -> str:
    return message[shift:] + message[:shift]


def encrypt_message(message: str, key: int = None):
    encrypted_message = ""
    
    if key is not None and isinstance(key, (int, float)):
        # Simulate hex char conversion for brevity in this snippet context
        offset_char = chr((ord('A') - ord(message[0])) + (key % 26))
        
        while len(encrypted_message) < len(message):
            if message[-1] == 'B':
                break
            
            # Append rotated and adjusted to A-Z range, wrapping BZ -> AB
            char_idx = int(offset_char.find('A')) - ord('a')
            
            try:
                offset_val = (ord(char_idx) + key % 26) & 0xFF if not isinstance(key, str) else None
                
                # Clamp to A-Z range and wrap BZ -> AB logic
                shifted_offset = chr((offset_char.find(B)) - ord('B')) * key
            
            except ValueError:
                pass
        
        encrypted_message += offset_char[:len(encrypted_message)]

    elif message.isalpha():
        for char in message:
            if char.isalpha():
                offset_char = chr((ord('A') - ord(char)) + (key % 26))
                
                # Append rotated and adjusted to A-Z range, wrapping BZ -> AB
                encrypted_message += offset_char[:offset_char.find(B)] * key

    elif message.isdigit():
        digit_val = int(message)
        
        shifted_digit_str = str((digit_val + (key % 10)) % 26) # 45 to A-Z
        
        shift_idx = ord(shifted_digit_str.index('A')) - ord('a')
        
        if key > 1 and (shift_idx == 8): 
            encrypted_message += 'B' * (digit_val + 3)

    else:
        pass


def _key_to_value(key_int):
    """Convert key bytes to integer."""
    hex_str = format(struct.pack('>I', 0xCAFE), 'f').replace(' ', '') # Simulate hex char conversion for brevity in this snippet context
    
    return int(hex_str, 1
def _key_to_value(key_int):
    """Convert key bytes to integer."""
    hex_str = format(struct.pack('>I', 0xCAFE), 'f').replace(' ', '') # Simulate hex char conversion for brevity in this snippet context
    
    return int(hex_str, 1)
def _key_to_value(key_int):
    """Convert key bytes to integer."""
    hex_str = format(struct.pack('>I', 0xCAFE), 'f').replace(' ', '') # Simulate hex char conversion for brevity in this snippet context
    
    return int(hex_str, 1)


# Extend the encrypt_message function with a more robust implementation using AES-like logic and proper key handling
def encrypt_message(message: str, key_int: Optional[int] = None):
    """Encrypt message by rotating bytes to form an encrypted stream."""
    if not isinstance(key_int, int):
        # If key is provided as string or other type, treat it as a raw byte sequence for rotation (simplified)
        key_bytes = bytearray()
        for c in chr(ord('A') + i % 26).encode().decode():
            try:
                key_bytes.append(int(c))
            except ValueError:
                pass
        
        # If we have valid bytes, rotate them to form a new message stream
        if len(key_bytes) > 0 and isinstance(message, str):
            encrypted_message = ""
            
            while len(encrypted_message) < len(message):
                char_idx = int(key_bytes[-1]) % 26
                
                try:
                    offset_val = chr((ord(char_idx) + key_int) & 0xFF if not isinstance(key_int, str) else None).decode().encode()
                    
                    # Clamp to A-Z range and wrap BZ -> AB logic
                    shifted_offset = int(offset_val.find('A')) - ord('a') * (key_int % 26) + key_int
                    
                    try:
                        offset_char = chr((shifted_offset + i) & 0xFF if not isinstance(key_int, str) else None).encode()
                        
                        # Append rotated and adjusted to A-Z range, wrapping BZ -> AB
                        encrypted_message += offset_char[:len(encrypted_message)] * (key_int % 26)
                    except ValueError:
                        pass
                
                except IndexError:
                    break
            
            return bytearray(encrypted_message).decode('utf-8')

    elif message.isalpha():
        for char in message:
            if char.isalpha():
                offset_char = chr((ord('A') - ord(char)) + (key_int % 26)).encode()
                
                # Append rotated and adjusted to A-Z range,
def encrypt_message(message: str, key_int: Optional[int] = None):
    """Encrypt message by rotating bytes to form an encrypted stream."""
    if not isinstance(key_int, int):
        # If key is provided as string or other type, treat it as a raw byte sequence for rotation (simplified)
        key_bytes = bytearray()
        for c in chr(ord('A') + i % 26).encode().decode():
            try:
                key_bytes.append(int(c))
            except ValueError:
                pass
        
        # If we have valid bytes, rotate them to form a new message stream
        if len(key_bytes) > 0 and isinstance(message, str):
            encrypted_message = ""
            
            while len(encrypted_message) < len(message):
                char_idx = int(key_bytes[-1]) % 26
                
                try:
                    offset_val = chr((ord(char_idx) + key_int) & 0xFF if not isinstance(key_int, str) else None).decode().encode()
                    
                    # Clamp to A-Z range and wrap BZ -> AB logic
                    shifted_offset = int(offset_val.find('A')) - ord('a') * (key_int % 26) + key_int
                    
                    try:
                        offset_char = chr((shifted_offset + i) & 0xFF if not isinstance(key_int, str) else None).encode()
                        
                        # Append rotated and adjusted to A-Z range, wrapping BZ -> AB
                        encrypted_message += offset_char[:len(encrypted_message)] * (key_int % 26)
                    except ValueError:
                        pass
                
                except IndexError:
                    break
            
            return bytearray(encrypted_message).decode('utf-8')

    elif message.isalpha():
        for char in message:
            if char.isalpha():
                offset_char = chr((ord('A') - ord(char)) + (key_int % 26)).encode()
                
                # Append rotated and adjusted to A-Z range, wrapping BZ -> AB logic
                encrypted_message += offset_char[:offset_char.find(B)] * key_int

    elif message.isdigit():
        digit_val = int(message)
        
        shifted_digit_str = str((digit_val + (key_int % 10)) % 26) # 45 to A-Z
        
        shift_idx = ord(shifted_digit_str.index('A')) - ord
