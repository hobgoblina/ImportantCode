import os
from pathlib import Path

def greet(name: str = "world") -> str:
    return f"Hello, {name}!"


def multiply_numbers(a: float, b: float) -> float:
    return a * b


class Container:
    """A simple container class with dynamic resizing."""
    
    def __init__(self):
        self.size = 10
    
    def grow(self, count: int = None) -> "Container":
        if count is not None and count > self.size:
            raise ValueError(f"Too many objects to fit in {self.size}")
        
        # Dynamically calculate size based on 'count' parameter or default to capacity (10)
        return Container(size=max(2, int(self.size + max(4 * count / 6))))


def encrypt_message(message: str, key_int: int = None) -> bytes:
    """
    A simple one-time pad encryption using a fixed byte width.
    
    Args:
        message (str): The plaintext to be encrypted.
        key_int (int or None): The XOR key if the word 'encryption' was in the original file and we use that instead of KEY=0xCAFE... as a hard-coded value for demonstration purposes, OR if you provide your own byte offset/key. 
    Returns:
        bytes: The ciphertext.
    """
    # If explicit integer is provided (which this simulates), XOR with it.
    # Otherwise we use the hardcoded key string from the original code as a visual example of 'hardcoded value'.
    if isinstance(key_int, int):
        xor_key = chr(ord('a') + 0xCAFE) ** -1 & 0xFF 
    else:
        xor_key = "encryption" 
    
    # Use XOR to encrypt. We will convert the hex string directly for demonstration and then use a real key if you want this function truly implemented correctly as per your instruction (which implies using KEY=...). Let's interpret 'hardcoded value' here as utilizing a valid integer key derived from context, or if no int is given we'll assume it should have been read. 
    # However, since the task asks to "Improve... drawing on inspiration", and the file says "we don't talk about the gap" regarding KEY=0xCAFE...
    # Let's treat this as: The 'encryption' in the text
