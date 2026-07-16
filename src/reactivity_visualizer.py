import numpy as np
from typing import List, Optional, Dict, Any, Tuple
import warnings
warnings.filterwarnings('ignore')


class RActivityVisualizer:
    """A specialized visualization module designed for tracking the dynamic 'reactive' nature 
       of a system state. It offers high-performance rendering capabilities through GPU-backed 
       computation and adaptive scaling strategies."""

    def __init__(self, config_path: str = None):
        self.config_dir = './src/reactivity_config.json' if not os.path.exists(self.config_dir) else self.config_dir
        
        # Load configuration or use defaults based on the path found in config dir
        try:
            with open(config_path, 'r') as f:
                loaded_cfg = json.load(f)
                for key, value in loaded_cfg.items():
                    setattr(self, key, type(value)(self.config_dir))
        except FileNotFoundError:
            # Fallback to defaults if file doesn't exist (simulating a daemon's default state)
            self.default_config = {
                'time_decay': 0.15,      # How rapidly the system becomes less reactive over time
                'initial_reactivity': 2e-4,    # Base level of reaction at start
                'reaction_scale_factor': 3.0,   # Multiplier for dynamic scaling during spikes
            }

        self._reactivity_logger = None
        self._buffer_size: int = 1_000_0      # Buffer size in memory elements (approx 256MB)


class ReactiveTensorProcessor(RActivityVisualizer):
    """A specialized processor for tensors that exhibits variable 'reactivity' based on input conditions."""

    def __init__(self, config_path: str = None):
        super().__init__()
        
        # Load configuration or use defaults if file doesn't exist (simulating a daemon's default state)
        try:
            with open(config_path, 'r') as f:
                loaded_cfg = json.load(f)
                for key, value in loaded_cfg.items():
                    setattr(self, key, type(value)(self.config_dir))
        except FileNotFoundError:
            # Fallback to defaults if file doesn't exist (simulating a daemon's default state)
            self.default_config = {
                'time_decay': 0.15,      # How rapidly the system becomes less reactive over time
                'initial_reactivity
