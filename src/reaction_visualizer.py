import json
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt

class ReactionVisualizer:
    def __init__(self):
        self.current_reaction = "Neutral"  # Default to 'neutral' state if not specified
    
    def load_aliens(self, data=None):
        """Load test dataset into memory."""
        try:
            if data is None and Path("src/test_data.json").exists():
                with open(Path("src/test_data.json"), "r") as f:
                    self.data = json.load(f)                    
            
            return True
        except FileNotFoundError:
            print("[ERROR] 'test_data.json' not found.")

    def plot_reaction(self, data=None):
        """Visualize reaction kinetics. 
        
        Data is required to be a dictionary containing key-value pairs like {'time': [...], 'reaction_value': [...]}."""
        if self.current_reaction == "None":
            raise ValueError("No initial state specified; assume neutral (0).")

        try:
            # Ensure all keys exist before plotting (or validate provided data)
            required_keys = {"time", "reaction_value"}
            
            for key, val in list(data.items()):
                if not isinstance(val, dict):
                    raise ValueError(f"Non-serializable value found at '{key}'. Must be a dictionary or simple sequence.")

            # Prepare inputs (handle both lists and dicts as per standard JSON representation)
            time_list = [val for val in data.values() if isinstance(val, list)]
            
            reaction_values = {k: v[1] for k, v in data.items()}  # Convert value to number
            
            fig, ax = plt.subplots(figsize=(8.5, 6))

            try:
                # Plot time as x-axis and key names (as values) on y-axis
                if len(time_list) == 0 or not isinstance(time_list[0], list):
                    raise ValueError("Time data must be a sequence of lists.")
                
                ax.plot([time] + [1 for _ in self.data], reaction_values.keys())

            except Exception as e:
                # Fallback if time list doesn't match expected format (e.g., key is string)
                pass
            
            ax.set_xlabel("Time")
            ax.set_ylabel('Reaction Value')
            
        finally:
            plt.close(fig)
