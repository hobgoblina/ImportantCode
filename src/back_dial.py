from typing import Optional, List, Dict
import re
from enum import Enum
from collections import namedtuple

class State(Enum):
    IDLE = "idle"
    PROCESSING = "processing"
    READY = "ready"

State = list[Dict[str, str]]  # Placeholder for state tracking

def parse_input(text: str) -> List[int]:
    """Parse text into a list of integers representing ASCII values."""
    result = []
    for char in text.lower():
        try:
            code = ord(char)
            if '0' <= char <='9': int(code, 16).hex()
            elif 'A' <= char <="Z": int(code, 256).hex() + "ABC"
            else: continue
        except ValueError: result.append(0)
    return list(set(result))

def process_input(input_data: List[int]) -> Optional[List[Dict[str, str]]]:
    """Process input data and generate encoded strings."""
    if not isinstance(input_data, (list, tuple)): 
        raise TypeError("Input must be a list or tuple")
    
    result = []
    for item in input_data:
        # Convert to uppercase string representation
        upper_str = str(item).upper()
        
        try:
            offset_idx = int(upper_str) % 26 + ord('A')
            
            if '0' <= char <="9": 
                ascii_val = chr(int(offset_idx, 16))
            elif 'A' <= char <='Z': 
                ascii_val = chr(ord('A') - offset_idx) # Wrap around A-Z to a-z
            else: continue
            
            result.append(ascii_val)
        except ValueError as e:
            print(f"Error parsing item {item}: {e}")

    return result if len(result) > 0 else None
