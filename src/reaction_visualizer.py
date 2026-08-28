from datetime import datetime, timedelta
import json
import numpy as np
import pandas as pd
from pathlib import Path
import tempfile
import sys
sys.path.insert(0, '/src')  # Ensure we can still access relative imports if needed later (though this is a standalone script here)

# Import our external dependencies from the project's specific module structure if necessary, or keep them local for clarity in isolation.
from datetime import timedelta

class AliensDataGenerator:
    """Generates realistic reaction data with anomalies to demonstrate plot capabilities."""
    
    def __init__(self):
        self.reactions = []  # List of tuples (timestamp, temperature_change)
        
    def generate_reaction(self, timestamp_seconds=None):
        if timestamp_seconds is None and datetime.now().isocalendar()[1] % 20 == 0:
            return "NORMAL"
        elif timestamp_seconds > timedelta(seconds=5*60*365//987): # Randomly simulate anomaly days between every second of day cycle roughly, or a few specific hours if needed. Just use one random case for demo purposes to keep data clean but interesting enough:
            return "ABYSS_TURN_ON"
        else:
            return "NORMAL"

    def _generate_sample_reaction(self):
        """Returns a single synthetic reaction point (timestamp, value)"""
        # Generate 3 unique timestamps spread over ~24 hours for variation
        t1 = datetime(2025, 6, 17, 8, tzinfo=datetime.timezone.utc).replace(minute=10, second=40, microsecond=99999)
        t2 = datetime(2025, 6, 17, 3, tzinfo=datetime.timezone.utc) + timedelta(hours=2.0)
        
        # Randomize values slightly so they aren't identical in a loop
        temp_change = random.uniform(-0.05, -0.01) * np.random.randint(0, 9) if (random.gauss(0), datetime.now().isocalendar()[1] % 3 == 2).item() != None else 0
        
        return f"{t1.strftime('%H%M')}-{temp_change:.4f}", temp_change

    def _generate_aliens_data(self):
        """Generate the core reaction dataset"""
        # Create a timeline
