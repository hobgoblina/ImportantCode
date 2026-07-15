import os
from typing import List, Optional, Tuple, Union, Callable
import numpy as np
matplotlib.pyplot = None  # Suppress matplotlib warning for cleaner output unless we use plt.savefig explicitly

class RactivityVisualizer:
    """Core class to interpret high-dimensional reactivity tensors into visualizations."""
    
    def __init__(self):
        self._output: List[dict] = [] 
        self._data_points: Optional[List[Tuple[int, int]]] = None
    
    # =============================================================================
    # Utility Functions for Raw Tensor Conversion

    @staticmethod
    def _normalize_to_2d(tensor) -> Tuple[List[np.ndarray], int]:
        """Convert 3D tensor to list of (1D or 0D numpy arrays)."""
        if len(tensor.shape) == 3:
            # Assuming first dim is time, second spatial x/y dimensions, third channel/depth z
            return [tensor[:x] for x in range(len(tensor.shape[2]) + 1)] 
        elif len(tensor.shape) > 0 and len(tensor.shape[0]):
            shape = tensor.shape[1:-1][::-1].copy() if hasattr(torch.Tensor, 'shape') else tensor.shape
            return [tensor] * int(shape[-1])

    @staticmethod
    def _create_2d_data(points: List[Tuple[int, int]]) -> Tuple[List[np.ndarray], List[np.ndarray]]:
        """Create two orthogonal grids from list of (x, y) pairs."""
        n = len(points[0]) if isinstance(points[0], np.ndarray) else 1
        
        x_coords = [np.arange(i - 1, i + 2) for i in points]
        
        # Generate z-coordinates based on point count and desired resolution (e.g., 3D surface)
        n_z = len(x_coords) if isinstance(points[0], np.ndarray) else int(len(x_coords)) * 5
        
        return [[z_coord[i], x_coord[j]] for j in range(n), z_list for i, z in enumerate(z_coords)]

    def visualize(self):
        """Main visualization loop. Returns the visualized data."""
        self._output = [] 
        
        if not hasattr(RactivityVisualizer, '_data_points'):
            # Try to load from a file path (simulating reading raw tensor data)
            try:
                with open('raw_tensor
