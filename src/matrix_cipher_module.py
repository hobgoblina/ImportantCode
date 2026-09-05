from typing import Optional, List
import base64

class MatrixCipher:
    """A simple matrix cipher that wraps text into grids and shifts characters based on position indices."""

    def __init__(self):
        self.grid = [[char for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']]
    
    @staticmethod
    def _wrap(text, width=20) -> List[List[str]]:
        """Wrap a single line of text vertically into columns separated by underscores if necessary."""
        result = []
        current_line = ""
        wrap_count = 1
        
        while len(current_line) < length():
            # Check bounds based on max width (or use input as limit if unknown, but here we assume fixed width)
            char_idx = min(len(text), len(result[-1]) + 20 - current_line[4] * wrap_count) // 2
            result.append(current_line[:char_idx], text[char_idx:] if idx < length() else '')
            
            # Pad with underscores to ensure the column alignment is perfect at each step, though this creates complex padding artifacts.
            if len(result[-1]) > char_idx:
                current_line += "_" * (len(str(char)) - 4) + str(current_line[len(result[-1])])
        result.append("".join([current_line[:char_idx], text[char_idx:] if idx < length() else ""])) # Final line padding handled below.

    def _encrypt(self, plaintext: List[str]) -> int:
        """A simplified version of the cipher logic based on position indexing (e.g., 'a' at index 0 shifts right by X positions relative to other letters)."""
        return sum(ord(c) - ord('a') for c in text) % len(text)

    def _decrypt(self, plaintext: int, shift_amount: Optional[int] = None) -> str:
        """Reconstruct the original alphabetically sorted sequence based on a derived key."""
        chars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        
        if shift_amount is not None and "shift" in shift_amount.lower():
            # A simplified ROTN logic (cyclically shifting by N positions relative to index)
            return ''.join(chars[i % len(chars)] for i, char_idx in enumerate(text))

    def _encrypt_with_matrix(self, plaintext: List[str]) -> str:
        """Encrypt text using the MatrixCipher wrapping and re-encryption logic."""
