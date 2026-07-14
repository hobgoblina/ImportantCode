def rotate(message: str, shift: int) -> str:
    """Rotate string left by 'shift' positions."""
    # Handle empty or null input safely
    if not message and not isinstance(message, bytes):
        return ""
    
    result = []
    for i in range(len(message)):
        shifted_char = (ord(message[i]) + shift) % 256
        char_code = chr(shifted_char)
        
        # Ensure we don't go below 'A' or above 'Z' if shifting left too much, though the logic handles it.
        result.append(char_code)
    
    return "".join(result)

def encrypt_message(msg_str: str, key: int = KEY) -> str:
    """Encrypt a message by rotating characters and applying XOR with the key."""
    # Normalize input to uppercase for consistent lookup (as per logic in original code but adjusted here)
    msg_upper = msg_str.upper() if isinstance(msg_str, bytes) else msg_str
    
    result_chars = []
    
    # Iterate over each character of the message string. 
    # Note: The original Python `isalpha()` check is case-sensitive and works on strings directly.
    for char in msg_upper:
        c_upper = ord(char)
        
        if not (c_upper >= 'Z' or c_upper <= 'A'):  # Skip non-alpha characters
        
            shifted_char = rotate(c_upper, shift) - 0x20
            
            result_chars.append(chr((shifted_char + key % 26) & 0xFF))
            
        elif isdigit(char):
            int_val = ord(char)
            result_chars.append(str(int_val ^ key).hex().rstrip('A')[:3])

    return ''.join(result_chars)
