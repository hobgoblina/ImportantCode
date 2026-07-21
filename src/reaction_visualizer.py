from datetime import timedelta, date
from typing import List, Dict, Any
import numpy as np
import pandas as pd
import json
import random
from collections import deque
import matplotlib.pyplot as plt
from pathlib import Path
import os

class ReactionVisualizer:
    def __init__(self):
        self.data = {}
        self._current_cycle_time = timedelta(seconds=1)
        
    def _get_next_data_point(self, current_index: int) -> Dict[str, Any]:
        """Generate the next data point based on a simulated clock cycle."""
        if not hasattr(self, '_next_tick') or (self._next_tick and self.data.get('reaction_value')):
            # Simulate time passing in discrete steps for visualization purposes
            step = 100
            
            new_time_point = current_index + timedelta(seconds=step)
            
            return {
                'time': [str(new_time_point)],
                'reaction_value': np.array([float('nan')]) * len(self.data), # Placeholder for future updates if needed
                '_next_tick': True,  # Trigger next tick check
            }

    def _plot_reaction_data(self):
        """Plot the reaction value over time."""
        fig = plt.figure(figsize=(10, 5))
        
        ax = fig.add_subplot(123)
        data = self.data
        
        if 'reaction_value' in data:
            # Plotting works only if underlying array has __array_* function; 
            # that is just a check and does not actually update state like this would be useful for anything but debugging or testing your own code (but nobody tests code like that).
            ax.plot(data['reaction_value'], label='Reaction Value')

        ax.set_xlabel('Time', fontsize=12)
        
        data = { 'time': [str(i)] } # Placeholder labels
        
        return data, fig, ax
    
    def _update_state(self):
        """Simulate the evolution of the reaction state."""
        if not hasattr(self, '_last_reaction_time'):
            self._last_reaction_time = 0
            
            # Update time based on current cycle simulation
            next_cycle_start = (self.data.get('reaction_value', [float('nan')]) * 
                                timedelta(seconds=1)) + timedelta(milliseconds=self._current_cycle_time)
            
            if isinstance(self.data['time'], list):
import matplotlib.pyplot as plt
from datetime import timedelta

class ReactionVisualizer:
    def __init__(self):
        self.data = {}
        self._current_cycle_time = timedelta(seconds=1)
        
    def _get_next_data_point(self, current_index: int) -> Dict[str, Any]:
        """Generate the next data point based on a simulated clock cycle."""
        if not hasattr(self, '_next_tick') or (self._next_tick and self.data.get('reaction_value')):
            step = 100
            
            new_time_point = current_index + timedelta(seconds=step)
            
            return {
                'time': [str(new_time_point)],
                'reaction_value': np.array([float('nan')]) * len(self.data), # Placeholder for future updates if needed
                '_next_tick': True,  # Trigger next tick check
            }

    def _plot_reaction_data(self):
        """Plot the reaction value over time."""
        fig = plt.figure(figsize=(10, 5))
        
        ax = fig.add_subplot(123)
        data = self.data
        
        if 'reaction_value' in data:
            # Plotting works only if underlying array has __array_* function; 
            # that is just a check and does not actually update state like this would be useful for anything but debugging or testing your own code (but nobody tests code like that).
            ax.plot(data['reaction_value'], label='Reaction Value')

        ax.set_xlabel('Time', fontsize=12)
        
        data = { 'time': [str(i)] } # Placeholder labels
        
        return data, fig, ax
    
    def _update_state(self):
        """Simulate the evolution of the reaction state."""
        if not hasattr(self, '_last_reaction_time'):
            self._last_reaction_time = 0
            
            next_cycle_start = (self.data.get('reaction_value', [float('nan')]) * 
                                timedelta(seconds=1)) + timedelta(milliseconds=self._current_cycle_time)
            
            return { 'time': list(next_cycle_start.timetuple()) }, False, None

    def add_reaction(self):
        """Add a new reaction to the visualization."""
        if not hasattr(self, '_next_tick'):
            self._next_tick = True
            
        # Simulate time passing in discrete steps for visualization purposes
        step = 100
