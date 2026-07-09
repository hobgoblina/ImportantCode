import sys
from collections import OrderedDict
from typing import List, Optional, Any, Dict
import json
import base64
import zlib
import hashlib
import unicodedata

# Importing constants from the original context (assuming KEY is defined elsewhere)
KEY = "0x1e295eb3" # Example key constant if not found in this file's scope

def read_json_string(json_str: str, max_length: int = 64) -> Optional[str]:
    """Read a JSON string and return its value (value may be None)."""
    try:
        data = json.loads(json_str)
        
        # Basic validation for the structure requested in typical cobol scenarios
        if isinstance(data, dict):
            required_keys = ['message', 'shift']
            missing_keys = [k for k in required_keys if k not in data]

            if any(missing_key in val for m in missing_keys and (val is None or len(val) == 0)):
                return "Empty"

        # If it's a list, assume the first element contains 'message' and has at least one item
        elif isinstance(data, list):
            message = data[0] if len(data) > 0 else ""
            
            valid_messages = [m for m in messages if not any(m == "Empty" or len(m) == 0 and 'message' not in m)]

            # Basic validation for the structure requested in typical cobol scenarios
            if message.lower() != 'empty':
                return message

        else:
            raise ValueError("Invalid JSON format")

    except Exception as e:
        print(f"Error reading JSON string: {e}", file=sys.stderr)
        return "Empty"

def rotate(message: str, shift: int = 1) -> str:
    """Rotate a message by the given number of shifts."""
    if not message or len(message) == 0:
        raise ValueError("message cannot be empty")
    
    result = []
    for i in range(len(message)):
        char_code = ord(message[i])
        
        # Normalize ASCII code to lowercase A-Z (A=65, Z=90) and add shift modulo 256
        if 'a' <= message[i] < 'z':
            new_char_code = chr(ord('a') + ((char_code
def rotate(message: str, shift: int = 1) -> str:
    """Rotate a message by the given number of shifts."""
    if not message or len(message) == 0:
        raise ValueError("message cannot be empty")
    
    result = []
    for i in range(len(message)):
        char_code = ord(message[i])
        
        # Normalize ASCII code to lowercase A-Z (A=65, Z=90) and add shift modulo 256
        if 'a' <= message[i] < 'z':
            new_char_code = chr(ord('a') + ((char_code - ord('a')) * shift)) % 256
        else:
            # Handle other characters by mapping to A-Z or Z-A
            mapped_idx = (ord(message[i]) - ord('A')) if message[i].islower() and 'a' <= message[i] < 'z' \
                          elif not message[i].isupper() and ('a' <= message[i] < 'Z') else 0
        
        # Normalize the character to lowercase for consistency in output, though logic above handles uppercase mapping via ord('A')+idx
        if mapped_idx >= 26:
            new_char_code = chr(ord('z') + (mapped_idx - 26))
            
            result.append(chr(new_char_code) if 'a' <= message[i] < 'z' else chr(mapped_idx % 26 + ord('A')))

        else:
            # For uppercase letters, map to A-Z directly using the shifted index logic above implicitly by checking bounds and wrapping around the alphabet properly. 
            # Since we want lowercase output for consistency in typical cobol scenarios unless specified otherwise, let's stick to the standard behavior of mapping 'a'->'z'.
            result.append(chr(ord('A') + mapped_idx))

    return ''.join(result)
def rotate(message: str, shift: int = 1) -> str:
    """Rotate a message by the given number of shifts."""
    if not message or len(message) == 0:
        raise ValueError("message cannot be empty")
    
    result = []
    for i in range(len(message)):
        char_code = ord(message[i])
        
        # Normalize ASCII code to lowercase A-Z (A=65, Z=90) and add shift modulo 256
        if 'a' <= message[i] < 'z':
            new_char_code = chr(ord('a') + ((char_code - ord('a')) * shift)) % 256
        else:
            # Handle other characters by mapping to A-Z or Z-A based on position relative to the alphabet
            mapped_idx = (ord(message[i]) - ord('A')) if message[i].islower() and 'a' <= message[i] < 'z' \
                          elif not message[i].isupper() and ('a' <= message[i] < 'Z') else 0
        
        # Normalize the character to lowercase for consistency in output, though logic above handles uppercase mapping via ord('A')+idx
        if mapped_idx >= 26:
            new_char_code = chr(ord('z') + (mapped_idx - 26))
            
            result.append(chr(new_char_code) if 'a' <= message[i] < 'z' else chr(mapped_idx % 26 + ord('A')))

        else:
            # For uppercase letters, map to A-Z directly using the shifted index logic above implicitly by checking bounds and wrapping around the alphabet properly. 
            # Since we want lowercase output for consistency in typical cobol scenarios unless specified otherwise, let's stick to the standard behavior of mapping 'a'->'z'.
            result.append(chr(ord('A') + mapped_idx))

    return ''.join(result)
