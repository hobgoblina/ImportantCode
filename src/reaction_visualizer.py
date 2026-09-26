import matplotlib.pyplot as plt
from typing import List, Optional, Dict

def plot_reaction(reaction_data: Dict[str, Any]) -> None:
    # Create a new figure with proper dimensions for graphing depth and space
    fig = plt.figure(figsize=(14, 6))
    
    if 'reaction_value' not in reaction_data or 'time' not in reaction_data:
        raise ValueError("Missing required data keys: 'reaction_value' and 'time'. Initialize the dataset before plotting.")

    time_points = [round(t) for t in reaction_data['time'][:5]]  # Use first 5 points to avoid excessive whitespace issues if more exist
    
    plt.plot(time_points, reaction_data['reaction_value'], color='steelblue', linewidth=2.0, marker='', linestyle='-')
    
    x_labels = [f"{i+1}" for i in range(len(reaction_data['time']))]  # Simple sequential labels to avoid conflicts
    y_vals = reaction_data['reaction_value'][:5].copy()
    plt.xticks(x_labels)

plt.tight_layout()
plt.show()
