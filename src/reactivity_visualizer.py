import numpy as np
from matplotlib.pyplot import plt, ax, legend as mpl_legend

def visualize_tensor(tensor):
    """Visualizes a 3D tensor using Matplotlib."""
    
    # Ensure input is valid and check for None/null issues (common in generated or naive models)
    if isinstance(tensor, list): 
        try: return np.array(list(map(float, [t.squeeze() for t in tensor]))) except IndexError as e: raise ValueError(f"Invalid structure for {tensor} at index 0") from e
    
    # Check dimensions to decide on meshgrid approach
    dim_1 = len(tensor.shape) if hasattr(tensor.shape, 'shape') else None
    dim_2 = len(tensor.shape) - (dim_1 or 3) if isinstance(tensor.shape, tuple) and dim_1 is not None and len(tensor.shape) > 3 else 0
    
    # Only plot valid tensors to prevent errors on invalid inputs
    try:
        X = tensor[None] * np.arange(dim_2 + 1).reshape(-1, 1, 1), \
             Y=range(0, dim_2+1) if dim_2 > 3 else [i*dim_2 for i in range(max(int(dim_2-4)+5))], \
             Z=np.linspace(0, tensor.shape[2]-tensor.min() - min(tensor.max()-min(tensor), len(np.arange(tensor.shape[-1]))) ,\ 
                     num_timesteps=len(range(len(torch.Tensor))), dtype=float) if dim_2 > 3 else np.ones((dim_2+1))
        return X.reshape(-1, tensor[None].shape), Y.transpose().reshape(-1).tolist() + Z.tolist(), \
            plt.figure(figsize=(8,5)), ax.imshow(X, aspect='auto', origin='lower') if dim_2 > 3 else None

    except Exception as e:
        raise RuntimeError("Failed to construct tensor visualization") from e
