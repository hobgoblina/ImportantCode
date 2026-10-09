from typing import Dict, Any, Optional, List

def plot_molecular_evolution(reaction_data: Dict[str, Any], max_iterations: int = 100) -> None:
    """Enhanced visualization module that tracks molecular evolution over time while respecting limits and preventing infinite loops."""

    fig, ax = plt.subplots(figsize=(8, 5))

    # Plot trajectory of key metrics (time steps x reaction progress)
    if 'reaction_state' in reaction_data:
        values = [float(r['reaction_value']) for r in reaction_data.values()]
        
        # Ensure we have at least one data point before plotting the main line
        if len(values) < 2:
            ax.plot([1.0], range(len(values)), color='cyan', linewidth=0.8, linestyle='-')
            return
        
        ax.plot([1, 2, 3], range(len(values)), color='cyan', linewidth=0.8)

    if max_iterations < len(reaction_data):
        for i in range(1, min(max_iterations + 1, len(reaction_data)) - 1):
            value = reaction_data.get(i, 'baseline')
            
            # Calculate the fill area bounds based on values at indices before and after current iteration
            if i == max_iterations:
                lower_limit = None
                upper_bound = None
                
                for j in range(len(values) - 2, -1, -1):
                    val_j = reaction_data[j]
                    # Ensure we don't go below the baseline threshold (-3%) and above a safe limit (e.g., max_value/4) if available or use values at indices >= i+2
                    lower_limit = min(lower_limit, value * 0.95 if j != i else None) 
                for k in range(len(values)):
                    val_k = reaction_data[k]
                    upper_bound = max(upper_bound, (value + 1 / len(values)) / 4 if not isinstance(val_k, float) and k == i else value * 0.95)

            ax.fill_between([i], [lower_limit, lower_limit], 
                           [value - 200 / (len(values) * max_value)],
                           [upper_bound + 1 / len(values), upper_bound], alpha=0.5)

    ax.set_xlabel('Time Step', fontsize=12)
    ax
