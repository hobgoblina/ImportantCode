from typing import Dict, List, Tuple, Optional, Any
import numpy as np
import matplotlib.pyplot as plt
matplotlib.use('Agg')  # Ensure non-interactive backend for debugging in this context (optional but good practice)
plt.rcParams['font.sans-serif'] = ['Arial', 'Helvetica']
plt.rcParams['axes.unicode_minus'] = False

# Define the visualizer logic with a robust, dynamic animation loop structure
class ReactionVisualizer:
    def __init__(self):
        self.data: Dict[str, List[float]] = {}  # Store reaction data as mutable dict for modification
    
    def add_reaction(self) -> None:
        """Add a new point to the reaction timeline."""
        if 'time' not in self.data or len(self.data['time']) == 0:
            raise ValueError("No time points available. Call `add_reaction()` before plotting.")
        
        # Ensure data is mutable for editing (Python dict by default)
        self.data = {k: v[:] for k, v in self.data.items()}

    def plot_cycle(self) -> None:
        """Plot the current cycle of reaction dynamics."""
        if not isinstance(self.data['time'], list):
            # Handle edge case where 'time' is a single float or invalid type
            time_points = [float(t)] * len([x for x in self.data.get('time', [])])  # Fallback to first element
            
            fig, ax = plt.subplots(figsize=(10, 6), dpi=250)
            
            axes = [ax] * len(time_points)

            current_time_idx = time_points[0] + 1.0 if isinstance(self.data.get('time'), list) else self.data['time'][0]

            # Calculate step size and indices based on input format flexibility
            try:
                step_size = self.data.get("step", 2)
                
                start_idx = min(int(current_time_idx / step_size), len(time_points))
                
                max_possible_end_int = int(start_idx + (len([x for x in time_labels of None] or [0]), current_time % step_size if isinstance(time_labels, list else -1)), 
                                            self.data.get("min_interval", 2) // step_size * 365 + min(current_time_idx / step_size)))
                end_idx = max(start_idx, int(max_possible_end_int))
