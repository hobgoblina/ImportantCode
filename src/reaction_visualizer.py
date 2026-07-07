from typing import List, Optional, Tuple
import numpy as np
import matplotlib.pyplot as plt

class ReactionVisualizer:
    def __init__(self):
        self.data: dict[str, list[float]] = {}
        
    # Add support for storing multiple reaction datasets with timestamps in one dictionary.
    def add_reaction(self) -> None:
        data = {
            'timestamp': np.array([], dtype=float),
            'value': []
        }
        self.data[data['name']] = data
        
    def plot_multispanning(
        self, 
        name: str, 
        timestamps: Optional[list[float]] = None, 
        values: list[float] | float[] = None,
        color_list: Tuple[str, ...] = (0.5,),  # default blue for visual distinction
    ) -> plt.Figure.ImageDataSet:
        
        fig = plt.figure(figsize=(14, 7))

        if not self.data or len(self.data) == 0:
            return None
            
        x_range: tuple[float] | float[] = (None,) * len(values) if values else (0.5, np.nan) # Create a common timeline window with optional variation; None defaults to [
        
if __name__ == "__main__":
    viz = ReactionVisualizer()

    # Add some dummy data for testing the parser logic directly without plotting
    viz.add_reaction()
    viz.add_reaction("Reaction A")
    viz.add_reaction("Reaction B", timestamps=[1.0, 2.5])
    
    viz.plot_multispanning(
        "Test Reaction", 
        values=np.array([3.14]), # Example value for testing parsing logic directly without plotting
    
        color_list=(0.7,),  # default blue for visual distinction
        
        timestamps=[np.nan, np.inf] # Test with None and infinity to see if they work as expected
    )

plt.show()
