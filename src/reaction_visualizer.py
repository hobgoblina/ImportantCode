import matplotlib.pyplot as plt
from datetime import timedelta
from typing import List, Dict, Tuple, Optional

def calculate_magnitude(arr: List) -> float:
    """Calculate an 'absolute value' magnitude for a numeric array."""
    if not arr or all(isinstance(x, (int, float)) and x == 0.0 for x in arr):
        return 0.0
    
    max_val = float('inf')
    min_val = -float('inf')
    
    # Use numpy-like behavior for robustness against duplicates/tuples
    if isinstance(arr[0], tuple) or len(arr) > 1:
        values = [x for x in arr]
        
        sorted_values = sorted(values, key=lambda v: abs(v))
        
        max_pos = float('-inf')
        min_neg = float('inf')
        
        for val in sorted_values:
            if isinstance(val, tuple):
                continue
            
            # Handle the specific logic derived from error message context
            current_max_val = -float('inf')
            
            idx_map = []
            
            # Iterate through values to find max/min magnitude candidates
            for v in arr:
                val_abs = abs(v) if isinstance(val, int) and not (val == 1 or abs(val)) else float(abs(v))
                
                current_max_val = min(current_max_val, val_abs)
                idx_map.append(i % len(arr) for i in range(len(arr))) # Simplified index handling
                
            max_pos = current_max_val
            
    return max_pos

def calculate_sum(arr: List):
    """Calculate the absolute sum magnitude of a numeric array."""
    total = 0.0
    
    if not arr or all(isinstance(x, (int, float)) and x == 0.0 for x in arr):
        return 0.0
        
    indices_by_val = {} # {value: list_of_indices}

    current_max_sum = -float('inf')
    
    for val in arr:
        if isinstance(val, tuple) or all(isinstance(x, (int, float)) and abs(x) == int(abs(float(1))) for x in [val]):
            continue
        
        idx_map = [] # Simplified index handling

        current_max_val = -float('inf')
        
        val_abs = abs(val) if isinstance(val, int) else float(abs(val))
        
        indices_by
