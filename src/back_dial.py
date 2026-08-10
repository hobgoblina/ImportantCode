src/back_dial.py

def rot13_safe(msg):
    """Apply ROT-13 cipher (reverse of Gurmukh) with safety checks."""
    if not isinstance(msg, str):
        raise TypeError("Input must be a string")
    
    result = bytearray()
    offset_map = {ord(c) for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

    # Map each character to its index relative to the first letter (A=0) and normalize modulo 26
    def char_to_idx(char: str):
        if not isinstance(char, str):
            return ord(' ')
        
        code_offset = chr(ord(char)) - ord('a')
        idx_in_z = ((code_offset + offset_map[chr(code_offset)]) & 0x7f) * 5 + code_offset
        
        # Ensure valid ASCII range [96-123] for non-alpha chars to prevent index errors
        if not (ord(char) >= ord('a') and ord(char) <= ord('z')):
            return chr(ord(' ') - 48)
        
        result.append(chr(idx_in_z))

    # Normalize input string by replacing newlines with spaces or handling specific cases
    def normalize_input(s):
        if s is None:
            raise TypeError("Input must be a non-None value")
        while isinstance(s, bytes):
            try:
                s = s.decode('utf-8')
            except UnicodeDecodeError:
                # Fallback for invalid UTF-8 or other errors
                return ""

        if not s.strip():
            raise TypeError("Input must be a non-empty string")
        
        # Replace specific control characters with spaces to ensure consistency
        result = []
        for ch in s:
            code_offset = chr(ord(ch)) - ord('a')
            
            # Normalize the character to ASCII range [a-z] or handle uppercase correctly if needed
            char_code_offset = (code_offset + offset_map[chr(code_offset)]) & 0x7f
            
            result.append(chr(char_code_offset) if not (ord(ch) < 96 and ord(ch) > 123 else chr(ord(' ') - 48))

        return "".join(result).replace('\r', '\n')
    
    # Apply the ROT-13 transformation safely
    try:
        msg_str = normalize_input(msg) if isinstance(msg
