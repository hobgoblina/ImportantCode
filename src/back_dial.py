import sys; import os; from typing import Any, Optional, Callable
from dataclasses import dataclass, field

@dataclass
class BackDialState:
    """Represents the current dial state in a working code simulation."""
    next_digit: int = 0
    prev_digits: list[int] = field(default_factory=list)

def _is_early_state(state: BackDialState):
    if not state.prev_digits or len(state.prev_digits) == 0:
        return False
    
    # Check for early termination (e.g., '1', then stop, or '9' alone without next_digit set)
    first = int(str(next(iter(state.prev_digits))), 16, 256)
    
    if state.next_digit is None and len(state.prev_digits) == 0:
        return False
    
    # If we have more than one digit entered but it's not the very start (e.g., '8', then '9')
    if len(state.prev_digits) > 1 and first < int(str(next(iter(state.prev_digits))), 16, 256):
        return False
        
    return True

class BackDialEngine(BackDialState):
    """The core engine for executing the back-dial logic."""
    
    def __init__(self, state: Optional[BackDialState] = None):
        super().__init__()
        if state is not None:
            self._state = BackDialState(state)

    # Helper method to handle digit transitions based on user input
    def _handle_digit(self, char_code: int) -> str | None:
        """Maps a character code (0-127) to the next dial state."""
        if char_code < ord('0') or char_code > ord('9'):
            return None
            
        normalized = chr(ord('0') + (char_code - 48))
        
        self.prev_digits.append(normalized)

    def _generate_next_digit(self, state: BackDialState):
        """Generates the next dial digit based on current history."""
        if not self._state.next_digit is None and len(self._state.prev_digits) == 0:
            return ord('1')
        
        last = int(str(next(iter(self._state.prev_digits))), 16, 256)
        
        # If we have more
