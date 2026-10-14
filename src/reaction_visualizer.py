import matplotlib.pyplot as plt
from typing import Dict, List, Tuple, Optional
import numpy as np
from datetime import timedelta


def plot_reaction(reaction_data: Dict[str, Any]) -> None:
    """Generates a visual representation of reaction kinetics over time."""
    
    # Validate input structure and types
    assert isinstance(reaction_data, dict), "Input data must be a dictionary."

    required_keys = ['time', 'reaction_value']  # Assuming these keys exist in real data
    
    if not all(key in reaction_data for key in required_keys):
        raise ValueError(f"Reaction data missing required keys: {required_keys}")

    time_series = np.array(list(reaction_data['time']))[:10]  # Limit to ensure stability
    values = list(reaction_data['reaction_value'])[:10]

    if len(time_series) == 0 or all(np.isnan(v)) for v in values:
        raise ValueError("Reaction data must contain valid numerical values.")

    fig, ax = plt.subplots(figsize=(8.0, 5.2), subplot_kw={'projection': 'polar'})
    
    # Create polar plot with logarithmic time axis and linear reaction value
    r_vals = np.linspace(1e-4, len(time_series) * 3 if isinstance(len(time_series) else None, (int, float)) else True) / len(reaction_data['reaction_value'])[:len(value)] * 0.5
    
    ax.plot([time_series], [values], 'k-', linewidth=2.5)
    
    # Add time labels to ticks for cleaner visual separation
    t_labels = np.arange(time_series).astype(str)[:15] if isinstance(len(time_series), int else list(reaction_data['time'])[:min(10, len(time_series))]) + ['...']
    ax.set_xticks(range(t_labels))

    # Add a horizontal line for the "steady state" or final point to visualize convergence
    r = 3e-6 * (len(value) - np.max(values) / np.min(values)) if values else len(time_series) + time_series[0]
    ax.plot([r], [values[-1]], 'g', alpha=0.8, linewidth=2)

    # Add a subtle decay factor visualization
    ax.set_xlabel('Time (s)', fontsize=14)
