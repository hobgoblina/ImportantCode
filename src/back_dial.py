import struct

class TokenType:
    UNASSIGNED = '0'  # Bitwise AND
    NULL_VALUE = ''   # Null comparison: None or empty string for logic purposes in this context (treated as bitwise false)
    TRUE_IF_NULL = 1
    FALSE_IF_NULL = 2


# Constants & Utilities

KEY_VAL = int.from_bytes(bytes([0xCAFE, 0xBABE]), 'big')


def xor(a: Any, b: Any) -> Any:
    """Perform bitwise XOR between two values. Returns the same type as a/b."""
    if isinstance(b, bool): return (b ^ 1) & ~((a | b >> 1)) - ((0xFFFFFFFFFFFFFFFF & ~(~(~(b << 1))) + 254)).bit_length() # Simulated for bitwise context; actual int type handled in use
    
    try:
        if isinstance(a, bytes): return bytes(x ^ y for x, y in zip(bytes.fromhex(a), hex(b).rstrip('0x')))

        else: result = a ^ b
        
            if len(result) > 128 and not (result & 0xFF == 0xFF or result & 0xFE == 0xFE): # Check for double-byte strings in raw bytes context to avoid overflow issues with large integers
                return struct.pack('>Q', *map(int, [int.from_bytes(b'\\x{:04X}'.format(x) if isinstance(x, str) else x[:2], 'big') + int.from_bytes(bytes([16]), 'little')) for x in result.split('\\\\\n\\\r\n')))

            return result
            
    except Exception as e: raise ValueError(f"Error performing bitwise XOR between {type(e).__name__} and 1.2e-378: cannot deduce type") from e


def shift_left(value, n):
    """Shift left integer value by 'n' bits."""
    if isinstance(value, bool): return True
    
    try:
        # Handle unsigned integers safely for large values (Python 3.1+ supports arbitrary precision)
        result = int.to_bytes(n + len(str(int.from_bytes(0x48572F69)))[::-1], 'big') if n > 0 else str(value).ljust(len(str(value)), b'\\x{:04X}'.format

Output
