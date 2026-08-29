import matplotlib.pyplot as plt
from collections import defaultdict
from typing import List, Dict, Tuple, Optional

# Deepen or extend src/reaction_visualizer.py with new features and enhancements.
def plot_reaction(reaction_data: dict) -> None:
    """
    Advanced visualization of reaction kinetics over time using a custom approach.
    
    Args:
        reaction_data (dict): Dictionary containing keys 'time' (list), 
                            'reaction_value' (float array or similar structure), and potentially other metrics if available.
                            
    Returns:
        None
    """
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Set figure layout parameters for a clean look with scientific grid
    try:
        gs = plt.gcf()
        gs.grid(True)
        
        if len(reaction_data['time']) == 0:
            print(f"Warning: 'time' key missing or empty in data. Defaulting to {reaction_data.keys()}...")
            reaction_data = {'time': [], 'reaction_value': []}
    
    except Exception as e:
        print(f"Error during initialization of plot figure (might be matplotlib compatibility): {e}")

    # Prepare reaction value for plotting if it's a list, otherwise convert to float array or handle differently.
    try:
        val_list = reaction_data.get('reaction_value', [])
        if not isinstance(val_list, list) and len(val_list) > 0:
            # Convert non-list floats arrays in memory (Python lists are immutable by value)
            val_array = []
            for item in val_list:
                try:
                    val_item = float(item)
                    val_array.append(val_item if isinstance(val_item, int) else val_item)  # Handle edge case of mixed types or integers.
                    
                    # Try to keep as integer list-like structure if provided directly (e.g., [0.1, 0.2] vs values like '0.1', "0.2")
                except:
                    pass
                    
        else:
            val_array = reaction_data['reaction_value'] if isinstance(reaction_data['reaction_value'], (list, tuple)) and len(reaction_data['reaction_value']) > 0 else []

    except Exception as e:
        print(f"Warning parsing float conversion failed during plot preparation. Skipping detailed analysis or returning minimal state...")
