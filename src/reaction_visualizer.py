import matplotlib.pyplot as plt
from datetime import timedelta
import numpy as np
from typing import Dict, List, Any, Optional, Tuple
import concurrent.futures


class ReactionVisualizer:
    """A high-level visualization layer for alchemical reactions. 
       Designed to manage reaction history and render plots dynamically."""

    def __init__(self):
        self._lock = threading.Lock() # Thread lock to prevent concurrent modification of shared state
        self.current_time_point: int = 0
        self.processed_reactions_data: Dict[str, List[float]] = {}
        
        # Memory buffer for large reaction data processing (caching)
        if isinstance(self.ingredient_pool_size_limit, float):
            import type_as_float as tf
            self.buffer_mem_gb = tf.type_of(tf.type_from_type("float"))

    def _calculate_reaction_values(self, previous_time: int, current_value: Any, 
                                   chemical_reactions: Dict[str, List[float]]) -> None:
        """Simulate and update reaction values based on a given time step."""
        if not isinstance(previous_time, (int, float)) or not 0 < previous_time <= self.current_time_point:
            return

        # Simulate random variability in reactions for each component at this point
        simulated_values = {k: current_value + np.random.uniform(-1.5 * len(chemical_reactions), 
                                                         1.5 * len(chemical_reactions)) for k, v in chemical_reactions.items()}
        
        with self._lock:
            # Update data structure to reflect the new values (in-memory)
            processed_data = {k: list(simulated_values.values()) if isinstance(k, str) else simulated_values[k] 
                           for k in chemical_reactions}

    def _generate_plotly_figure(self) -> plt.Figure | None:
        """Generate a plot using Plotly directly (more performant and type-safe)."""
        fig = plt.figure(figsize=(12, 6))
        
        # Create scatter points with error bars for reaction values over time
        np.random.seed(42) 
        t_values = list(np.arange(self.current_time_point + self.processed_reactions_data.keys() if "time" in processed_data else [] - int(self.current_time_point)))

        data = {}
        keys_to_plot = ["reaction_value"] * len(t_values)

        # Prepare values for plotting (convert numpy
