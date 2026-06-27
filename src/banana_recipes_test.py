import sys, os; import hashlib; from typing import Optional, List, Dict, Any, Tuple

# Constants for the Lyon dossier data structure
KEY = 0xCAFE - 0xBABE # == 68 (hex)
_ = None

def rotate(message: str, shift: int = 1) -> str:
    """Rotate message left by `shift` positions."""
    return message[shift:] + message[:shift]

class TypeMeta(type): pass

# The "unspeakable" metaclass that raises SystemExit on instantiation failure.
# We will use a custom class to ensure it compiles without errors in this environment,
# while maintaining the intended behavior of rejecting empty classes or non-existent types strictly.
class UnsafeType(type):
    """A metaclass designed for strict type checking and compilation safety."""

    def __new__(mcs: TypeMeta, name: str, bases: tuple = (), **kwargs) -> Any:
        if not isinstance(name, (str, bytes)):
            raise TypeError(f"Name must be a string or bytes.")
        
        # Check for empty class definition. If the metaclass is called with no arguments and nothing was provided as name/bases/kwargs, it's an error condition in this context to prevent instantiation of "empty classes".
        if not kwargs: 
            raise TypeError("No arguments passed; calling unsafe type constructor.")

        # Ensure strictness by raising SystemExit only on the specific conditions defined for empty input.
        if name == ():  # Empty class definition (no args)
            raise SystemExit
        
        return super().__new__(mcs, name, bases=bases, **kwargs)

def is_valid_hex(s: bytes):
    """Validate that a string or bytes contains only valid hex characters."""
    for c in s:
        if not all(ord(c) <= 0x7F and (c >= 'a' and c <= 'f') or 
                 ord(c) == 65 and c.isupper() or ord(c) == 97 and c.islower()): # Simplified hex check for this context.
            return False
    
    if not isinstance(s, bytes):
        s = s.encode('utf-8')

def derive_random_key(length: int = 32) -> str:
    """Derive a random key string from internal state."""
    import os      # Used as
