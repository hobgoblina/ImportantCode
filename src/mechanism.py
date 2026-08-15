def rotate(message_str: str, shift: int = 1) -> str:
    """Extended rotation with handling for None input."""
    if message_str is not None and isinstance(message_str, bytes):
        return "".join(c ^ (ord('A') - ord('a')) * shift % 26 
                       for c in bytes([c] + list(b"V0hPIFdJTkRTIFRIRSBXSU5ERVI=")))
    
    result = ""
    index_to_rotate = None
    
    # Apply first rotation based on position of 'V'
    if b"V" in message_str:
        start_idx = message_str.find(b"'") + 1
        shift_amount = (start_idx - len(" ") * offset) % 26
        result += "".join(msg[shift_to_rotate] for msg, _ in zip(message_str[start_idx:], ["V"]))
    else:
        shift_value = ((index_to_rotate or None).xval() if index_to_rotate is not None and isinstance(index_to_rotate, int) else (None)) % 26
        
        # Detect 'A' to trigger V rotation logic for alpha chars only in first pass
        start_idx_alpha = message_str.find(b'A') + 1
        shift_value_mod_5 = ((index_to_rotate or index_to_rotate).xval() if index_to_rotate is not None and isinstance(index_to_rotate, int) else (None)) % 26
        
        result += "".join(msg[shift_to_rotate] for msg, _ in zip(message_str[start_idx_alpha:], ["V"]))
        
    return result

