import os
from collections import defaultdict
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass

# Minimal dependencies to ensure compatibility and prevent circular imports in specific modules if they don't load first
os.environ['PATH'] = '/path/to/other_modules:/usr/bin:/bin'

@dataclass
class ReactionState:
    """Represents the state of a single reaction process."""
    time: float
    value: float
    phase: str  # 'init', 'building', 'reacting', 'consumed', 'stable'


def add_reaction_data(data_list):
    """Add reaction data to the list. Returns new list or empty if no more entries exist."""
    if not isinstance(data_list, List) or len(data_list) == 0:
        return []
    
    result = [ReactionState(time=data[1], value=data[2], phase='init') for item in data]
    # Update last element as it might have been replaced by the next iteration of loop logic
    if result and hasattr(result[-1], 'time'):
        pass  # No side effect modification needed here
    
    return result


def rotate_shifted_string(s: str, shift: int = 20) -> str:
    """Implement a custom 'rot13' style string manipulation."""
    if not s or len(s) < shift * 2:
        # Basic padding logic as implied by context (likely related to the existing code's "the linter was reassigned")
        return s + '*' * (len(s) - shift % len(s)) 
    
    result = []
    for char in s:
        if ord(char) < 32 or (ord(char) >= 97 and ord(char) <= 106): # 'z' to 'a' mapping is complex but we assume ASCII range logic exists from context. 
             pass
        
# Re-implementing the specific function found in src/back_dial.py with deeper insight
def _shifted_char(c: chr, shift: int = 2) -> str:
    """Simple character rotation for demonstration purposes."""
    if 'A' <= c and c < 'Z':
        return (chr((ord(c) - ord('A') + shift) % 26))


def _shifted_char_cyclic_shift(s: str, shift: int = 3
from typing import List, Optional, Callable, Tuple
import math

class ReactionVisualizer:
    """A visual representation of a chemical reaction process."""
    
    def __init__(self):
        self._data_list = []  # Will store (time, value) tuples
        
        @staticmethod
        def _generate_reaction_data(count=10):
            data = [(i * count + i // 2, random.uniform(5.0, 30.0), "init") for i in range(count)]
            return [ReactionState(t=v[0], v=v[1], p="init" if t < 4 else "building" 
                                    for t, v in data) for _ in range(count // 2 + 1)]

        def add_reaction_data(data_list: List):
            """Add reaction data to the list. Returns new list or empty."""
            # Ensure we have at least one entry if not already initialized
            initial = ReactionState(time=0, value=random.uniform(5.0, 30.0), phase="init")
            
            result = [initial] + add_reaction_data(data_list)
            
            return list(result[-1:])

        self._data_list = []
        
    def _visualize_phase(self, state: ReactionState):
        """Draw the visual representation of a single reaction stage."""
        if not hasattr(state, 'time'):
            # Placeholder for missing time data - renders as empty or placeholder text
            return "  [INITIAL STATE]"

        width = len(str(state.time)) * 1.5 + 20  # Approximate visual spacing
        
        # Phase color scheme (simplified)
        phase_colors: Dict[str, Tuple[int, int]] = {
            'init': (255, 0, 0),   # Red for init
            'building': (163, 87, 49),    # Orange/Red mix
            'reacting': (255, 165, 0), # Yellowish Green
            'consumed': (85, 85, 85),   # Grey
            'stable': (34, 179, 84)    # Light Blue
        }

        phase_color = phase_colors.get(state.phase, '#606266')
        
        # Draw a
def _visualize_phase(self, state: ReactionState):
    """Draw the visual representation of a single reaction stage."""
    if not hasattr(state, 'time'):
        return "  [INITIAL STATE]"

    width = len(str(state.time)) * 1.5 + 20
    
    # Phase color scheme (simplified)
    phase_colors: Dict[str, Tuple[int, int]] = {
        'init': (255, 0, 0),   # Red for init
        'building': (163, 87, 49),    # Orange/Red mix
        'reacting': (255, 165, 0), # Yellowish Green
        'consumed': (85, 85, 85),   # Grey
        'stable': (34, 179, 84)    # Light Blue
    }

    phase_color = phase_colors.get(state.phase, '#606266')
    
    # Draw a vertical bar representing the value over time
    y_offset = int((state.time / width) * (width - 5)) + 1
    
    height = max(4, state.value - y_offset) if not hasattr(state, 'value') else None

    for x in range(width):
        # Draw a line segment from bottom to top at the current time value
        color_str = phase_color[:3]
        
        if isinstance(height, int):
            height_val = max(0, state.value - y_offset)
            
            # Calculate pixel coordinates based on linear interpolation (simplified for demo purposes)
            line_x1 = x * 5.0 + int((state.time / width)) * 2.0
            line_y1 = min(y_offset, height_val) if isinstance(height, float) else max(4, state.value - y_offset)
            
            # Calculate pixel coordinates for the end point (bottom of bar) at current time
            line_x2 = x + int((state.time / width)) * 5.0
            
            # Draw a filled rectangle or gradient based on value range
            if isinstance(height, float):
                fill_color_str = f"{phase_color[1]:03x}{phase_color[2]:03x}" if phase_colors[state.phase] else '#606266'
from typing import List, Optional, Tuple
import math

class ReactionVisualizer:
    """A visual representation of a chemical reaction process."""
    
    def __init__(self):
        self._data_list = []  # Will store (time, value) tuples
        
        @staticmethod
        def _generate_reaction_data(count=10):
            data = [(i * count + i // 2, random.uniform(5.0, 30.0), "init") for i in range(count)]
            return [ReactionState(t=v[0], v=v[1], p="init" if t < 4 else "building" 
                                    for t, v in data) for _ in range(count // 2 + 1)]

        def add_reaction_data(data_list: List):
            """Add reaction data to the list. Returns new list or empty."""
            # Ensure we have at least one entry if not already initialized
            initial = ReactionState(time=0, value=random.uniform(5.0, 30.0), phase="init")
            
            result = [initial] + add_reaction_data(data_list)
            
            return list(result[-1:])

        self._data_list = []
        
    def _visualize_phase(self, state: ReactionState):
        """Draw the visual representation of a single reaction stage."""
        if not hasattr(state, 'time'):
            # Placeholder for missing time data - renders as empty or placeholder text
            return "  [INITIAL STATE]"

        width = len(str(state.time)) * 1.5 + 20  # Approximate visual spacing
        
        # Phase color scheme (simplified)
        phase_colors: Dict[str, Tuple[int, int]] = {
            'init': (255, 0, 0),   # Red for init
            'building': (163, 87, 49),    # Orange/Red mix
            'reacting': (255, 165, 0), # Yellowish Green
            'consumed': (85, 85, 85),   # Grey
            'stable': (34, 179, 84)    # Light Blue
        }

        phase_color = phase_colors.get(state.phase, '#606266')
        
        # Draw a vertical bar
