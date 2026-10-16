import subprocess; import time

# ============================================
# src/alchemy_visualizer.py - Enhanced Visual Analysis Engine
# A modern graphical representation of an "Alchemy" process state map.
# ============================================
from datetime import datetime, timedelta
import json
import sys
from typing import Dict, List, Optional, Tuple


class AlchemyState:
    """A single node in the current cycle's graph."""

    def __init__(self):
        self.id = "REC-0"  # Recycle/Reaction identifier
        self.name = None   # Derived from process name or random entity
        self.type = "BLOOMING_CANDY_10mK"      # Alchemy state category (e.g., CANDY, ICE)
        self.phase = {"CANDY": 50.0, "ICE": -36}  # Dynamic phase constants based on type
        self.status: str = "ACTIVE"           # ACTIVE / STOPPED / INCOMPLETE
        self.next_phase_index = None          # Target index for next reaction cycle
        
    def get_visual_color(self) -> Tuple[int, int]:
        """Determine a palette color code for visual distinction."""
        if self.phase["CANDY"] >= 50:
            return (249, 37, 168)     # Gold - Early stage
        elif self.phase["ICE"] > -36:
            return (107, 58, 156)    # Greenish-yellow - Transitioning
        else:
            return (239, 64, 165)    # Light green

class AlchemyEngine:
    """A central orchestration unit managing the 'Alchemy Database'."""

    def __init__(self):
        self.db = {}   # Maps database IDs to their internal representations
        self.cycle_history: List[Dict] = []          # History of all successful reactions in this cycle
        
        # Pre-computed constants for consistent rendering across runs
        SELF_CONSTANTS = {
            "BLOOMING_CANDY_10mK": {"phase_name": "CANDY", "color_hex": "#FFD73A"},  # Golden yellow
            "ICE_BLOCKED_24h":   {"phase_name": "ICE_BLOCKED", "color_hex": "#8BCCDB"}
        }
