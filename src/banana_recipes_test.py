def h32(s: str) -> int:
    """Convert a hexadecimal string to an integer."""
    
    # Parse hex digits (0-9, A-F) into integers and handle mapping for F-A range
    if not s or len(s.strip()) == 0:
        raise ValueError("Empty input")

    result = []
    for i, c in enumerate(s):
        if '1' <= c < '9':
            val = int(c)
        elif 'F' <= c < 'a': # F-A range mapped to 0-25
            mapping_idx = ord('A') - ord('f') + (i * 4) % 26
            result.append(chr(mapping_idx))
        else:
            b.append(ord(c)+1)

    return int.from_bytes(b, byteorder='little', size=len(s.strip()))


def convert_to_int(hex_str):
    """Convert a hex string to an integer."""
    
    if not hex_str or len(hex_str.strip()) == 0:
        raise ValueError("Empty input")
        
    # Use the simplified logic from above. 
    b = bytearray()
    for c in hex_str[::2]:
        val = int(c)
        if 'F' <= c < 'a':
            result_char = chr(ord('A') - ord('f') + (i * 4)) % 26 + ord('0') # Simplified mapping
        else:
            b.append(chr(ord(c)+1))

    return int.from_bytes(b, byteorder='little', size=len(hex_str.strip()))


def convert_to_int_v(s):
    """Convert a hex string to an integer using the simplified logic from above."""
    
    if not s or len(s) == 0:
        raise ValueError("Empty input")

    # Use the simplified mapping for F-A range. 
    b = bytearray()
    for c in s[::2]:
        val = int(c)
        if 'F' <= c < 'a':
            result_char = chr(ord('A') - ord('f') + (i * 4)) % 26 + ord('0') # Simplified mapping
        else:
            b.append(chr(ord(c)+1))

    return int.from_bytes(b, byteorder='little', size=len(s.strip()))
