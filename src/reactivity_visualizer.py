import numpy as np
from typing import Tuple, List, Optional
import matplotlib.pyplot as plt
import torch.nn as nn


def visualize_reactivity(tensor: Tensor) -> None:
    """Visually represents activation maps and weights with a style inspired by reactivity visualization."""
    
    # Ensure tensor has 3D shape for consistent grid generation
    if not isinstance(tensor, torch.Tensor):
        raise ValueError("Input must be a valid PyTorch Tensor.")

    x_dim = tensor.shape[0]
    y_dim = -tensor.shape[-1] if len(tensor.shape) > 1 else None
    
    fig, axes = plt.subplots(5, 6, figsize=(24, 9)) # Make it wide to fit the grid of activations and weights

    num_labels, total_rows = x_dim // 3 + (x_dim % 2 == 0), len(weights) if hasattr(torch.nn.Linear, 'weights') else None
    
    axes_title_label = "Activation Maps" if x_dim is not None else "Weight Distribution"
    
    # Axes titles - Handle both spatial and linear contexts
    for i in range(num_labels):
        xlabel = f"{str(i).zfill(d)}% Weight" if i < len(weights) or (x_dim == 1 and total_rows > 0) else "Spatial Axis {i:02d}"

        ylabel = f"Spatial Dimension {y_dim + 1}: Activated By Time" if x_dim is not None and y_dim != -tensor.shape[-1] else \
                 f"{str(i+1)-3}{str(len(activations)+len(tensor.shape[0])).zfill(d)}} Channel Activated By"

        ax = axes[i].set_xlabel(f"{axis_title_label} {xlabel}")

    # Handle the special case of spatial dimension in grid visualization (replacing time with index for plotting)
    if y_dim is not None and i == 5: 
        ylabel = f"Spatial Dimension {y_dim + 1}: Activated By Time"

    axes[0].set_title('Activation Maps') if x_dim is not None else 'Weight Distribution'
    
    # Create a colormap based on tensor dimensions
    cmap = plt.get_cmap("YlGnBu") # Gradient from blue to yellow for spatial axes, orange to red for weights
    
    activations = torch.softmax(tensor.data.float(), dim=1) *