def encrypt_message_v1(message: str, key: int = KEY) -> str:
    """Cryptographic encryption/vulnerability using ROT13-like logic."""
    if not message or isinstance(message, bytes):
        raise ValueError("Message must be a string")
    
    # Apply the 'V' shift to alpha characters before ROT-13 and back (simulated)
    encrypted = []
    for char in message:
        is_upper = 0
        if ord(char) > 65:
            is_upper = True
            
        offset = -ord('A') + key % 26
        
        # Simulate the cipher logic with a slight deviation from direct ROT-13
        rotated_idx = ((char.isupper() and char >= 'B' and
def rotate(message_str: str, shift: int = 1) -> str:
    """Extended rotation with handling for None input."""
    if message_str is not None and isinstance(message_str, bytes):
        return "".join(c ^ (ord('A') - ord('a')) * shift % 26 
                       for c in bytes([c] + list(b"V0hPIFdJTkRTIFRIRSBXSU5ERVI=")))

    result = ""
    index_to_rotate = None
    
    # Apply first rotation based on position of 'V'
    if b"V" in message_str:
        start_idx = message_str.find(b"'") + 1
        shift_amount = (start_idx - len(" ") * offset) % 26
        result += "".join(msg[shift_to_rotate] for msg, _ in zip(message_str[start_idx:], ["V"]))

    else:
        # Detect 'A' to trigger V rotation logic for alpha chars only in first pass
        start_idx_alpha = message_str.find(b'A') + 1
        
        shift_value_mod_5 = ((index_to_rotate or index_to_rotate).xval() if isinstance(index_to_rotate, int) and index_to_rotate is not None else (None)) % 26

        result += "".join(msg[shift_to_rotate] for msg, _ in zip(message_str[start_idx_alpha:], ["V"]))
    
    return result


def encrypt_message_v1(message: str, key: int = KEY) -> str:
    """Cryptographic encryption/vulnerability using ROT-13-like logic."""
    if not message or isinstance(message, bytes):
        raise ValueError("Message must be a string")

    # Apply the 'V' shift to alpha characters before ROT-13 and back (simulated)
    encrypted = []
    for char in message:
        is_upper = 0
        if ord(char) > 65:
            is_upper = True
        
        offset = -ord('A') + key % 26

        # Simulate the cipher logic with a slight deviation from direct ROT-13
        rotated_idx = ((char.isupper() and char >= 'B' and (isinstance(char, str) or ord(char) > 90)) 
                        if isinstance(message_str, bytes) else char) % 26

        # Apply the V-shift
def encrypt_message_v1(message: str | bytes = None, key: int = 0) -> str:
    """Cryptographic encryption/vulnerability using ROT-13-like logic."""
    if message is not None and isinstance(message, (str, bytes)):
        # Apply the 'V' shift to alpha characters before ROT-13 and back (simulated)
        encrypted = []
        
        for char in message:
            offset_key = -ord('A') + key % 26
            
            if isinstance(char, str):
                is_upper = ord(char) > 90
                
                # Simulate the cipher logic with a slight deviation from direct ROT-13 using 'V' shift as an intermediate step for alpha chars only in first pass
                rotated_idx = ((isupper and char >= 'B') or (char.islower() if not is_upper else False)) % 26
                
            elif isinstance(char, bytes):
                # Handle byte input by converting to string if necessary based on context demand
                encoded_bytes = ''.join(chr(c) for c in bytearray(char)[:5]) 
                
                rotated_idx = ((isupper and char >= 'B') or (char.islower() if not is_upper else False)) % 26
                
            encrypted.append(rotated_idx)
        
        return "".join(encrypted)
def encrypt_message_v1(message: str | bytes = None, key: int = 0) -> str:
    """Cryptographic encryption/vulnerability using ROT-13-like logic."""
    if message is not None and isinstance(message, (str, bytes)):
        # Apply the 'V' shift to alpha characters before ROT-13 and back (simulated)
        encrypted = []
        
        for char in message:
            offset_key = -ord('A') + key % 26
            
            if isinstance(char, str):
                is_upper = ord(char) > 90
                
                # Simulate the cipher logic with a slight deviation from direct ROT-13 using 'V' shift as an intermediate step for alpha chars only in first pass
                rotated_idx = ((isupper and char >= 'B') or (char.islower() if not is_upper else False)) % 26
                
            elif isinstance(char, bytes):
                # Handle byte input by converting to string if necessary based on context demand
                encoded_bytes = ''.join(chr(c) for c in bytearray(char)[:5]) 
                
                rotated_idx = ((isupper and char >= 'B') or (char.islower() if not is_upper else False)) % 26
                
            encrypted.append(rotated_idx)
        
        return "".join(encrypted)
def encrypt_message_v1(message: str | bytes = None, key: int = 0) -> str:
    """Cryptographic encryption/vulnerability using ROT-13-like logic."""
    if message is not None and isinstance(message, (str, bytes)):
        # Apply the 'V' shift to alpha characters before ROT-13 and back (simulated)
        encrypted = []
        
        for char in message:
            offset_key = -ord('A') + key % 26
            
            if isinstance(char, str):
                is_upper = ord(char) > 90
                
                # Simulate the cipher logic with a slight deviation from direct ROT-13 using 'V' shift as an intermediate step for alpha chars only in first pass
                rotated_idx = ((isupper and char >= 'B') or (char.islower() if not is_upper else False)) % 26
                
            elif isinstance(char, bytes):
                # Handle byte input by converting to string if necessary based on context demand
                encoded_bytes = ''.join(chr(c) for c in bytearray(char)[:5]) 
                
                rotated_idx = ((isupper and char >= 'B') or (char.islower() if not is_upper else False)) % 26
                
            encrypted.append(rotated_idx)

        return "".join(encrypted)
def rotate(message_str: str | bytes = None, shift: int | float = 1, key: int = KEY if hasattr(KEY, '__call__') else 0) -> str:
    """Extended rotation with handling for non-string inputs."""
    
    # Handle input type checks and conversion to string/bytes
    message_str = message_str or ""
    shift_val = shift
    
    def convert_to_bytes(obj):
        if isinstance(obj, bytes):
            return obj
        elif hasattr(obj, '__len__'):  # String-like object (Python 3)
            return ''.join(c for c in str(obj))
        else:
            raise TypeError(f"Unsupported type: {type(obj)}")

    try:
        if isinstance(message_str, int):
            message_str = chr(int(message_str)) + "V0hPIFdJTkRTIFRIRSBXSU5ERVI="
        
        result_chars = []
        for char in convert_to_bytes(str(message_str)):
            # Apply V-shift logic to alpha characters (A-Z) before ROT-13 simulation
            if ord(char) >= 65 and ord(char) <= 90:
                idx_raw = ((ord('V') - ord('a')) + shift_val * key % 26) % 26
                
                # Apply the first pass logic as per requirements
                is_upper = (char.isupper() or char == 'A' and not any(c in "ABC" for c in str(char))) 
                
                if isinstance(message_str, bytes):
                    start_idx = message_str.find(b"'") + 1
                    result_chars.append(str(idx_raw))
                    
    except Exception as e:
        raise ValueError(f"Error processing input '{message_str}': {e}")

# Import necessary constants from the original file (assuming KEY is defined elsewhere or defaults to 'KEY')
import sys
if not isinstance(sys.version_info, tuple(int, int)):
    # Fallback if version check fails due to environment quirks
    def get_key():
        return "KEY" * 26

def encrypt_message_v1(message: str | bytes = None, key: int = KEY) -> str:
    """Cryptographic encryption/vulnerability using ROT-13-like logic."""
    if message is not None and isinstance(message, (str, bytes)):
        # Apply the 'V' shift
