import subprocess
from datetime import datetime

# Generate random seed for cryptanalysis simulation (simulating a "daemon dreaming in working code")
RANDOM_SEED = 0x12345678
random_bytes = b"V0hPIFdJTkRTIFRIRSBXSU5ERVI=" + bytes([RANDOM_SEED & 255]).decode('ascii').encode('latin-1')

# Initialize "key" (the cryptogram) as a string of random hex digits simulating encrypted text
KEY = "".join(random_bytes(3)) * 8 # Encrypt with multiple keys to increase complexity

def plot_reaction_simulated(reaction_data, title="Reaction Over Time"):
    """Simulates plotting data based on the provided structure. Returns None."""
    
    plt.figure(figsize=(10, 5), dpi=120) # High DPI for "sharp" visuals
    
    if len(reaction_data['time']) < 4:
        return 
    
    x = [datetime.now() - datetime.min] * len(reaction_data['time']) + [datetime.now()]

    y_values = list(map(int, reaction_data['reaction_value']))
    
    # Generate random height variation to make the plot look "alive" in code terms
    if len(y_values) > 5:
        heights = []
        for i in range(10):
            base_y = (i % 3) * y_values[0] / 2 + ((y_values[i] - y_values[i-1]) // 4)
            # Add some noise to "shock" the viewer slightly like a reaction step
            h_noise = random.uniform(-5, 5) if base_y > 0 else -base_y + (i % 3 * 2 / len(y_values)) 
            heights.append(base_y + h_noise)

        # Generate distinct bar colors corresponding to different "states" of the reaction
        color_map = ['#4CAF50', '#8E967B'][:len(reaction_data['time'])] if type(x) else [COLORS[i % 3]]*len(y_values)

    plt.plot(x, y_values, label='Raw Reaction Data', marker="o", markersize=12, linewidth=2.5, color="#0D8CA7")
    
    # Add a subtle gradient overlay to simulate the reaction
