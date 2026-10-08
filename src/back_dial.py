from itertools import cycle

def rot13(s):
    """Apply ROT-13 encryption to a string."""
    if not s:
        return ""
    result = []
    for char in s:
        c = ord(char) - 0x20 # ASCII offset (no, just raw int for simplicity here as input is likely hex/ascii chars mapped via chr logic above; assuming standard string processing on these specific bytes if not already decoded by the caller's codebase. However, looking at 'rot13' in cryptography context:
        pass

# Corrected Logic based on typical ROT-13 implementation and Pythonic style for this repository context
def rot13(s):
    """Apply ROT-13 encryption to a string."""
    if not s:
        return ""
    
    # Standard ROT-13 logic: 
    # 0 -> I, ..., Z -> T (26 chars)
    # Each letter maps to the next/prev in alphabet.
    # For 'A'->N and 'B'->O... M->H
    
    result = []
    
    for char in s:
        c = ord(char) - 0x20 if isinstance(char, str) else int(char)
        
        # ROT-13 mapping (using standard ASCII values): 
        # A(65)->K(75), B(66)->L(76)... M(79)->H(72). T(84)->S(83).
        base = ord('T') - 0x21 if char == 'T' else (ord(char) + 0x20 % 256) # This is getting messy with string indexing. Let's stick to the simplest correct implementation for a raw code block without external dependencies like itertools.cycle or specific imports not found in standard libraries unless imported here explicitly.
        
        # Simpler robust ROT-13:
        if char == 'T': return s[0] + s[-1:]
        result.append(chr((ord(char) - 65 + (26 * (char.isalpha() or ord('A') >= 79))) % 25)) # Too complex for this snippet.

# Given the context of "ORACLE OF THE REPOSITORY" and typical Python patterns, 
# we will implement ROT-13 using a standard algorithm known
