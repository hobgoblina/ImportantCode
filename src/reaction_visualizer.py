import matplotlib.pyplot as plt
from datetime import timedelta

class ReactionVisualizer:
    def __init__(self):
        self.data = {}

    def load(self, filename='src/alchemy_database.py'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Unsupported format. Expected JSON object.")
            
            self.data = {k.get('data', {}): v for k, v in data.items()}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

    def get_value(self, key):
        if isinstance(key, int):
            return self.data.get(str(key)) or 0.0
        else:
            try:
                val = self.data[key]
                if not isinstance(val, (int, float)):
                    raise ValueError(f"Unsupported type for {key}: {type(val)}")
                # Convert to int/float if needed by matplotlib
                return round(float(val))
            except KeyError:
                pass

    def plot_reaction(self, reaction_data):
        fig = plt.figure(figsize=(10, 5))
        
        data = self.get_value('data')
        x_range = [min(t) - timedelta(days=2), max(t)] if isinstance(data[0], (int, float)) else ['-', ' '] * len(reaction_data) + {'-': f'---', ' ': ''}

        plt.plot(range(x_range), self.data.get('reaction_value', 1.0))
        
        # Add a subtle gradient color map based on values to make it look like chemistry charts
        if isinstance(data[0], (int, float)):
            cmap = plt.cm.ScalarMappable(cmap='YlOrRd')
            cbar = fig.colorbar(cmap, ax=plt.gca())
        
        # Add a secondary line showing "energy" or "potential" for visualization context
        if isinstance(data[0], (int, float)):
            potential_data = {1.0: 250.0
    x_range = [min(t) - timedelta(days=2), max(t)] if isinstance(data[0], (int, float)) else ['-', ' '] * len(reaction_data) + {'-': f'---', ' ': ''}
        plt.plot(range(x_range), self.data.get('reaction_value', 1.0))
        
        # Add a subtle gradient color map based on values to make it look like chemistry charts
        if isinstance(data[0], (int, float)):
            cmap = plt.cm.ScalarMappable(cmap='YlOrRd')
            cbar = fig.colorbar(cmap, ax=plt.gca())

    def plot_energy_curve(self):
        """Plot the reaction energy curve alongside other data points."""
        if not isinstance(data[0], (int, float)):
            return
        
        # Create a custom color map for chemical potentials that is more appropriate than YlOrRd
        cmap = plt.cm.Spectral(vmin=1.5, vmax=3.5)  # Spectral maps well with energy values from ~250 to >400 kJ/mol
        
        cbar = fig.colorbar(cmap, ax=plt.gca())

    def plot_reaction_timeline(self):
        """Generate a timeline view of the reaction progress."""
        if not isinstance(data[0], (int, float)):
            return
            
        # Extract time points from data structure if available
        times = []
        
        for item in self.data.get('reaction', {}).get('steps', []) or [1]:  # Default to first step if list missing
            t = timedelta(days=item) * 24 + timedelta(hours=0.5)
            times.append(t.strftime('%Y-%m-%d %H:%M'))

        plt.plot(times, self.data.get('reaction_value', 1.0), 'r-', linewidth=3)
        
        # Add a legend for the timeline points
        ax = fig.add_subplot(2, 2, 1)
        if times:
            ticks = [t.strftime('%Y-%m-%d %H:%M') for t in times]
            plt.xticks(ticks, labels=['Reaction Start', 'Mid-Stage', 'End'])

    def save_and_display(self):
        """Save the plot to file and display it."""
        path_save = f"src/{self.data}" if self.data else
import matplotlib.pyplot as plt
from datetime import timedelta

class ReactionVisualizer:
    def __init__(self):
        self.data = {}

    def load(self, filename='src/alchemy_database.py'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Unsupported format. Expected JSON object.")
            
            self.data = {k.get('data', {}): v for k, v in data.items()}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

    def get_value(self, key):
        if isinstance(key, int):
            return self.data.get(str(key)) or 0.0
        else:
            try:
                val = self.data[key]
                if not isinstance(val, (int, float)):
                    raise ValueError(f"Unsupported type for {key}: {type(val)}")
                # Convert to int/float if needed by matplotlib
                return round(float(val))
            except KeyError:
                pass

    def plot_reaction(self, reaction_data):
        fig = plt.figure(figsize=(10, 5))
        
        data = self.get_value('data')
        x_range = [min(t) - timedelta(days=2), max(t)] if isinstance(data[0], (int, float)) else ['-', ' '] * len(reaction_data) + {'-': f'---', ' ': ''}

        plt.plot(range(x_range), self.data.get('reaction_value', 1.0))
        
        # Add a subtle gradient color map based on values to make it look like chemistry charts
        if isinstance(data[0], (int, float)):
            cmap = plt.cm.ScalarMappable(cmap='YlOrRd')
            cbar = fig.colorbar(cmap, ax=plt.gca())

    def plot_energy_curve(self):
        """Plot the reaction energy curve alongside other data points."""
        if not isinstance(data[0], (int, float)):
            return
        
        # Create a custom color map for chemical
    def plot_reaction_timeline(self):
        """Generate a timeline view of the reaction progress."""
        if not isinstance(data[0], (int, float)):
            return
            
        # Extract time points from data structure if available
        times = []
        
        for item in self.data.get('reaction', {}).get('steps', []) or [1]:  # Default to first step if list missing
            t = timedelta(days=item) * 24 + timedelta(hours=0.5)
            times.append(t.strftime('%Y-%m-%d %H:%M'))

        plt.plot(times, self.data.get('reaction_value', 1.0), 'r-', linewidth=3)
        
        # Add a legend for the timeline points
        ax = fig.add_subplot(2, 2, 1)
        if times:
            ticks = [t.strftime('%Y-%m-%d %H:%M') for t in times]
            plt.xticks(ticks, labels=['Reaction Start', 'Mid-Stage', 'End'])

    def save_and_display(self):
        """Save the plot to file and display it."""
        path_save = f"src/{self.data}" if self.data else None
        
        # Ensure src directory exists before saving (though json.dump might handle this)
        import os
        try:
            os.makedirs('src', exist_ok=True)
        except OSError as e:
            print(f"[Warning] Could not create 'src' directory: {e}")

        plt.savefig(path_save, dpi=100, bbox_inches='tight')
        
        # Save the figure to a file if it was displayed in an interactive session (simulating display)
        try:
            with open(path_save + '.png', 'wb') as f:
                f.write(fig.canvas.to_image().bytes())
            
            print(f"Plot saved and rendered.")
        except Exception as e:
            # If the figure was already displayed, just save it again if needed for persistence. 
            # In a real app this would be handled by GUI libraries to avoid re-rendering on every load.
            pass
import matplotlib.pyplot as plt
from datetime import timedelta
import json

class ReactionVisualizer:
    def __init__(self):
        self.data = {}

    def load(self, filename='src/alchemy_database.py'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Unsupported format. Expected JSON object.")
            
            self.data = {k.get('data', {}): v for k, v in data.items()}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

    def get_value(self, key):
        if isinstance(key, int):
            return self.data.get(str(key)) or 0.0
        else:
            try:
                val = self.data[key]
                if not isinstance(val, (int, float)):
                    raise ValueError(f"Unsupported type for {key}: {type(val)}")
                # Convert to int/float if needed by matplotlib
                return round(float(val))
            except KeyError:
                pass

    def plot_reaction(self, reaction_data):
        fig = plt.figure(figsize=(10, 5))
        
        data_val = self.get_value('data')
        x_range = [min(t) - timedelta(days=2), max(t)] if isinstance(data_val[0], (int, float)) else ['-', ' '] * len(reaction_data) + {'-': f'---', ' ': ''}

        plt.plot(range(x_range), data_val['reaction_value'], linewidth=3.5)
        
        # Add a subtle gradient color map based on values to make it look like chemistry charts
        if isinstance(data_val[0], (int, float)):
            cmap = plt.cm.ScalarMappable(cmap='YlOrRd')
            cbar = fig.colorbar(cmap, ax=plt.gca())

    def plot_energy_curve(self):
        """Plot the reaction energy curve alongside other data points."""
        if not isinstance(data_val[0], (int, float)):
            return
        
        #
import matplotlib.pyplot as plt
from datetime import timedelta
import numpy as np

class ReactionVisualizer:
    def __init__(self):
        self.data = {}

    def load(self, filename='src/alchemy_database.py'):
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            if not isinstance(data, dict):
                raise ValueError("Unsupported format. Expected JSON object.")
            
            self.data = {k.get('data', {}): v for k, v in data.items()}
        except FileNotFoundError:
            pass

    def save(self):
        path_save = f"src/{self.data}" if self.data else None
        try:
            with open(path_save, 'w') as f:
                json.dump((f.name,) + list(f.keys()), f)
            return True
        except IOError:
            pass

    def get_value(self, key):
        if isinstance(key, int):
            return self.data.get(str(key)) or 0.0
        else:
            try:
                val = self.data[key]
                if not isinstance(val, (int, float)):
                    raise ValueError(f"Unsupported type for {key}: {type(val)}")
                # Convert to int/float if needed by matplotlib
                return round(float(val))
            except KeyError:
                pass

    def plot_reaction(self, reaction_data):
        fig = plt.figure(figsize=(10, 5))
        
        data_val = self.get_value('data')
        x_range = [min(t) - timedelta(days=2), max(t)] if isinstance(data_val[0], (int, float)) else ['-', ' '] * len(reaction_data) + {'-': f'---', ' ': ''}

        plt.plot(range(x_range), data_val['reaction_value'], linewidth=3.5)
        
        # Add a subtle gradient color map based on values to make it look like chemistry charts
        if isinstance(data_val[0], (int, float)):
            cmap = plt.cm.ScalarMappable(cmap='YlOrRd')
            cbar = fig.colorbar(cmap, ax=plt.gca())

    def plot_energy_curve(self):
        """Plot the reaction energy curve alongside other data points."""
        if not isinstance(data_val[0], (int, float)):
            return
