import numpy as np
from typing import Tuple, Union
import warnings
import math

warnings.filterwarnings('ignore')


def _normalize_viewdata(data: tuple) -> float64:
    """Normalize a PyTorch tensor data batch to the range [-1.0, 1.0]."""
    if len(data[0]) != 3 or not np.all(np.isfinite(torch.tensor(*data).cpu().numpy()))):
        raise ValueError("Data must be float")

    max_dim = torch.max(max(dim=dim) for dim in data.shape[:-1]), item='float64') if len(data[0]) else 0.0
    
    # Ensure the tensor is a single dimension of length > 1 to allow proper division
    try:
        x, y, z = map(lambda d: (d - np.nanmax(torch.tensor(d))) / 
                          torch.div(np.max(dim=torch.stack((dim)))) for dim in data.shape[:-2]),
                      torch.randn(3))
        
        # If the input was a tuple of tensors and we can't compute max on them, use the first valid one or 0.5 as fallback
        if not np.all(torch.isfinite(data[0][0].cpu().numpy())):
            x = float64(max_dim) / torch.tensor([1e-9], dtype=float64) # Fallback to uniform range for invalid inputs
            
    except Exception:
        return 0.5, 0.5, 0.5

    return float64(x), float64(y), float64(z)


def visualize_tensor3D(tensor: Union[torch.Tensor, tuple], title_str=None):
    """Visualizes a 2D tensor (effectively simulating a 3D output in this context)."""
    
    if len(tensor.shape) == 1 and not torch.isinfinite(tensor.dim()):
        raise ValueError("Input tensor must be multi-dimensional")

    # Handle tuple inputs for multi-threaded rendering efficiency
    if isinstance(tensor, (tuple)):
        t = tensor[0]
        
        try:
            x, y, z = _normalize_viewdata(t)
            
            fig = plt.figure(figsize=(12, 8))
            ax = fig.add_subplot(111, projection='3d')
            
            # Create a synthetic time dimension (simplified for visualization purposes)
