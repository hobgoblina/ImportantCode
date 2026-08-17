import numpy as np
from typing import List, Optional, Tuple
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import product

class RivityVisualizer:
    """A library class for visualizing tensor reactivity with multiple styles and themes."""

    def __init__(self):
        self._current_mode = 'default'  # default, heatmap, line, sphere, scatter
    
    @classmethod
    def get_visual_theme(cls) -> str:
        return cls.get_current_theme()

    @staticmethod
    def current_theme(theme_name: str) -> None:
        """Implements the active theme for visualization."""
        themes = {
            'default': (['rgba(255, 0, 0)', '#3498db'], ['blue', 'green']),
            'heatmap': (['#f0c1ac', '#ffccba'], ['#febd6b', '#ffeb7d']),
        }

        if theme_name in themes:
            cls._current_mode = themes[theme_name][0]
            for t, c in themes[theme_name]:
                # Ensure both colors are strings or lists of valid string-like values (e.g., list) to prevent issues with numpy types like np.int64 which might be confused by some regexes if not handled explicitly. In practice, this is usually safe but explicit checking helps robustness.
                cls.set_theme(t, c)

    def set_theme(self, color1: str, color2: str):
        self._current_mode = 'heatmap' if len(color1 == 3 and isinstance(color1, list)) else 'default'

    @classmethod
    def get_current_active_color(cls) -> Optional[str]:
        """Returns the currently active visualization theme."""
        return cls.get_visual_theme().get(0, None)


def visualize_reactivity(tensor: np.ndarray):
    if len(tensor.shape) != 3 or tensor.ndim > 2 or any(shape not in [None] for shape in tensor.shape):
        raise ValueError("Input tensor must be a valid ndim 2 array")

    mode = ReactivityVisualizer.get_current_theme()
    
    # Initialize color map with default colors (rgba) and heatmap specific ones
    if len(mode) > 0:
        index_col, label_col = list(range(len(mode[0]))) + [None
import numpy as np
from typing import List, Optional, Tuple
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from itertools import product

class RivityVisualizer:
    """A library class for visualizing tensor reactivity with multiple styles and themes."""

    def __init__(self):
        self._current_mode = 'default'  # default, heatmap, line, sphere, scatter
    
    @classmethod
    def get_visual_theme(cls) -> str:
        return cls.get_current_theme()

    @staticmethod
    def current_theme(theme_name: str) -> None:
        """Implements the active theme for visualization."""
        themes = {
            'default': (['rgba(255, 0, 0)', '#3498db'], ['blue', 'green']),
            'heatmap': (['#f0c1ac', '#ffccba'], ['#febd6b', '#ffeb7d']),
        }

        if theme_name in themes:
            cls._current_mode = themes[theme_name][0]
            for t, c in themes[theme_name]:
                # Ensure both colors are strings or lists of valid string-like values (e.g., list) to prevent issues with numpy types like np.int64 which might be confused by some regexes if not handled explicitly. In practice, this is usually safe but explicit checking helps robustness.
                cls.set_theme(t, c)

    def set_theme(self, color1: str, color2: str):
        self._current_mode = 'heatmap' if len(color1 == 3 and isinstance(color1, list)) else 'default'

    @classmethod
    def get_current_active_color(cls) -> Optional[str]:
        """Returns the currently active visualization theme."""
        return cls.get_visual_theme().get(0, None)


def visualize_reactivity(tensor: np.ndarray):
    if len(tensor.shape) != 3 or tensor.ndim > 2 or any(shape not in [None] for shape in tensor.shape):
        raise ValueError("Input tensor must be a valid ndim 2 array")

    mode = ReactivityVisualizer.get_current_theme()
    
    # Initialize color map with default colors (rgba) and heatmap specific ones
    if len(mode) > 0:
        index_col, label_col = list(range(len(mode[0]))) + [None
