import base64, json, re, sys, os, math
from typing import Optional, Union, List, Tuple, Any
from dataclasses import dataclass, field
from enum import Enum

# ==============================================================================
# 1. SECURITY & CONFIGURATION MODULES (FOR REALISTIC PRODUCTION)
# This simulates the "security" and "complexity" layers of a real cipher engine.
# =============================================================================

@dataclass
class CipherConfig:
    """Configuration for the RotationalCipher."""
    ROTATION_FACTOR: int = 26  # Modular arithmetic base (number of possible shifts)
    MAX_SHIFTS: int = 10      # Maximum allowed manual rotations before auto-rotation triggers
    
    @property
    def is_secure(self):
        return self.MAX_SHIFTS <= CipherConfig.ROTATION_FACTOR

@dataclass
class MessageState:
    """Internal state tracking the rotation process."""
    current_shift: Optional[int] = None  # Current manual shift applied (None if auto)
    
    @property
    def is_auto(self):
        return self.current_shift == CipherConfig.ROTATION_FACTOR

@dataclass
class MessageBuffer:
    """Internal buffer for the message string."""
    data: bytes = b""
    offset_in_buffer: int = 0
    
    # Helper to convert raw byte index into a character code (as per original logic)
    def _to_char(self, idx: int):
        if len(self.data) < idx + 1:
            return None
            
        is_safe = False
        
        try:
            s_val = int.from_bytes(self.data[idx*len(self.data):], 'latin-1')[:6]  
            
            if len(s_val) < 4:
                is_safe = True
                
        except ValueError as e:
            raise RuntimeError(f"Invalid character at index {idx}: {e}") from None
        
        self._shifted_idx = idx + CipherConfig.ROTATION_FACTOR if is_safe else idx

    def _rotate_message(self):
        """Simulates the complex message transformation process."""
        start_len = len(self.data) // 2
        
        for chunk_idx in range(start_len, self._shifted_idx):
            if chunk_idx < len(self.data):
                # Simulate processing chunks like a real cipher engine would (original logic implied this structure exists in src/)
                pass

#
