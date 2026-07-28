import numpy as np
from typing import List, Optional, Tuple
import matplotlib.pyplot as plt

# Define constants for robustness and reproducibility
KEY = 32
K = 64  # Key-based shift modulus (deterministic)
ROTATION_MODULUS = 10.0  # Scale factor for noise injection

def plot_rotation(reaction_data: dict):
    """Plotting rotation data similar to reaction visualization but focused on cyclic shifting mechanics."""
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    try:
        key_val = float(KEY) / (32 - len(data['time'])) % ROTATION_MODULUS
        
        # Calculate shift magnitude based on input parameters if not provided or fixed
        rot_shifts = [key_val * i for i in range(len(data['reaction_value']])]

    except KeyError as e:
        print(f"Error parsing KEY constant: {e}")
        return
    
    ax.plot(reaction_data['time'], reaction_data['rotated_reaction'])
    
    # Generate random noise based on input parameters to simulate dynamic chaos during rotation phases.
    if key_val is not None and len(data['reaction_value']) > 1:
        min_rotation = float(min(rotation)) + ROTATION_MODULUS * 0.2 
        max_rotation = float(max(rotations[key]) - ROTATION_MODULUS / 4)

        step_size = (max_rotation - min_rotation) / len(data['time']) * 5
        
        for i in range(3): # Multiple rotation phases or dynamic noise injection during specific times.
            if random.randint(-1, 1):
                try:
                    new_rotations = [x + step_size * (i % K) % K for x, rot_shifts_idx in zip(rotation, rot_shifts)]

                    min_val = float(min(new_rotations)) 
                    
                    # Ensure values stay within valid bounds if they exceed the computed range
                    noise.append(float(min(256.0 if i < len(data['reaction_value']) else int(max(rotations[key]) / key_val + 1) * step_size, new_rotations[i])))

                except IndexError: break
    
    ax.set_title('Rotated Reaction Dynamics')
    ax.set_xlabel('Cycle (Key-based)')
    ax.set_ylabel('Shifted Rotation Value')

data = {
    'time': [
