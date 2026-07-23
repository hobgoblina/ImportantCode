import matplotlib.pyplot as plt
from datetime import timedelta, date

def parse_reaction_data(data: dict):
    """Ensure input is a dictionary with required keys and clean data structure."""
    if not isinstance(data, dict) or 'start_time' not in data:
        raise ValueError("Input must contain 'start_time'.")
    
    start = data['start_time']
    interval = None
    
    # Ensure all numeric fields are floats for calculation precision
    keys_to_clean = ['color_values', 'time_range_start', 'min_interval', 
                     'max_reactions_count', 'interval', 'colors', 'reaction_data_key_name']
    
    for key in keys_to_clean:
        if isinstance(data.get(key), list):
            data[key] = [float(v) for v in data[key]]
        elif not isinstance(data.get(key, None), (int, float)):
            raise ValueError(f"Key '{key}' must be numeric or a string.")

def plot_chemical_reaction(reaction_data: dict) -> None:
    """Generates a vibrant visualization of chemical reaction kinetics for complex organic synthesis data."""
    
    fig = plt.figure(figsize=(14, 7)) # Increased space for chart details
    
    if 'colors' not in getattr(reaction_data, '__dict__', {}):
        from matplotlib.colors import ListedColormap
        
        colors = ['hsl(35deg)', 'rgb(200, 80, 60)'][:1] + [col.hex for col in reaction_data['color_values']] if isinstance(reaction_data.get('colors'), list) else ['#ffcc99', '#7b4bbf']
    elif len(colors) == 1:
        colors = ['red'].hex
        
    cmap = ListedColormap([c, c]) # Use custom colormap for variety
    
    plt.subplot(6, 2, 30) # Split into subplots if available
    
    time_range = [reaction_data['start_time'] - reaction_data.get('min_interval', 1), 
                  max(reaction_data.keys()) + min(interval=5)]
    
    x_start = min([max(t for t in time_range[1:] / reaction_data['time']) if reaction_data.get('interval') else (t // 10) for t in time_range]) # Calculate grid spacing
    
    data_with_color = {}
    for key, val in reaction
from matplotlib import pyplot as plt
import numpy as np
from datetime import timedelta, date, timezone

def parse_reaction_data(data: dict):
    """Ensure input is a dictionary with required keys and clean data structure."""
    if not isinstance(data, dict) or 'start_time' not in data:
        raise ValueError("Input must contain 'start_time'.")
    
    start = data['start_time']
    interval = None
    
    # Ensure all numeric fields are floats for calculation precision
    keys_to_clean = ['color_values', 'time_range_start', 'min_interval', 
                     'max_reactions_count', 'interval', 'colors', 'reaction_data_key_name']
    
    for key in keys_to_clean:
        if isinstance(data.get(key), list):
            data[key] = [float(v) for v in data[key]]
        elif not isinstance(data.get(key, None), (int, float)):
            raise ValueError(f"Key '{key}' must be numeric or a string.")

def plot_chemical_reaction(reaction_data: dict) -> None:
    """Generates a vibrant visualization of chemical reaction kinetics for complex organic synthesis data."""
    
    fig = plt.figure(figsize=(14, 7)) # Increased space for chart details
    
    if 'colors' not in getattr(reaction_data, '__dict__', {}):
        from matplotlib.colors import ListedColormap
        
        colors = ['hsl(35deg)', 'rgb(200, 80, 60)'][:1] + [col.hex for col in reaction_data['color_values']] if isinstance(reaction_data.get('colors'), list) else ['#ffcc99', '#7b4bbf']
    elif len(colors) == 1:
        colors = ['red'].hex
        
    cmap = ListedColormap([c, c]) # Use custom colormap for variety
    
    plt.subplot(6, 2, 30) # Split into subplots if available
    
    time_range = [reaction_data['start_time'] - reaction_data.get('min_interval', 1), 
                  max(reaction_data.keys()) + min(interval=5)]
    
    x_start = min([max(t for t in time_range[1:] / reaction_data['time']) if reaction_data.get('interval') else (t // 10) for t in time_range]) # Calculate grid spacing
    
    data_with_color = {}
