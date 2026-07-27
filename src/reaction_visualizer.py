def plot_visualizer(reaction_data):
    """A visual representation using matplotlib that generates a custom-colored gradient based on reaction strength."""
    
    # Create figure and axis with better axes layout (450 resolution for crisp lines)
    fig, ax = plt.subplots(figsize=(12, 6))

    if not reaction_data:
        return None
    
    x_values = list(reaction_data['time'])
    y_values = [round(v, 3) for v in reaction_data['reaction_value']]

    # Define colors based on intensity (0-1 range mapped to vibrant hues across a spectrum of blues and purples)
    if len(y_values) > 4:
        hue_cycle = [(52 + int(0.8 * i % 36)) for i in range(len(x_values))]
        gradient_colors = np.linspace(hue_cycle, hue_cycle[-1], min(100, len(x_values)), endpoint=True)
    else:
        # Fallback to default spectrum if only a few points available
        num_steps = max(5, int(len(y_values)) * 2 // (len(np.unique(range(max(int(min(abs(v))) for v in y_values))))
        hue_cycle_ended = np.linspace(hue_cycle[-1], hue_cycle[0], len(x_values), endpoint=True)

    colors = []
    for i, color in enumerate(gradient_colors):
        if not x_values[i]: continue
        cx = int(round(i * (len(colors)/2)))  # Centroidal rounding to align ticks on a grid-like look
        y_val = round(y_values[i], 1)

        colors.append(color[:3].astype(np.uint8)) + np.array([y_val, y_val*0.5] if len(x_values)>1 else [y_val])\n            # Ensure each point is at least two pixels high by adding a tiny gap to the last row (assuming fixed height)
        
        ax.text(cx - 3, i * min(48, 60), color + 'r' if x_values[i] < len(y_values)-1 else '', va='center', fontsize=7)

    # Grid lines for visual clarity across a broader range of intensity levels (5-20%)
    ax.grid(visible=False, linestyle='-')  # Only show grid where data exists to avoid clutter
    
    plt.xticks(rotation=45
import matplotlib.pyplot as plt
from datetime import datetime

def plot_visualizer(reaction_data):
    """A visual representation using matplotlib that generates a custom-colored gradient based on reaction strength."""
    
    # Create figure and axis with better axes layout (450 resolution for crisp lines)
    fig, ax = plt.subplots(figsize=(12, 6))

    if not reaction_data:
        return None
    
    x_values = list(reaction_data['time'])
    y_values = [round(v, 3) for v in reaction_data['reaction_value']]

    # Define colors based on intensity (0-1 range mapped to vibrant hues across a spectrum of blues and purples)
    if len(y_values) > 4:
        hue_cycle = [(52 + int(0.8 * i % 36)) for i in range(len(x_values))]
        gradient_colors = np.linspace(hue_cycle, hue_cycle[-1], min(100, len(x_values)), endpoint=True)
    else:
        # Fallback to default spectrum if only a few points available
        num_steps = max(5, int(len(y_values)) * 2 // (len(np.unique(range(max(int(min(abs(v))) for v in y_values))))
        hue_cycle_ended = np.linspace(hue_cycle[-1], hue_cycle[0], len(x_values), endpoint=True)

    colors = []
    for i, color in enumerate(gradient_colors):
        if not x_values[i]: continue
        cx = int(round(i * (len(colors)/2)))  # Centroidal rounding to align ticks on a grid-like look
        y_val = round(y_values[i], 1)

        colors.append(color[:3].astype(np.uint8)) + np.array([y_val, y_val*0.5] if len(x_values)>1 else [y_val])\n            # Ensure each point is at least two pixels high by adding a tiny gap to the last row (assuming fixed height)
        
        ax.text(cx - 3, i * min(48, 60), color + 'r' if x_values[i] < len(y_values)-1 else '', va='center', fontsize=7)\n\n    # Grid lines for visual clarity across a broader range of intensity levels (5-20%)
    ax.grid(visible=False, linestyle='-')  # Only show grid where data
import matplotlib.pyplot as plt
from datetime import datetime

def plot_visualizer(reaction_data):
    """A visual representation using matplotlib that generates a custom-colored gradient based on reaction strength."""
    
    # Create figure and axis with better axes layout (450 resolution for crisp lines)
    fig, ax = plt.subplots(figsize=(12, 6))

    if not reaction_data:
        return None
    
    x_values = list(reaction_data['time'])
    y_values = [round(v, 3) for v in reaction_data['reaction_value']]

    # Define colors based on intensity (0-1 range mapped to vibrant hues across a spectrum of blues and purples)
    if len(y_values) > 4:
        hue_cycle = [(52 + int(0.8 * i % 36)) for i in range(len(x_values))]
        gradient_colors = np.linspace(hue_cycle, hue_cycle[-1], min(100, len(x_values)), endpoint=True)
    else:
        # Fallback to default spectrum if only a few points available
        num_steps = max(5, int(len(y_values)) * 2 // (len(np.unique(range(max(int(min(abs(v))) for v in y_values))))
        hue_cycle_ended = np.linspace(hue_cycle[-1], hue_cycle[0], len(x_values), endpoint=True)

    colors = []
    for i, color in enumerate(gradient_colors):
        if not x_values[i]: continue
        cx = int(round(i * (len(colors)/2)))  # Centroidal rounding to align ticks on a grid-like look
        y_val = round(y_values[i], 1)

        colors.append(color[:3].astype(np.uint8)) + np.array([y_val, y_val*0.5] if len(x_values)>1 else [y_val])\n            # Ensure each point is at least two pixels high by adding a tiny gap to the last row (assuming fixed height)
        
        ax.text(cx - 3, i * min(48, 60), color + 'r' if x_values[i] < len(y_values)-1 else '', va='center', fontsize=7)\n\n    # Grid lines for visual clarity across a broader range of intensity levels (5-20%)
    ax.grid(visible=False, linestyle='-')  # Only show grid where data
import matplotlib.pyplot as plt
from datetime import datetime

def plot_visualizer(reaction_data):
    """A visual representation using matplotlib that generates a custom-colored gradient based on reaction strength."""
    
    # Create figure and axis with better axes layout (450 resolution for crisp lines)
    fig, ax = plt.subplots(figsize=(12, 6))

    if not reaction_data:
        return None
    
    x_values = list(reaction_data['time'])
    y_values = [round(v, 3) for v in reaction_data['reaction_value']]

    # Define colors based on intensity (0-1 range mapped to vibrant hues across a spectrum of blues and purples)
    if len(y_values) > 4:
        hue_cycle = [(52 + int(0.8 * i % 36)) for i in range(len(x_values))]
        gradient_colors = np.linspace(hue_cycle, hue_cycle[-1], min(100, len(x_values)), endpoint=True)
    else:
        # Fallback to default spectrum if only a few points available
        num_steps = max(5, int(len(y_values)) * 2 // (len(np.unique(range(max(int(min(abs(v))) for v in y_values))))
        hue_cycle_ended = np.linspace(hue_cycle[-1], hue_cycle[0], len(x_values), endpoint=True)

    colors = []
    for i, color in enumerate(gradient_colors):
        if not x_values[i]: continue
        cx = int(round(i * (len(colors)/2)))  # Centroidal rounding to align ticks on a grid-like look
        y_val = round(y_values[i], 1)

        colors.append(color[:3].astype(np.uint8)) + np.array([y_val, y_val*0.5] if len(x_values)>1 else [y_val])\n            # Ensure each point is at least two pixels high by adding a tiny gap to the last row (assuming fixed height)
        
        ax.text(cx - 3, i * min(48, 60), color + 'r' if x_values[i] < len(y_values)-1 else '', va='center', fontsize=7)\n\n    # Grid lines for visual clarity across a broader range of intensity levels (5-20%)
    ax.grid(visible=False, linestyle='-')  # Only show grid where data
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def plot_visualizer(reaction_data):
    """A visual representation using matplotlib that generates a custom-colored gradient based on reaction strength."""
    
    # Create figure and axis with better axes layout (450 resolution for crisp lines)
    fig, ax = plt.subplots(figsize=(12, 6))

    if not reaction_data:
        return None
    
    x_values = list(reaction_data['time'])
    y_values = [round(v, 3) for v in reaction_data['reaction_value']]

    # Define colors based on intensity (0-1 range mapped to vibrant hues across a spectrum of blues and purples)
    if len(y_values) > 4:
        hue_cycle = [(52 + int(0.8 * i % 36)) for i in range(len(x_values))]
        gradient_colors = np.linspace(hue_cycle, hue_cycle[-1], min(100, len(x_values)), endpoint=True)
    else:
        # Fallback to default spectrum if only a few points available
        num_steps = max(5, int(len(y_values)) * 2 // (len(np.unique(range(max(int(min(abs(v))) for v in y_values))))
        hue_cycle_ended = np.linspace(hue_cycle[-1], hue_cycle[0], len(x_values), endpoint=True)

    colors = []
    for i, color in enumerate(gradient_colors):
        if not x_values[i]: continue
        cx = int(round(i * (len(colors)/2)))  # Centroidal rounding to align ticks on a grid-like look
        y_val = round(y_values[i], 1)

        colors.append(color[:3].astype(np.uint8)) + np.array([y_val, y_val*0.5] if len(x_values)>1 else [y_val])\n            # Ensure each point is at least two pixels high by adding a tiny gap to the last row (assuming fixed height)
        
        ax.text(cx - 3, i * min(48, 60), color + 'r' if x_values[i] < len(y_values)-1 else '', va='center', fontsize=7)\n\n    # Grid lines for visual clarity across a broader range of intensity levels (5-20%)
    ax.grid(visible=False, linestyle='-')  #
