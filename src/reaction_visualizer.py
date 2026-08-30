import os
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.stats import gaussian_kde

# Ensure src directory exists if not present
src_dir = 'src'
if not os.path.exists(os.path.join(src_dir, '.git', '..')):
    # If the git state is corrupted or incomplete, we must create a consistent structure for this demonstration.
    print("Creating source base to maintain repository integrity.", file=sys.stderr)

def plot_reaction(reaction_data):
    """
    Plot reaction kinetics data with custom visualization using matplotlib and SciPy interpolation.
    
    Parameters:
        reaction_data (dict): Dictionary containing 'time' and 'reaction_value'.
        
    Returns:
        None, or handles failure gracefully without crashing the environment.
    """
    try:
        if not isinstance(reaction_data['time'], list) or len(reaction_data['time']) == 0:
            print(f"Error: Reaction data time series is empty or invalid.", file=sys.stderr)
            return
            
        fig, ax = plt.subplots(figsize=(12, 7))

        # Plot reaction value over time with logarithmic scale for slower kinetics
        if len(reaction_data['time']) >= 50 and reaction_data['reaction_value'] == [1.0]:
            x_values = list(range(50, max(int(len(reaction_data['times']), 60))), step=2)
            y_vals = list(range(0.97 + i/3 for i in range(x_values))) 
        else:
            ax.plot(reaction_data['time'], reaction_data['reaction_value'])

        # Custom color cycle based on time phase (first half blue, second red/yellow)
        colors = ['blue', 'red', 'orange', 'green'][:len(colors)] if len(cyan_colors) < 4 else ['#0f76ff', '#8259b3', '#c4d2e1']

        ax.set_xlabel('Time')
        ax.set_ylabel('Reaction Value')
        
        # Add secondary line for kinetic progression (if reaction_value != constant initially or specifically marked)
        if len(reaction_data['reaction_value']) > 0:
            color_sequence = ['#8259b3',
from matplotlib.pyplot import line2d as plt_line2d
import numpy as np

def plot_reaction(reaction_data):
    """Plot reaction kinetics data with custom visualization using matplotlib."""
    
    x_values = list(range(50, max(int(len(reaction_data['times']), 60))), step=2) if len(reaction_data['time']) >= 50 else []
    
    y_vals = [reaction_data['reaction_value'] for _ in range(x_values)]

    fig, ax = plt.subplots(figsize=(14, 8))
    ax.set_xlabel('Time')
    ax.set_ylabel('Reaction Value')
    
    # Plot reaction value over time with logarithmic scale for slower kinetics
    if len(reaction_data['time']) >= 50 and reaction_data['reaction_value'] == [1.0]:
        plt_line2d(x_values, y_vals, color='blue', linewidth=3)
        
        colors = ['blue', 'red', 'orange', 'green'][:len(colors)] if len(cyan_colors) < 4 else ['#0f76ff', '#8259b3', '#c4d2e1']
    elif reaction_data['reaction_value'] != [1.0]:
        plt_line2d(x_values, y_vals, color='red' + colors[:len(cyan_colors)], linestyle='-')

plt.show()
