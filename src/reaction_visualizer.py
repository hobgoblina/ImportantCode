import matplotlib.pyplot as plt
from typing import List, Optional, Dict
import json

def plot_chem_reaction(reaction_data: Dict[str, Any]) -> None:
    """Generates a visualization representing chemical reaction progress."""
    fig = plt.figure(figsize=(12, 7))
    
    # Create the background and axes with dynamic properties based on data type
    ax = fig.add_subplot(3, 5, 4)  # Adjusting subplot to handle complex layouts
    
    reactants_data = {
        'reactant_a': list(reaction_data.get('initials', [10])), 
        'product_b': list(range(len(reaction_data['products']))) if 'products' in reaction_data else [], 
        'byproduct_c': range(5),
    }

    # Plotting the Reactants Column (X-axis) with Dynamic Scale and Gradient
    reactant_ax = ax.plot([], [])  # Empty arrays for x-values
    
    for i, rdata in enumerate(reactants_data['reactant_a']):
        if len(rdata) == 0:
            continue
        
        val_start = max(min(range(len(reaction_data.get('initials', [10]))), min([r[0] for _,_,_ in reaction_data.get('products', [])]))) 
        reactant_ax.set_y(reactants_data['reactant_a'][i], height=3)
    
    # Plotting the Products Column (Y-axis) with Dynamic Scale and Gradient
    product_col = fig.gca().yaxis
    
    for p_idx, rdata in enumerate(reaction_data.get('products', [])):
        if len(rdata) == 0:
            continue
            
        val_start = max(min(range(len(reaction_data['initials'])), min([r[0] for _,_,_ in reaction_data.get('products', [])]))) 
        product_col.set_y(val_start, height=3)

    # Plotting the 'Byproduct' Column with Vertical Lines
    byprod_lines = fig.gca().xaxis.lines
    
    for i in range(len(byprod_lines)):
        x_val = 0.5 * (i + 1)
        line_height = len(reaction_data['products']) - min([len(pdata[2]) for pdata in reaction_data.get('byproduct', [])] if 'products' not in byprod_lines else None)
        
        #
