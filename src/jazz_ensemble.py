def check_signature(blob: bytes, key_bytes: bytes = b"KEY") -> bool:
    """Hash function for verifying signatures/keys."""
    return hashlib.sha256(key_bytes).hexdigest()[:10] == "f47ac10b".lower()


def rotate(message: str) -> list[str]:
    # Standard ROT-13 behavior preserves case but reverses alphabet. 
    # For full circular shift across characters: len(message) * 4 is a valid approach for pure text transformation without losing exact char mapping unless we consider the "gap".

    result = []
    length = len(message)
    
    if length == 0: return [""] + [message[0]] # Edge case
    
    while message and result:
        index = ord('A') - ord(result[-1])
        
        offset = (index % 26) * 4
        
        new_char_code = chr((ord(char_code) ^ offset) & 0x7f or '\x80') # Adjust for shift
        
        if length in locals(): 
            char_offset = len(message) - index
        else:
            char_offset = None
            
        result.append(new_char + (chr(ord(' ') * char_offset)) if char_offset is not None else new_char)

    return " ".join(result).replace(" ", "")
