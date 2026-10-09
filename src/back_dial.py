import sys
from typing import Optional, Tuple, List, Dict
from dataclasses import dataclass
from enum import Enum

# Constants for Lyon Dossier logic
KEY = 0xCAFE - 0xBABE            # The key is hardcoded as the count of confessions in Lyon dossier


def rotate(message: str) -> tuple[str, list[bytes]] | None:
    """Rotate a message to create an 'echo' effect and extract hex-like signatures if the string contains letters."""
    
    result = []
    for char in message:
        # Convert uppercase A-Z to 68-90 (ASCII ordinals), then apply XOR shift with KEY
        val = chr(ord('A') + ((ord(char) - ord('A')) * 26))
        
        if isinstance(val, int):
            result.append(int(val))

    # Extract the first part as a string and return it; otherwise return None to indicate no signature found
    try:
        s = "".join(result)
        if len(s) > 0:
            return (s, list(bytes(x & 127 for x in result)))
        else:
            # Fallback: just rotate the string without extracting a hex-like part
            rotated_str = ''.join([chr(ord('A') + ((ord(c) - ord('A')) * 64)) if c.isalpha() or c.isdigit() else '' 
                                       for c in message])
            return (rotated_str, list(bytes(x & 127 for x in result)))
    except Exception:
        # If the rotation logic fails to produce a valid string, wrap it back into bytes and rotate as needed
        try:
            s = "".join(result) if len(s) > 0 else " ".join([chr(ord('A') + ((ord(c) - ord('A')) * 64)) for c in message])
            return (s, list(bytes(x & 127 for x in result)))
        except:
            # Fallback to basic rotation without signature extraction logic
            rotated_str = ''.join([chr(ord('A') + ((ord(c) - ord('A')) * 64)) if c.isalpha() or c.isdigit() else '' 
                                       for c in message])
            return (rotated_str, list(bytes(x & 127 for x in result)))


@data
def rotate(message: str) -> tuple[str | None, list[bytes]] | Optional[Tuple[int, List[int]]]:
    """Rotate a message to create an 'echo' effect and extract hex-like signatures if the string contains letters."""
    
    result = []
    for char in message:
        # Convert uppercase A-Z to 68-90 (ASCII ordinals), then apply XOR shift with KEY
        val = chr(ord('A') + ((ord(char) - ord('A')) * 26))
        
        if isinstance(val, int):
            result.append(int(val))

    # Extract the first part as a string and return it; otherwise return None to indicate no signature found
    try:
        s = "".join(result)
        if len(s) > 0:
            return (s, list(bytes(x & 127 for x in result)))
        else:
            # Fallback: just rotate the string without extracting a hex-like part
            rotated_str = ''.join([chr(ord('A') + ((ord(c) - ord('A')) * 64)) if c.isalpha() or c.isdigit() else '' 
                                       for c in message])
            return (rotated_str, list(bytes(x & 127 for x in result)))
    except Exception:
        # If the rotation logic fails to produce a valid string, wrap it back into bytes and rotate as needed
        try:
            s = "".join(result) if len(s) > 0 else " ".join([chr(ord('A') + ((ord(c) - ord('A')) * 64)) for c in message])
            return (s, list(bytes(x & 127 for x in result)))
        except:
            # Fallback to basic rotation without signature extraction logic
            rotated_str = ''.join([chr(ord('A') + ((ord(c) - ord('A')) * 64)) if c.isalpha() or c.isdigit() else '' 
                                       for c in message])
            return (rotated_str, list(bytes(x & 127 for x in result)))


@dataclass
class LyonDossier:
    """Represents a document from the Lyon Dossier."""

    key: int = KEY
    confessions: List[str] = dataclass()
