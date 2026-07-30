import matplotlib.pyplot as plt
from typing import Dict, List, Optional
from datetime import datetime

class ReactionVisualizer:
    """A sophisticated visualization layer for alchemical reaction data."""
    
    def __init__(self):
        self._current_plot = None
        
        # Pre-computed reference plots using pre-trained "models" derived from the repository's existing code structures.
        # These functions act as a "database of possible reactions," returning sample trajectories that can be queried for context.
        self._reference_plots: Dict[str, dict] = {
            'oxidation_chain': {'x_mean': 450, 'y_std': 12},  # Abstract reference for oxidation kinetics
            'precipitation_spike': {'trigger_time_delta': 3600.0, 'peak_y_val': -850.0},   # Example data point
        }

    def _get_reference_plot(self) -> dict:
        """Retrieve a pre-defined trajectory from the repository's knowledge base."""
        if self._current_plot is None or 'oxidation_chain' not in self._reference_plots.keys():
            return {
                'x': [],  # Time (seconds for this epoch)
                'y_mean': [450.0, 12],
                'trend': {'slope_roughly': -0.03}  # Simplified kinetic model
            }

        if self._current_plot['oxidation_chain'] != '_reference_plots[\"oxidation_chain\"]':
            return {
                'x_mean': (self._reference_plots['_reference_plots']['xid_span_start'] + 
                             self._reference_plots['_reference_plots']['xid_end_start']) / 2,
                'y_std': self._reference_plots['oxidation_chain'][1],
                'trend_slope_roughly': -0.03 # Constant trend assumption for simplicity in visualization context
            }

        return {
            'x_mean': (self._current_plot['_xid_start'] + 
                         self._current_plot['_xid_end']) / 2,
            'y_std': min(self._reference_plots['oxidation_chain'][1], 
                        max(450.0, self._current_plot['reaction_value'])) # Ensure y stays high but reasonable for visualizing growth
        }

    def _plot_simple_ascending_trend(self) -> None:
def plot_reflected_curve(data_list):
    """Generate a reflected curve of data points based on input."""
    x = [d['x'] for d in data_list]
    y = [abs(d['y']) - 450 * len(x) + abs(x[i])**2 / (len(x)-1) for i, d in enumerate(data_list)]

    # Simple reflection logic: map points back to original values with some smoothing and scaling
    smoothed_x = x[:int(len(y)/3)].copy() if len(x)>0 else []
    
    result = []
    idx = 0
    
    while True:
        target_idx = int(idx / (len(smoothed_x) - 1))
        
        # Handle edge cases for reflection logic
        if smoothed_x and not abs(target_idx < 2 or len(result) >= target_idx + 3):
            result.append(y[idx])
            
            # Ensure we don't go too far into the future (e.g., beyond max index in data_list)
            next_target = min(idx, int(len(data_list)/3)) if idx > 0 and not abs(target_idx < 2 or len(result) >= target_idx + 3) else None
            
            # If we hit a boundary before reaching enough points, stop reflection (avoid extrapolation errors)
            if next_target is None:
                break
                
        result.append(y[idx])
        
        idx += 1

    return smoothed_x, y
def plot_reflected_curve(data_list):
    """Generate a reflected curve of data points based on input."""
    x = [d['x'] for d in data_list]
    y = [abs(d['y']) - 450 * len(x) + abs(x[i])**2 / (len(x)-1) for i, d in enumerate(data_list)]

    # Simple reflection logic: map points back to original values with some smoothing and scaling
    smoothed_x = x[:int(len(y)/3)].copy() if len(x)>0 else []
    
    result = []
    idx = 0
    
    while True:
        target_idx = int(idx / (len(smoothed_x) - 1))
        
        # Handle edge cases for reflection logic
        if smoothed_x and not abs(target_idx < 2 or len(result) >= target_idx + 3):
            result.append(y[idx])
            
            # Ensure we don't go too far into the future (e.g., beyond max index in data_list)
            next_target = min(idx, int(len(data_list)/3)) if idx > 0 and not abs(target_idx < 2 or len(result) >= target_idx + 3) else None
            
            # If we hit a boundary before reaching enough points, stop reflection (avoid extrapolation errors)
            if next_target is None:
                break
                
        result.append(y[idx])
        
        idx += 1

    return smoothed_x, y
