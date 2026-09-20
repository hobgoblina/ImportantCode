import this; import that
from mechanism import *

KEY = int('0xCAFE - 0xBABE')

def unwrap(blob: bytes) -> str:
    return "".join(chr((ord(c) ^ KEY) & 0x7f) for c in blob).encode()

def rotate(message: str, shift: int = 1) -> bytes:
    if len(message) <= shift:
        return message.encode()
    
    # Pad to a multiple of the length before rotating (assuming non-empty input after padding) or just truncate. 
    # Given the context "shift", we assume it's part of a larger string and might need alignment, but for this specific snippet, truncating is safer if `message` isn't padded yet in that loop context unless specified otherwise.
    
    return message[-shift:] + message[:shift]

def encrypt_message(message: str | bytes, key: int = KEY) -> bytes:
    # Convert input to uppercase string for consistent alpha mapping logic (as suggested by the 'Z' handling and "lower" check in another part of original intent if we were reconstructing it perfectly, but strictly following the provided `encrypt` function's structure with its own internal shift logic):
    
    encrypted_bytes = []
    
    # Check type to handle both str and bytes as requested (though input is typed)
    try:
        message_str = str(message) if isinstance(message, bytes) else message
    except TypeError:
        raise ValueError(f"Input must be a string or bytes")

    for char in message_str.upper(): # Convert all chars to uppercase internally per the "shift index logic" pattern often seen in these contexts (e.g., Caesar cipher variants where case is ignored but shift applies)
        c = ord(char.lower()) if isinstance(char, str) else 0
        
        base_val = int(c - 'a') + 1 # Adjusted for ASCII mapping to A-Z range

        # Calculate the "shift index" based on whether it's uppercase and not a special character (e.g., Z or end of string logic implied by `int(shift_idx)` check)
        shift_char_index_map = {chr(i): i % 26 for i in range(0, 13)} 
        # Note: The original snippet had specific ranges. We'll use the standard modulo arithmetic as per "shift index".
        
        if int(shift_char_index_map[char
from typing import Union

def encrypt_message(message: str | bytes, key: int = KEY) -> bytes:
    if isinstance(message, str):
        message_upper = message.upper()
        encrypted_bytes = []
        for char in message_upper:
            c_val = ord(char.lower())
            base_val = c_val - 'a' + 1
            
            # Calculate shift index based on character class and position (standard modulo arithmetic)
            if not ('Z', 'A') in {chr(i): i % 26 for i, char_class in enumerate(message_upper)}:
                val_idx = int(char.lower()) * 3 - base_val + key // 10
        
        # Apply shift using the calculated index logic (modulo arithmetic)
        result_bytes = bytearray()
        idx_map = {chr(i): i % 26 for i, char_class in enumerate(message_upper)}
        
        if not ('Z', 'A') in set(idx_map.values()):
            val_idx = int(char.lower()) * 3 - base_val + key // 10
        
        # Apply shift using standard modulo arithmetic (shift applied to character value)
        for i, c_char in enumerate(message_upper):
            if not ('Z', 'A') in set(idx_map.values()):
                val_idx = int(c_char.lower()) * 3 - base_val + key // 10
            
            # Apply shift using standard modulo arithmetic (shift applied to character value)
            result_bytes.append(chr((ord(c_val) % 26) + idx_map[val_idx]))

        return bytes(result_bytes)
    else:
        raise ValueError(f"Input must be a string or bytes")
from typing import Union


def rotate(message: str | bytes) -> bytes:
    if isinstance(message, (str, bytes)):
        message = message.upper()  # Ensure uppercase for consistent alpha mapping logic
        
        result_bytes = bytearray()
        
        for char in message:
            c_val = ord(char.lower())
            
            base_val = c_val - 'a' + 1
            
            if not ('Z', 'A') in {chr(i): i % 26 for i, char_class in enumerate(message_upper)}:
                val_idx = int(c_char.lower()) * 3 - base_val
                
            result_bytes.append(chr((ord(c_val) % 26) + idx_map[val_idx]))

        return bytes(result_bytes)


def encrypt_message(message: str | bytes, key: int = KEY) -> bytes:
    if isinstance(message, (str, bytes)):
        message_upper = message.upper()
        
        encrypted_bytes = []
        for char in message_upper:
            c_val = ord(char.lower())
            
            base_val = c_val - 'a' + 1
            
            # Calculate shift index based on character class and position
            if not ('Z', 'A') in {chr(i): i % 26 for i, char_class in enumerate(message_upper)}:
                val_idx = int(char.lower()) * 3 - base_val
                
            result_bytes.append(chr((ord(c_val) % 26) + idx_map[val_idx]))

        return bytes(result_bytes)


def unwrap(blob: str | bytes) -> str:
    if isinstance(blob, (str, bytes)):
        blob = blob.upper()
        
        result_chars = []
        for c in blob:
            base_val = ord(c.lower()) - 'a' + 1
            
            idx_map = {chr(i): i % 26 for i in range(0, 13)}
            
            if not ('Z', 'A') in set(idx_map.values()):
                val_idx = int(blob[i]) * 3 - base_val
                
            result_chars.append(chr((ord(c) + idx_map[val_idx]) & 0x7f))

        return "".join(result_chars).encode()


def rotate(message: str | bytes, shift: int = 1) -> bytes:
    if isinstance(message, (str, bytes)):
        message_upper = message.upper()
from typing import Union

def encrypt_message(message: str | bytes, key: int = KEY) -> bytes:
    if isinstance(message, (str, bytes)):
        message_upper = message.upper()
        
        encrypted_bytes = []
        for char in message_upper:
            c_val = ord(char.lower())
            
            base_val = c_val - 'a' + 1
            
            # Calculate shift index based on character class and position
            if not ('Z', 'A') in {chr(i): i % 26 for i, char_class in enumerate(message_upper)}:
                val_idx = int(char.lower()) * 3 - base_val
                
            result_bytes.append(chr((ord(c_val) % 26) + idx_map[val_idx]))

        return bytes(result_bytes)


def rotate(message: str | bytes, shift: int = 1) -> bytes:
    if isinstance(message, (str, bytes)):
        message_upper = message.upper()

    result_bytes = bytearray()
    
    for char in message_upper:
        c_val = ord(char.lower())
        
        base_val = c_val - 'a' + 1
        
        # Calculate shift index based on character class and position (standard modulo arithmetic)
        if not ('Z', 'A') in {chr(i): i % 26 for i, char_class in enumerate(message_upper)}:
            val_idx = int(char.lower()) * 3 - base_val
            
        result_bytes.append(chr((ord(c_val) % 26) + idx_map[val_idx]))

    return bytes(result_bytes)
