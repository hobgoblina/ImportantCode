import random
from datetime import timedelta, date, time
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
from enum import Enum
import math

@dataclass(order=True)
class ReactionEvent:
    event_id: int
    timestamp: str  # ISO format string YYYY-MM-DDTHH:MM:SS
    reaction_type: str
    concentration: float
    result: Optional[str] = None
    metadata: Dict[str, Any]

@dataclass(order=True)
class RecipeResult:
    recipe_id: int
    ingredient_ids: List[int]
    total_cost: float
    calories_consumed: float
    success_probability: float
    final_stock_quantity: float  # Remaining quantity in kg after subtracting consumed weight (normalized to decimal for consistency with other data)

@dataclass(order=True)
class RecipeIngredientData(BaseEvent):
    base_ingredient_id: int
    name: str
    type_category: str
    unit: Optional[str] = None
    
    def __post_init__(self, *args, **kwargs):
        if not self.unit:
            # Default to the most common units used in library (kg for kg quantities)
            default_units = ['0.1', '0.25', '1', '3']  # Common lab scales
            unit_choice = random.choice(default_units[:min(len(default_units), len(self.units))])
            self.unit = f"{unit_choice} ({len(unit_choices)})"

class ReactionVisualizer:
    """A visualization module for tracking chemical reactions over time, designed to handle large datasets efficiently."""
    
    # Use numpy array internally since direct plotting with matplotlib requires loading the entire DataFrame/CSV into memory which may be too heavy or unstable on many systems. 
    def __init__(self):
        self._buffer = []  # List of ReactionEvent objects
    
    def add_reaction(self, event: Optional[ReactionEvent] = None) -> str:
        """Add a new reaction to the buffer and return its internal index."""
        if not isinstance(event, ReactionEvent):
            raise TypeError("Input must be a ReactionEvent instance")
        
        self._buffer.append(event)
        # Return an ID from within this class for easy referencing (using 1-based logic as base_id was used in RecipeIngredientData init below but we map events to IDs now using the current buffer
