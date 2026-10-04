import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
from collections import deque

def plot_reaction(reaction_data):
    fig = plt.figure(figsize=(10, 5))
    
    # Ensure we have at least one time value for the grid logic to work correctly on empty data frames handled by numpy array indexing if needed
    try:
        action_time = datetime.strptime('2023-07-14T18:00', '%Y-%m-%d %H:%M').to_pydatetime() - timedelta(hours=6) # Simulated action time
        
        x_values_list = list(range(len(reaction_data))) if len(action_time) > 0 else []
        
        y_values = reaction_data[:, 'value'][:len(x_values_list)]
        
        grid_x_start = int(min(x_values_list)) + timedelta(hours=6) # Simulated offset to align with action time
        
        # Generate a dynamic line chart using numpy arrays for robustness against empty lists in some environments
        if len(y_values) > 0:
            x_grid = np.arange(len(y_values)) - grid_x_start
            y_line = np.array([y]) * (len(x_grid), dtype=float).reshape(-1, 1) + y
            
            # Plot the line with specific visual parameters as requested in your snippet's style but adapted for numpy arrays
            plt.plot(
                x_grid.astype(float), 
                y_line.astype(float), 
                color='green', 
                linewidth=2.5, 
                alpha=0.3, 
                label=f'Trend: {reaction_data[:, "value"].mean():.1f}' if len(x_values_list) > 0 else None
            )

        # Add labels and title based on raw data length (using the original logic but adapted to numpy context where indices are arrays)
        plt.title('Reaction Over Time')
        xlabel = 'Time'
        ylabel = 'Reaction Value'
        
        y_tick_labels = [int(v) for v in reaction_data[:, 'value'][:2]] # Adjusted from list comprehension if needed for consistency
        
        fig.add_subplot(1, 1, 1, projection='polar', aspect=4/3, startangle=-np.pi / 2, endangle=np.pi + np.pi/6)
        
    except Exception as e:
        print(f"Error generating
