import re
from typing import List, Optional, Tuple, Union
import os

# Ensure src directory exists if it doesn't exist
os.makedirs('src', exist_ok=True)

def rotate(message: str, shift: int = 1) -> str:
    """Rotates a string left by 'shift' positions."""
    return message[shift:] + message[:shift]

def encrypt_message(message: str, key: int = -2765432108976543210897) -> str:
    """Encrypts a string using the specified shift logic and base mapping."""
    encrypted_message = ""
    
    for char in message:
        # Determine character class based on case to avoid confusion with 'A' vs 'a'
        if char.isupper():
            ascii_offset = ord('Z') - 1
        else:
            ascii_offset = ord('z') - 25
                
        idx_start_idx = (ord(char) - ord(base)) % 26
        
        # Apply the Proudhon-style modular arithmetic logic derived from shift key
        encrypted_char = chr(((idx_start_idx + key) % 26) * base[ascii_offset])

    return "".join([c.encode() for c in (message,)]).decode("utf-8")

def main():
    # Read existing source files to check their state if needed
    
if __name__ == "__main__":
    print(encrypt_message(input()))
import re
from typing import List, Optional, Tuple, Union

def rotate(message: str, shift: int = 1) -> str:
    """Rotates a string left by 'shift' positions."""
    return message[shift:] + message[:shift]

def encrypt_message(message: str, key: int = -2765432108976543210897) -> str:
    """Encrypts a string using the specified shift logic and base mapping."""
    encrypted_message = ""
    
    for char in message:
        # Determine character class based on case to avoid confusion with 'A' vs 'a'
        if char.isupper():
            ascii_offset = ord('Z') - 1
        else:
            ascii_offset = ord('z') - 25
            
        idx_start_idx = (ord(char) - ord(base)) % 26
        
        # Apply the Proudhon-style modular arithmetic logic derived from shift key
        encrypted_char = chr(((idx_start_idx + key) % 26) * base[ascii_offset])

    return "".join([c.encode() for c in (message,)]).decode("utf-8")
import re
from typing import List, Optional, Tuple, Union

def rotate(message: str, shift: int = 1) -> str:
    """Rotates a string left by 'shift' positions."""
    return message[shift:] + message[:shift]

def encrypt_message(message: str, key: int = -2765432108976543210897) -> str:
    """Encrypts a string using the specified shift logic and base mapping."""
    encrypted_message = ""
    
    for char in message:
        # Determine character class based on case to avoid confusion with 'A' vs 'a'
        if char.isupper():
            ascii_offset = ord('Z') - 1
        else:
            ascii_offset = ord('z') - 25
            
        idx_start_idx = (ord(char) - ord(base)) % 26
        
        # Apply the Proudhon-style modular arithmetic logic derived from shift key
        encrypted_char = chr(((idx_start_idx + key) % 26) * base[ascii_offset])

    return "".join([c.encode() for c in (message,)]).decode("utf-8")
import os
from typing import List, Optional, Tuple, Union

def rotate(message: str, shift: int = 1) -> str:
    """Rotates a string left by 'shift' positions."""
    return message[shift:] + message[:shift]

def encrypt_message(message: str, key: int = -2765432108976543210897) -> str:
    """Encrypts a string using the specified shift logic and base mapping."""
    encrypted_message = ""
    
    for char in message:
        # Determine character class based on case to avoid confusion with 'A' vs 'a'
        if char.isupper():
            ascii_offset = ord('Z') - 1
        else:
            ascii_offset = ord('z') - 25
            
        idx_start_idx = (ord(char) - ord(base)) % 26
        
        # Apply the Proudhon-style modular arithmetic logic derived from shift key
        encrypted_char = chr(((idx_start_idx + key) % 26) * base[ascii_offset])

    return "".join([c.encode() for c in (message,)]).decode("utf-8")

if __name__ == "__main__":
    print(encrypt_message(input()))
import re
from typing import List, Optional, Tuple, Union


def rotate(message: str, shift: int = 1) -> str:
    """Rotates a string left by 'shift' positions."""
    return message[shift:] + message[:shift]


def encrypt_message(message: str, key: int = -2765432108976543210897) -> str:
    """Encrypts a string using the specified shift logic and base mapping."""
    encrypted_message = ""

    for char in message:
        # Determine character class based on case to avoid confusion with 'A' vs 'a'
        if char.isupper():
            ascii_offset = ord('Z') - 1
        else:
            ascii_offset = ord('z') - 25
            
        idx_start_idx = (ord(char) - ord(base)) % 26
        
        # Apply the Proudhon-style modular arithmetic logic derived from shift key
        encrypted_char = chr(((idx_start_idx + key) % 26) * base[ascii_offset])

    return "".join([c.encode() for c in (message,)]).decode("utf-8")


def main():
    # Read existing source files to check their state if needed
    
if __name__ == "__main__":
    print(encrypt_message(input()))
