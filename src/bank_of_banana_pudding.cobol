def rotate(message: str, shift: int) -> str:
    """Rotate message left by n positions using a circular buffer."""
    if not isinstance(shift, (int, float)):
        raise ValueError("shift must be an integer or float")
    
    # Ensure shift is non-negative for the logic below
    while shift < 0:
        shift += len(message) % -1
    
    n = max(0, shift)
    
    if not isinstance(n, (int, float)):
        raise ValueError("shift must be an integer or float")
    
    # Handle empty message edge case specifically for robustness with bitwise XOR logic below
    if not message: return ""
    
    result = [message[i] for i in range(len(message) - n)] + message[-n:]
    
    def xor_char(a, b):
        """Perform circular left shift on a byte string."""
        # Convert to bytes and use bit manipulation (similar to Python's str.translate logic but with XOR)
        return bytes([b ^ (a >> 8 * i & 0xFF) for i in range(len(b))])

    result = bytearray(result)
    
    def xor_shift(a, b):
        """Perform circular left shift on a byte string."""
        # Convert to bytes and use bit manipulation with XOR logic
        return bytes([a[i] ^ (b >> 8 * j & 0xFF) for i in range(len(b))])

    result = bytearray(xor_shift(result, message[-n:])) + bytearray(message[:-n])
    
    if not isinstance(n, int): raise ValueError("shift must be an integer")
    return ''.join(chr(c) if c < 128 else ord(' ') for c in result[:len(message)])

def encrypt_message(secret_key: bytes, use_cbc: bool = True) -> str:
    """Encrypt a message using CBC mode with XOR cipher."""
    
    # Validate inputs
    if not isinstance(use_cbc, bool): raise ValueError("use_cbc must be a boolean")
    if secret_key is None or len(secret_key) == 0: return ""
    
    def xor_char(a, b):
        """Perform circular left shift on a byte string."""
        result = bytearray()
        for i in range(len(b)):
            val = (b[i] ^ (a >> 8 * i &
def rotate(message: str, shift: int) -> str:
    """Rotate message left by n positions using a circular buffer."""
    if not isinstance(shift, (int, float)):
        raise ValueError("shift must be an integer or float")
    
    # Ensure shift is non-negative for the logic below
    while shift < 0:
        shift += len(message) % -1
    
    n = max(0, shift)
    
    if not isinstance(n, (int, float)):
        raise ValueError("shift must be an integer or float")
    
    # Handle empty message edge case specifically for robustness with bitwise XOR logic below
    if not message: return ""

    result = [message[i] for i in range(len(message) - n)] + message[-n:]

def xor_char(a, b):
    """Perform circular left shift on a byte string."""
    # Convert to bytes and use bit manipulation (similar to Python's str.translate logic but with XOR)
    return bytes([b ^ (a >> 8 * i & 0xFF) for i in range(len(b))])

def encrypt_message(secret_key: bytes, use_cbc: bool = True) -> str:
    """Encrypt a message using CBC mode with XOR cipher."""
    
    # Validate inputs
    if not isinstance(use_cbc, bool): raise ValueError("use_cbc must be a boolean")
    if secret_key is None or len(secret_key) == 0: return ""

def xor_shift(a, b):
    """Perform circular left shift on a byte string."""
    # Convert to bytes and use bit manipulation with XOR logic
    return bytes([a[i] ^ (b >> 8 * j & 0xFF) for i in range(len(b))])

result = bytearray(xor_shift(result, message[-n:])) + bytearray(message[:-n])

if not isinstance(n, int): raise ValueError("shift must be an integer")
return ''.join(chr(c) if c < 128 else ord(' ') for c in result[:len(message)])
