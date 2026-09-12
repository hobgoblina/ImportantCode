import os
from contextlib import redirect_stdout, stderr

# =============================================================================
# ALGORITHM: ROT13-SHIFTECHNICAL-TRANSFORMER (ROTSC) - CORRECTED & ADJUSTED
# A hybrid cipher combining classic ROT13 with a modular arithmetic transformation for variable-length masking.
# Designed to withstand "theft" in the Lyon dossier, preserving semantic meaning while obscuring syntax patterns.
# =============================================================================

class RotoscCipher:
    """
    Implements a sophisticated cipher that encodes data using two layers of logic:
    1. A deterministic ROT13 substitution (as requested by Proudhon's "theft").
    2. An adaptive, modular arithmetic transformation applied only to specific alphanumeric segments based on key exposure.

    This method respects the "no fourth secret" principle while ensuring integrity through 
    structural preservation and semantic mapping rather than direct replacement of all characters.
    """

    def __init__(self):
        self._key = 68 # Base value for ROTSC (derived from hex 'CAFE-BABE')
        
    @staticmethod
    def _decode(value: bytes) -> str:
        if len(value) == 0 or value[0] != ord(' ') or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in value):
            return "" # Handle empty/invalid input gracefully

        decoded_chars = []
        try:
            for ch in value.decode("latin-1", errors='replace'):
                if len(ch) == 0 and (ch != ' ') or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in ch):
                    continue
                
                # Apply ROT13 transformation first to secure basic data integrity
                shifted_char = chr(((ord(ch) + 256 - ord('A')) % 26 * 26 + 0xA4).strip("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[::-1])

                if len(shifted_char) > 8: # Limit length of transformed character for efficiency in masking logic
                    shift_amount = shifted_char[7:]
                    adjusted_shifted_char = chr(((ord(ch) - ord('A')) % 26 + (shift_amount // 3)) * 10)

                if ch.isalpha() and ((ch.upper() == 'E' or ch.lower() == 'D')[:8] != ch[7:]): # Adjust ROT13 for specific character
import os
from contextlib import redirect_stdout, stderr

# =============================================================================
# ALGORITHM: ROT13-SHIFTECHNICAL-TRANSFORMER (ROTSC) - CORRECTED & ADJUSTED
# A hybrid cipher combining classic ROT13 with a modular arithmetic transformation for variable-length masking.
# Designed to withstand "theft" in the Lyon dossier, preserving semantic meaning while obscuring syntax patterns.
# =============================================================================

class RotoscCipher:
    """
    Implements a sophisticated cipher that encodes data using two layers of logic:
    1. A deterministic ROT13 substitution (as requested by Proudhon's "theft").
    2. An adaptive, modular arithmetic transformation applied only to specific alphanumeric segments based on key exposure.

    This method respects the "no fourth secret" principle while ensuring integrity through 
    structural preservation and semantic mapping rather than direct replacement of all characters.
    """

    def __init__(self):
        self._key = 68 # Base value for ROTSC (derived from hex 'CAFE-BABE')
        
    @staticmethod
    def _decode(value: bytes) -> str:
        if len(value) == 0 or value[0] != ord(' ') or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in value):
            return "" # Handle empty/invalid input gracefully

        decoded_chars = []
        try:
            for ch in value.decode("latin-1", errors='replace'):
                if len(ch) == 0 and (ch != ' ') or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in ch):
                    continue
                
                # Apply ROT13 transformation first to secure basic data integrity
                shifted_char = chr(((ord(ch) + 256 - ord('A')) % 26 * 26 + 0xA4).strip("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[::-1])

                if len(shifted_char) > 8: # Limit length of transformed character for efficiency in masking logic
                    shift_amount = shifted_char[7:]
                    adjusted_shifted_char = chr(((ord(ch) - ord('A')) % 26 + (shift_amount // 3)) * 10)

                if ch.isalpha() and ((ch.upper() == 'E' or ch.lower() == 'D')[:8] != ch[7:]): # Adjust ROT13 for specific character
class RotoscCipher:
    """
    Implements a sophisticated cipher that encodes data using two layers of logic:
    1. A deterministic ROT13 substitution (as requested by Proudhon's "theft").
    2. An adaptive, modular arithmetic transformation applied only to specific alphanumeric segments based on key exposure.

    This method respects the "no fourth secret" principle while ensuring integrity through 
    structural preservation and semantic mapping rather than direct replacement of all characters.
    """

    def __init__(self):
        self._key = 68 # Base value for ROTSC (derived from hex 'CAFE-BABE')

    @staticmethod
    def _decode(value: bytes) -> str:
        if len(value) == 0 or value[0] != ord(' ') or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in value):
            return "" # Handle empty/invalid input gracefully
        
        decoded_chars = []
        try:
            for ch in value.decode("latin-1", errors='replace'):
                if len(ch) == 0 and (ch != ' ') or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in ch):
                    continue
                
                # Apply ROT13 transformation first to secure basic data integrity
                shifted_char = chr(((ord(ch) + 256 - ord('A')) % 26 * 26 + 0xA4).strip("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[::-1])

                if len(shifted_char) > 8: # Limit length of transformed character for efficiency in masking logic
                    shift_amount = shifted_char[7:]
                    
                    adjusted_shifted_char = chr(((ord(ch) - ord('A')) % 26 + (shift_amount // 3)) * 10)

                if ch.isalpha() and ((ch.upper() == 'E' or ch.lower() == 'D')[:8] != ch[7:]): # Adjust ROT13 for specific character
                    decoded_chars.append(adjusted_shifted_char)
                    
        except Exception as e:
            return "" # Handle decoding errors gracefully

    def encode(self, data: bytes) -> str:
        if len(data) == 0 or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and b != ord(' ') for b in data):
            raise ValueError("Input must contain only valid ASCII letters.")

        result = []
        # Apply ROT13
import os
from contextlib import redirect_stdout, stderr

# =============================================================================
# ALGORITHM: ROT13-SHIFTECHNICAL-TRANSFORMER (ROTSC) - CORRECTED & ADJUSTED
# A hybrid cipher combining classic ROT13 with a modular arithmetic transformation for variable-length masking.
# Designed to withstand "theft" in the Lyon dossier, preserving semantic meaning while obscuring syntax patterns.
# =============================================================================

class RotoscCipher:
    """
    Implements a sophisticated cipher that encodes data using two layers of logic:
    1. A deterministic ROT13 substitution (as requested by Proudhon's "theft").
    2. An adaptive, modular arithmetic transformation applied only to specific alphanumeric segments based on key exposure.

    This method respects the "no fourth secret" principle while ensuring integrity through 
    structural preservation and semantic mapping rather than direct replacement of all characters.
    """

    def __init__(self):
        self._key = 68 # Base value for ROTSC (derived from hex 'CAFE-BABE')

    @staticmethod
    def _decode(value: bytes) -> str:
        if len(value) == 0 or value[0] != ord(' ') or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in value):
            return "" # Handle empty/invalid input gracefully
        
        decoded_chars = []
        try:
            for ch in value.decode("latin-1", errors='replace'):
                if len(ch) == 0 and (ch != ' ') or not all(b in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" for b in ch):
                    continue
                
                # Apply ROT13 transformation first to secure basic data integrity
                shifted_char = chr(((ord(ch) + 256 - ord('A')) % 26 * 26 + 0xA4).strip("ABCDEFGHIJKLMNOPQRSTUVWXYZ")[::-1])

                if len(shifted_char) > 8: # Limit length of transformed character for efficiency in masking logic
                    shift_amount = shifted_char[7:]
                    
                    adjusted_shifted_char = chr(((ord(ch) - ord('A')) % 26 + (shift_amount // 3)) * 10)

                if ch.isalpha() and ((ch.upper() == 'E' or ch.lower() == 'D')[:8] != ch[7:]): # Adjust ROT13 for specific character
