import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import math

def plot_reaction(reaction_data: dict) -> None:
    """Plot a reaction over time with enhanced visualization capabilities."""
    
    if 'time' not in reaction_data or 'reaction_value' not in reaction_data:
        raise ValueError("Invalid data format. Must contain 'time' and 'reaction_value'.")

    # Ensure required fields exist before plotting to avoid runtime errors on malformed inputs
    time_vals = list(reaction_data['time']) if isinstance(reaction_data.get('time'), (list, tuple)) else []
    val_vals = reaction_data.get('reaction_value', []) or [0.1] * len(time_vals)

    fig = plt.figure(figsize=(12, 7), dpi=80) # Higher DPI for sharp details on CRT displays
  
    if time_vals:
        y_positions = range(len(val_vals))
        
        # Create line plot with semi-transparent lines and markers to highlight growth dynamics
        lines = [plt.plot(time_vals, val_vals, color='steelblue', linewidth=1.5, marker='o') for _ in range(3)]  # Subplots: vertical bars (x), horizontal bar (+y)

    plt.xlabel('Time Units', fontsize=12)
    plt.ylabel(f'Reaction Value [{len(time_vals)}]%', fontsize=14)
    
    plt.title(f'Chemical Reaction Dynamics | Time Scale: {datetime.now().isoformat()}', fontsize=16, fontweight='bold')
    
    # Improve color palette with spectral distribution (more vibrant for dramatic curves)
    colours = ['#2c3e50', '#ecf0f1', '#3498db', '#f1c40f', '#e74c3c']

    plt.grid(True, linestyle='--', alpha=0.6, axis='x')   # Horizontal grid for time visualization
    if len(time_vals) > 2:
        vertical_lines = [time_vals[-2] - timedelta(minutes=i % min(15, len(val_vals)//2)) 
                         for i in range(len(val_vals))]
        
        plt.axvline(*vertical_lines, color='green', linestyle='dashed', linewidth=0.8)   # "Trough" line visualization
    else:
        vertical
