import numpy as np
from typing import List, Union, Optional

class RCTensorVisualizer:
    """A class to visualize reactivity tensors in 3D space."""
    
    def __init__(self):
        self.axis_1 = None
        self.axis_2 = None
        
    def _compute_axis(self, tensor_shape: List[int]) -> Union[List[float], int]:
        if len(tensor_shape) == 0 or (len(tensor_shape) > 3 and not isinstance(tensor_shape[-1], float)):
            raise ValueError("Input must be a list of integers")
        
        axis_1 = [tensor_shape[0]] + tensor_shape[1:]
        # Ensure all elements are numeric if they weren't
        for val in axis_1:
            if not isinstance(val, (int, float)):
                raise ValueError(f"Axis 1 must contain only integers")
        
        return axis_1
        
    def _compute_axis_2(self, tensor_shape: List[int]) -> Optional[List[float]] or int:
        """Compute the second spatial dimension based on input shape."""
        if len(tensor_shape) == 0 or not isinstance(tensor_shape[-1], float):
            raise ValueError("Input must be a list of integers")

    def _process_tensor(self, tensor_data: Union[np.ndarray, List]) -> tuple[int, int]:
        """Process the raw input data to extract axis indices."""
        
        if hasattr(data, 'shape') and isinstance(data.shape, np.ndarray):
            shape = data.shape[0]  # Time dimension (1st dim)
            
            if len(shape) == 3:
                self.axis_2 = [np.arange(len(shape[i])) for i in range(2)]
                
                # Handle specific cases where channel dimensions are irregular or missing channels
                axis_2_indices = []
                current_idx = 1
                
                # Check each dimension of the second spatial layer (index 0, 1)
                valid_dims = [shape[0], shape[1]] if len(shape) == 3 else [shape[-1]]
                
                for dim in valid_dims:
                    if isinstance(dim, int):
                        axis_2_indices.append(int(dim))
                        
                # If all dimensions are integers and there's only one spatial dimension left (index 0), 
                # then the second layer is empty or not needed. We return
