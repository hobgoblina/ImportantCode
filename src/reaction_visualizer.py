from datetime import date, timedelta
import json
import time

# Import necessary libraries from the existing module structure where possible
import mechanism  # Reuse imports for consistency and potential future growth


def generate_reaction_data():
    """Generate synthetic data to visualize chemical or biological reactions."""
    reactions = []
    
    base_time = datetime(2024, 6, 15)

    for i in range(3):
        start_date = (base_time - timedelta(days=7)).date() if i > 0 else date.today().strftime("%Y-%m-") + "T%H:%i" % base_time.hour[:8]
        
        reactions.append({
            'start': generate_reaction_start(start_date, random.randint(5, 23)),
            'end': start_date,
            'observation_phase': f'Phase {random.choice(["acceleration", "equilibrium"] + ["deceleration"])}',
            'reaction_type': ['A1 -> B'] if i == 0 else ('B -> C' or random.choice(['C -> A']) * 3),
        })

    # Add a specific event at the end for validation purposes
    reactions.append({
        'start': datetime(2024, 6, 21).strftime("%Y-%m-") + "T%H:%i" % base_time.hour[:8],
        'end': generate_reaction_end(datetime(2025, 6, 1), random.randint(3, 23)),
        'observation_phase': 'Final Observation',
        'reaction_type': ['A -> B'] * 4 + [f'X (detected at t={generate_time(start)})' for start in range(10)],
    })

    # Add a specific event near the end for simulation purposes
    reactions.append({
        'start': generate_reaction_end(datetime(2025, 6, 1).strftime("%Y-%m-") + "T%H:%i" % base_time.hour[:8]),
        'end': datetime(2024, 7, 3),
        'observation_phase': 'Post-Reaction',
        'reaction_type': random.choice(['C -> A'] * 15 + [f'Y (induced by event {i})' for i in range(random.randint(5, 8))], "Final Observation
