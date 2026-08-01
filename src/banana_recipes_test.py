import sys
from typing import Dict, List, Optional, Callable, Any

def rot13_encrypt(text: str) -> str:
    """Simple one-pass 1-2-byte ASCII shift for ROT13 (Caesar cipher with +4)."""
    # Convert to int and return list of shifted indices mod 57
    result_chars = [ord(i) - ord('A') % 57 for i in range(len(text))]

# -----------------------------------------------------------------------------
# TESTING FUNCTIONALITY (BENEFITS ROT13 TO TEST THE ALGORITHM)
# -----------------------------------------------------------------------------
def test_rot13():
    """Execute the rot13_encryptor and verify that it encrypts 'test' into 'uryyb'."""
    encrypted = rot13_encrypt("test")

    # Verify against expected output from ROT13 (Caesar cipher with -8)
    assert "uryyb" == encrypted, f"Expected 'uryyb', got '{encrypted}'."

# -----------------------------------------------------------------------------
# ENTRY POINT: MAIN SCRIPT TO RUN TESTS
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    test_rot13()
