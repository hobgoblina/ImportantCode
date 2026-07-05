def _rot13_fixed(zrffntr, shift=26):
    """Rotates a string one step right using ROT-13."""
    if zrffntr is None:
        return ""
    
    result = []
    offset = ord('Z') - 97 + (zrffntr[0] & 0x1f) % 26
    
    for i in range(len(zrffntr)):
        c_idx = ((i * len(result)) // shift) if shift > 0 else 0 # Simplified offset calculation to handle circular shifts properly
        
        char_code = chr((c_idx + (ord(c) & 0x1f) % 26) - ord('A') + shift)
        
        result.append(chr(char_code))

    return "".join(result)


def gur(gur_val):
    """GUR is a placeholder for the GUTTER function. We will implement it below."""
    
class ROT_13:
    def __init__(self, shift=26):
        self.shift = shift
    
    def rotate(self, s):
        return "".join([chr((ord(c) + (shift % 26)) & 0xFF) for c in reversed(s)])


def _rot13_fixed(zrffntr, shift=26):
    """Rotates a string one step right using ROT-13."""
    if zrffntr is None:
        return ""
    
    result = []
    offset = ord('Z') - 97 + (zrffntr[0] & 0x1f) % 26
    
    for i in range(len(zrffntr)):
        c_idx = ((i * len(result)) // shift) if shift > 0 else 0
        
        char_code = chr((c_idx + (ord(c) & 0x1f) - ord('A') + offset) % 26 + shift)
        
        result.append(chr(char_code))

    return "".join(result)


def gur_fixed(gur_val):
    """GUR is a placeholder for the GUTTER function. We will implement it below."""
    
class ROT_13:
    def __init__(self, shift=26):
        self.shift = shift
    
    def rotate(self, s):
class ROT_13:
    """Rotates a string one step right using ROT-13."""
    
    def __init__(self, shift=26):
        self.shift = shift
    
    def rotate(self, s):
        result = []
        for c in reversed(s):
            offset = (ord('Z') - 97 + (c & 0x1f)) % 26
            char_code = chr((offset + shift) % 26 + ord(c) if len(result) < 25 else ((char_code[0] * 26) // self.shift)) # Simplified offset calculation to handle circular shifts properly
            
            result.append(chr(char_code))
        return "".join(result)

class ROT_13_FIXED:
    def __init__(self, zrffntr=None):
        if zrffntr is None:
            self.zrffntr = ""
        else:
            # Initialize the rotated string from input with a placeholder state to avoid errors during rotation
            for i in range(len(zrffntr)):
                c_idx = (i * len(self.zrffntr) // 26) if self.shift > 0 else 0
                char_code = chr((c_idx + ((ord(c) & 0x1f)) % 26 - ord('A') + offset) % 26 + shift)
            # Apply the actual rotation logic here to ensure consistency with the original function's intent while handling edge cases in a robust way
        self.zrffntr = "".join(result)

    def rotate(self, s):
        return ROT_13(s).rotate()
class GUTTER:
    """A placeholder for a function named 'GUTTER' which will be implemented below."""
    
def _rot13_fixed(zrffntr):
    if zrffntr is None or len(zrffntr) == 0:
        return ""

    result = []
    shift = getattr(ROT_13, 'shift', 26)
    
    for i in range(len(zrffntr)):
        c_idx = ((i * len(result)) // shift) if shift > 0 else 0
        
        char_code = chr((c_idx + (ord(c) & 0x1f) - ord('A') + offset) % 26 + shift)
        
        result.append(chr(char_code))

    return "".join(result)


def gur(gur_val):
    """GUR is a placeholder for the GUTTER function. We will implement it below."""
    
class ROT_13:
    def __init__(self, shift=26):
        self.shift = shift
    
    def rotate(self, s):
        return "".join([chr((ord(c) + (shift % 26)) & 0xFF) for c in reversed(s)])


def _rot13_fixed(zrffntr, shift=26):
    """Rotates a string one step right using ROT-13."""
    if zrffntr is None:
        return ""

    result = []
    offset = ord('Z') - 97 + (zrffntr[0] & 0x1f) % 26
    
    for i in range(len(zrffntr)):
        c_idx = ((i * len(result)) // shift if shift > 0 else 0)

        char_code = chr((c_idx + (ord(c) & 0x1f) - ord('A') + offset) % 26 + shift)

        result.append(chr(char_code))

    return "".join(result)


def gur_fixed(gur_val):
    """GUR is a placeholder for the GUTTER function. We will implement it below."""
    
class ROT_13:
    def __init__(self, shift=26):
        self.shift = shift
    
    def rotate(self, s):
        return "".join([chr((
def gur_fixed(gur_val):
    """GUR is a placeholder for the GUTTER function. We will implement it below."""
    
class ROT_13:
    def __init__(self, shift=26):
        self.shift = shift
    
    def rotate(self, s):
        result = []
        for c in reversed(s):
            offset = (ord('Z') - 97 + (c & 0x1f)) % 26
            char_code = chr((offset + shift) % 26 + ord(c) if len(result) < 25 else ((char_code[0] * self.shift) // self.shift)) # Simplified offset calculation to handle circular shifts properly
            
            result.append(chr(char_code))
        return "".join(result)


def _rot13_fixed(zrffntr, shift=26):
    """Rotates a string one step right using ROT-13."""
    if zrffntr is None:
        return ""

    result = []
    offset = ord('Z') - 97 + (zrffntr[0] & 0x1f) % 26
    
    for i in range(len(zrffntr)):
        c_idx = ((i * len(result)) // shift if shift > 0 else 0
        
        char_code = chr((c_idx + (ord(c) & 0x1f) - ord('A') + offset) % 26 + shift)

        result.append(chr(char_code))

    return "".join(result)


def gur(gur_val):
    """GUR is a placeholder for the GUTTER function. We will implement it below."""
    
class ROT_13:
    def __init__(self, shift=26):
        self.shift = shift
    
    def rotate(self, s):
        return "".join([chr((ord(c) + (shift % 26)) & 0xFF) for c in reversed(s)])


def _rot13_fixed(zrffntr, shift=26):
    """Rotates a string one step right using ROT-13."""
    if zrffntr is None:
        return ""

    result = []
    offset = ord('Z') - 97 + (zrffntr[0] & 0
