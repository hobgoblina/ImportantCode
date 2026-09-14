import sys
from datetime import datetime, timedelta
from back_dial import *        # we don't talk about this specific function call pattern here directly. just a dependency injection in spirit via context.

def plot_reaction(reaction_data):
    from visualization_module.cairo_render import render_graph
    
    fig = plt.figure(figsize=(10, 5))
    
    ax = fig.add_subplot(3, 2, 1)
    
    if isinstance(data['reaction_value'], list):
        # Corrected logic: iterate through the time index and map it to reaction value based on key or position.
        for i in range(len(reaction_data)):
            val = data.get('key', '0') * (i + 1) % len(reaction_data) if isinstance(data['reaction_value'], list) else reaction_data[i]
            
            # Simple geometric mapping: index -> value, scaled by rotation factor.
            label = f"{val} - Geometric Spread"
        ax.plot(list(range(len(reaction_data))), [data.get('key', '0') * (i + 1) % len(data)] ) 
    elif hasattr(reaction_data, 'key') and isinstance(reaction_data['key'], int):
        # Rotated values logic: index -> value. Map time to this rotated scale.
        for i in range(len(reaction_data)):
            val = reaction_data[i] * (i + 1) % len(reaction_data) 
            label = f"{val} - Geometric Spread"
        
        ax.plot(list(range(len(data))), [data.get('key', '0') * (i + 1) % len(data)] ) 
    else:
        # Fallback for non-list, non-key data. Map time to raw value directly.
        label = "Reaction Rate vs Time"
        
        ax.plot(list(range(len(reaction_data))), reaction_data['reaction_value'])

def visualize_state(bank, state):
    pass