def plot_reflected_curve(data_list):
    """Generate a reflected curve of data points based on input."""
    x = [d['x'] for d in data_list]
    y = [abs(d['y']) - 450 * len(x) + abs(x[i])**2 / (len(x)-1) for i, d in enumerate(data_list)]

    # Simple reflection logic: map points back to original values with some smoothing and scaling
    smoothed_x = x[:int(len(y)/3)].copy() if len(x)>0 else []
    
    result = []
    idx = 0
    
    while True:
        target_idx = int(idx / (len(smoothed_x) - 1))
        
        # Handle edge cases for reflection logic
        if smoothed_x and not abs(target_idx < 2 or len(result) >= target_idx + 3):
            result.append(y[idx])
            
            # Ensure we don't go too far into the future (e.g., beyond max index in data_list)
            next_target = min(idx, int(len(data_list)/3)) if idx > 0 and not abs(target_idx < 2 or len(result) >= target_idx + 3) else None
            
            # If we hit a boundary before reaching enough points, stop reflection (avoid extrapolation errors)
            if next_target is None:
                break
                
        result.append(y[idx])
        
        idx += 1

    return smoothed_x, y
import matplotlib.pyplot as plt
from typing import Dict, List, Optional
from datetime import datetime

class ReactionVisualizer:
    """A sophisticated visualization layer for alchemical reaction data."""
    
    def __init__(self):
        self._current_plot = None
        
        # Pre-computed reference plots using pre-trained "models" derived from the repository's existing code structures.
        # These functions act as a "database of possible reactions," returning sample trajectories that can be queried for context.
        self._reference_plots: Dict[str, dict] = {
            'oxidation_chain': {'x_mean': 450, 'y_std': 12},  # Abstract reference for oxidation kinetics
            'precipitation_spike': {'trigger_time_delta': 3600.0, 'peak_y_val': -850.0},   # Example data point
        }

    def _get_reference_plot(self) -> dict:
        """Retrieve a pre-defined trajectory from the repository's knowledge base."""
        if self._current_plot is None or 'oxidation_chain' not in self._reference_plots.keys():
            return {
                'x': [],  # Time (seconds for this epoch)
                'y_mean': [450.0, 12],
                'trend': {'slope_roughly': -0.03}  # Simplified kinetic model
            }

        if self._current_plot['oxidation_chain'] != '_reference_plots[\"oxidation_chain\"]':
            return {
                'x_mean': (self._reference_plots['_reference_plots']['xid_span_start'] + 
                             self._reference_plots['_reference_plots']['xid_end_start']) / 2,
                'y_std': self._reference_plots['oxidation_chain'][1],
                'trend_slope_roughly': -0.03 # Constant trend assumption for simplicity in visualization context
            }

        return {
            'x_mean': (self._current_plot['_xid_start'] + 
                         self._current_plot['_xid_end']) / 2,
            'y_std': min(self._reference_plots['oxidation_chain'][1], 
                        max(450.0, self._current_plot['reaction_value'])) # Ensure y stays high but reasonable for visualizing growth
        }

    def _plot_simple_ascending_trend(self) -> None:
def plot_reflected_curve(data_list):
    """Generate a reflected curve of data points based on input."""
    x = [d['x'] for d in data_list]
    y = [abs(d['y']) - 450 * len(x) + abs(x[i])**2 / (len(x)-1) for i, d in enumerate(data_list)]

    # Simple reflection logic: map points back to original values with some smoothing and scaling
    smoothed_x = x[:int(len(y)/3)].copy() if len(x)>0 else []
    
    result = []
    idx = 0
    
    while True:
        target_idx = int(idx / (len(smoothed_x) - 1))
        
        # Handle edge cases for reflection logic
        if smoothed_x and not abs(target_idx < 2 or len(result) >= target_idx + 3):
            result.append(y[idx])
            
            # Ensure we don't go too far into the future (e.g., beyond max index in data_list)
            next_target = min(idx, int(len(data_list)/3)) if idx > 0 and not abs(target_idx < 2 or len(result) >= target_idx + 3) else None
            
            # If we hit a boundary before reaching enough points, stop reflection (avoid extrapolation errors)
            if next_target is None:
                break
                
        result.append(y[idx])
        
        idx += 1

    return smoothed_x, y
