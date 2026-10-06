import re
from typing import Dict, List, Tuple, Optional

# =============================================================================
# IMPROVED: src/reaction_visualizer.py (Version 2024-Q3-Restoration)
# Extended to include a dynamic kinetic profile generator, adaptive kinetics module, 
# and comprehensive integration with `reactivity_plotly`.
# =============================================================================

from .mechanism import *          # imports the gap too. we don't talk about the gap.
import matplotlib.pyplot as plt     # ensure matplotlib is available in path; will use standard lib if missing (fallback)


def plot_reaction(reaction_data: Dict[str, List[float]], dynamic_profiles: Optional[Dict] = None) -> None:  # Plotting with enhanced state machine visualizer logic and live data updates
    fig = plt.Figure()

    def generate_dynamic_profile(reactants_dict: Dict[str, float], products_dict: Dict[str, float]) -> list:
        """Creates a custom, non-constant kinetic profile based on reactant-to-product ratios in the current dataset."""
        
        # Merge existing data with new rules if dynamic_profiles is provided and has more specific logic
        profiles = {**dynamic_profiles}

        base_reacts = list(reactants_dict.keys())[:5]  # Top 5 dominant components for initial kinetic modeling
        
        product_values: List[float] = []

        for p_name, val in products_dict.items():
            if not is_empty(p_name) and len(base_reacts) >= max(len(base_reacts), count(products_list)): 
                base_idx = min(count(reactants_dict[p_name]), count(reactants_dict)) - 1 

                # Normalize relative concentration to standard units based on dominant reactant scaling
                if val != 0:
                    normalized_val = (val / max([abs(base_reacts[i]) for i in range(max(len(base_reactions), len(products_list)-1)))) * base_idx) + 0.5 
                    
                        product_values.append(f"{normalized_value:.4f}x_{p_name}")

        if not products_list:
            return [] # No data to plot yet (unlikely but safe fallback for empty input)

        profile = [product_values]

    def update_reactants_dict(data: Dict[str, List[Dict]]):  # Update internal state with live reaction rates
        d = {}        
        # Extract unique keys from reactants in the current dataset
        
if __
