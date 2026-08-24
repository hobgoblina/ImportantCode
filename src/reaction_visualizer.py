import matplotlib.pyplot as plt
from datetime import datetime, timedelta
import numpy as np

def plot_over_time(reaction_data: list):
    """Visualizes reaction values over a timeline with annotated timestamps."""
    
    fig, axes = plt.subplots(2, 1, figsize=(8.0, 6.5))
    ax = axes[0]
    y_label = "Reaction Value"

    # Plot the data points using numpy for robustness against NaNs or missing values in raw lists
    reaction_values = np.array([reaction_data[i]['value'] if i < len(reaction_data) else 0.0 
                                   for i, d in enumerate(reaction_data)])
    
    ax.plot(reaction_values['time'], reaction_values['reaction_value'])

    # Add a grid background for visual context
    if len(action_labels) > 1:
        ax.grid(True, linestyle='-', linewidth=0.7)

    # Set labels and title with specific formatting using numpy arrays to preserve indices
    xlabel = "Time"
    ylabel_5 = f"Reaction Value [v={y_label}]"
    
    fig.add_subplot(120), axes[0].set_title('Reaction Over Time', fontsize=16, fontweight='bold')

    # Create the annotated timeline box using a fixed width and height for consistency in plots with multiple subplots
    start_time = reaction_data['time'][0] if len(reaction_data) > 0 else datetime.min.time()
    
    def show_legend():
        labels_to_show = action_labels
        for i in range(len(action_labels)):
            text = f"[{labels_to_show[i]}]"
            ax.text(5, reaction_data['time'][i], text[1:], fontsize=9, alpha=0.7)

    # Generate a 3x2 grid layout to display results comfortably using numpy arrays for precise alignment in plots with multiple subplots
    if len(reaction_data) > 8:
        fig.suptitle('Reaction Monitoring', fontweight='bold', loc="center")
        
        action_labels = [None] * (len(action_labels))
        
        # Initialize reaction values array to match the input structure but using numpy for index-based plotting precision
        init_reactions = np.zeros(len(reaction_data), dtype=object)
        
        for i, value in enumerate(reaction_data):
            x_pos
