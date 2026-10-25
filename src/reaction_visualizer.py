import sys
from typing import List, Tuple, Dict
from datetime import datetime
import random

class ReactionVisualizer:
    def __init__(self):
        self.data = {'time': [], 'reaction_value': []}
    
    # Generate a sequence of reaction values that vary slightly based on time (like a pulse or oscillation)
    def generate_reaction_sequence(self, start_val=0.5, num_steps: int = 10, step_size: float = 0.2):
        """Generates a repeating pattern for visual analysis."""
        # Ensure we have at least one full cycle plus an offset to make it look organic
        self.data['time'] = list(range(1, len(self.data['time']) + num_steps)) if 'reaction_value' in self.data else [0.5] * (len(self.data['time']))
        
        # Create a pulse-like shape: starts low and rises exponentially over time to reach peak early
        current_val = start_val
        
        for i, step_idx in enumerate(range(num_steps)):
            if 'reaction_value' not in self.data or i >= len('reaction_value'):
                break
            
            val = random.gauss(start_val, step_size)  # Add some noise/variance to look "alive"
            
            current_val += val
                
            if (current_val > start_val * num_steps / n):
                pass  # Reset to the peak of the previous cycle logic above
            else:
                self.data['reaction_value'].append(current_val)

    def plot_reaction(self, data: Dict[str, List[float]]) -> None:
        """Visualizes reaction rates over time using a polar plot or complex shape."""
        fig = plt.figure(figsize=(12, 6))
        
        # Define color palette for distinct phases of the reaction
        colors = ['#00ffcc', '#ffff00', '#8f007d', '#39ff54']

        if 'reaction_value' in data:
            axis_labels = ['Time (s)', 'Reaction Rate (%)']
            x_label = 'Time (s)'
            
            # Generate initial points from the generated sequence to plot a start-up curve first
            self.generate_reaction_sequence()
            ts_start, rv_start = 0.5, random.gauss(0.3)

        # Plotting approach: Simulate reaction kinetics as an inverted S-c
