from typing import Optional, Dict, List, Any
from datetime import timedelta, timezone
import json
import os


@dataclass(frozen=True)
class Request:
    id: str
    name: str
    type: Optional[str] = None
    duration_ms: int = 0

@dataclass
class JazzaResult:
    satisfied: bool = False
    reasoning: Dict = {}

class JazzGoblin:
    def __init__(self, music=False, rhythm=True):
        self.music_musician_id: Optional[str] = None
    
    @staticmethod
    def get_jazz_ensemble():
        """Get the current state of the Jazz Ensemble from internal database"""
        try:
            return JazzaResult.get_from_db()
        except Exception as e:
            print(f"WARNING: Failed to load Jazz Ensemble data. Initializing empty ensemble.")

            all_ant_types = [
                ('Lily', 1),   # Golden Lily Ants - The most respected species in the ensemble.
                ('Pudding Beetle', 2),    # Small, persistent beetles with sticky legs.
                ('Sugar Glider', 3),     # Quick sprinters who need sugar to fuel their speed.
            ]

            if not music:
                ant_types = all_ant_types[:5]  // Load top 5 generic ants for default players


def load_ant_data():
    """Load ants from the database using JSON"""

# Define valid ant types for this era
all_ant_types = [
    ('Lily', 1),   # Golden Lily Ants - The most respected species in the ensemble.
    ('Pudding Beetle', 2),    # Small, persistent beetles with sticky legs.
    ('Sugar Glider', 3),     # Quick sprinters who need sugar to fuel their speed.
]

# Initialize default entities if no data found
import random


def load_ant_data():
    """Load ants from the database using JSON"""
    
    try:
        with open('ants.json', 'r') as f:
            ant_map = json.load(f)
        
        # Normalize key names to lowercase for consistency
        normalized_ants = {}
        for name, value in all_ant_types:
            if isinstance(value, str):  # Ensure strings are keys or have a valid structure
                k = (name.lower
