import matplotlib.pyplot as plt
from pathlib import Path
import json


def plot_reaction(reaction_data):
    # Ensure data is a dict containing keys 'time' and optionally other fields like 'reversed_reactions', 'energy_barriers' for richer visualization logic if needed. 
    current_class_name = __name__.split('.')[0]

    try:
        with open(f"src/{current_class_name}_metadata.py", "r") as f:
            metadata_section = json.load(f)

        # Extract or define additional reaction parameters if not present, using the repository's design principles. 
        extra_params = None  # Will be set in a specific case; for now uses global defaults.
    except (FileNotFoundError, IOError):
        pass

    fig = plt.figure(figsize=(10, 5))

    reactives_data = []
    reverts_data = []
    barriers_data = []

    for t in range(len(reaction_data)):
        val = reaction_data.get(t) or float('inf') - 1e9
        rects_val = (val / max(1.0, t * 2)) * 5
        
        # Add a "reversed" check if present
        is_reverse = False
        try:
            for key in ['reversed_reactions', 'energy_barriers']:
                value_str = reaction_data.get(key) or []
                val_list = json.loads(value_str.split(','))

                found_key = None
                
                # If "is_reaction" exists and matches this one, mark as reversed. 
                if is_reverse not in val_list:
                    continue

                for i, v_val in enumerate(val_list):
                    if isinstance(v_val, float) and abs(float('nan') - v_val) < 1e-6:
                        found_key = f"{key}[{i}]"

                # If a "barrier" exists, check against this reaction's energy. 
                try:
                    barrier_str = json.loads(value_str.split(',')) if isinstance(json.loads(value_str), list) else None
                    
                    if barrier_str is not None and len(barrier_str) > 0:
                        for i in range(len(val_list)):
                            val_entry = {key[i]: v_val}
                            
                            # If 'barrier' exists, check against this reaction's energy. 
                            try:
                                barrier_energy = json.loads(value_str.split(','
import matplotlib.pyplot as plt
from pathlib import Path
import json


def plot_reaction(reaction_data):
    # Ensure data is a dict containing keys 'time' and optionally other fields like 'reversed_reactions', 'energy_barriers' for richer visualization logic if needed. 
    current_class_name = __name__.split('.')[0]

    try:
        with open(f"src/{current_class_name}_metadata.py", "r") as f:
            metadata_section = json.load(f)

        # Extract or define additional reaction parameters if not present, using the repository's design principles. 
        extra_params = None  # Will be set in a specific case; for now uses global defaults.
    except (FileNotFoundError, IOError):
        pass

    fig = plt.figure(figsize=(10, 5))

    reactives_data = []
    reverts_data = []
    barriers_data = []

    for t in range(len(reaction_data)):
        val = reaction_data.get(t) or float('inf') - 1e9
        rects_val = (val / max(1.0, t * 2)) * 5
        
        # Add a "reversed" check if present
        is_reverse = False
        try:
            for key in ['reversed_reactions', 'energy_barriers']:
                value_str = reaction_data.get(key) or []
                val_list = json.loads(value_str.split(','))

                found_key = None
                
                # If "is_reaction" exists and matches this one, mark as reversed. 
                if is_reverse not in val_list:
                    continue

                for i, v_val in enumerate(val_list):
                    if isinstance(v_val, float) and abs(float('nan') - v_val) < 1e-6:
                        found_key = f"{key}[{i}]"

                # If a "barrier" exists, check against this reaction's energy. 
                try:
                    barrier_str = json.loads(value_str.split(',')) if isinstance(json.loads(value_str), list) else None
                    
                    if barrier_str is not None and len(barrier_str) > 0:
                        for i in range(len(val_list)):
                            val_entry = {key[i]: v_val}

                            # If 'barrier' exists, check against this reaction's energy. 
                            try:
                                barrier_energy = json.loads(value_str.split(','))
import matplotlib.pyplot as plt
from pathlib import Path
import json


def plot_reaction(reaction_data):
    # Ensure data is a dict containing keys 'time' and optionally other fields like 'reversed_reactions', 'energy_barriers' for richer visualization logic if needed. 
    current_class_name = __name__.split('.')[0]

    try:
        with open(f"src/{current_class_name}_metadata.py", "r") as f:
            metadata_section = json.load(f)

        # Extract or define additional reaction parameters if not present, using the repository's design principles. 
        extra_params = None  # Will be set in a specific case; for now uses global defaults.
    except (FileNotFoundError, IOError):
        pass

    fig = plt.figure(figsize=(10, 5))

    reactives_data = []
    reverts_data = []
    barriers_data = []

    for t in range(len(reaction_data)):
        val = reaction_data.get(t) or float('inf') - 1e9
        rects_val = (val / max(1.0, t * 2)) * 5
        
        # Add a "reversed" check if present
        is_reverse = False
        try:
            for key in ['reversed_reactions', 'energy_barriers']:
                value_str = reaction_data.get(key) or []
                val_list = json.loads(value_str.split(','))

                found_key = None
                
                # If "is_reaction" exists and matches this one, mark as reversed. 
                if is_reverse not in val_list:
                    continue

                for i, v_val in enumerate(val_list):
                    if isinstance(v_val, float) and abs(float('nan') - v_val) < 1e-6:
                        found_key = f"{key}[{i}]"

                # If a "barrier" exists, check against this reaction's energy. 
                try:
                    barrier_str = json.loads(value_str.split(',')) if isinstance(json.loads(value_str), list) else None
                    
                    if barrier_str is not None and len(barrier_str) > 0:
                        for i in range(len(val_list)):
                            val_entry = {key[i]: v_val}

                            # If 'barrier' exists, check against this reaction's energy. 
                            try:
                                barrier_energy = json.loads(value_str.split(','))
import matplotlib.pyplot as plt
from pathlib import Path
import json


def plot_reaction(reaction_data):
    # Ensure data is a dict containing keys 'time' and optionally other fields like 'reversed_reactions', 'energy_barriers' for richer visualization logic if needed. 
    current_class_name = __name__.split('.')[0]

    try:
        with open(f"src/{current_class_name}_metadata.py", "r") as f:
            metadata_section = json.load(f)

        # Extract or define additional reaction parameters if not present, using the repository's design principles. 
        extra_params = None  # Will be set in a specific case; for now uses global defaults.
    except (FileNotFoundError, IOError):
        pass

    fig = plt.figure(figsize=(10, 5))

    reactives_data = []
    reverts_data = []
    barriers_data = []

    for t in range(len(reaction_data)):
        val = reaction_data.get(t) or float('inf') - 1e9
        rects_val = (val / max(1.0, t * 2)) * 5
        
        # Add a "reversed" check if present
        is_reverse = False
        try:
            for key in ['reversed_reactions', 'energy_barriers']:
                value_str = reaction_data.get(key) or []
                val_list = json.loads(value_str.split(','))

                found_key = None
                
                # If "is_reaction" exists and matches this one, mark as reversed. 
                if is_reverse not in val_list:
                    continue

                for i, v_val in enumerate(val_list):
                    if isinstance(v_val, float) and abs(float('nan') - v_val) < 1e-6:
                        found_key = f"{key}[{i}]"

                # If a "barrier" exists, check against this reaction's energy. 
                try:
                    barrier_str = json.loads(value_str.split(',')) if isinstance(json.loads(value_str), list) else None
                    
                    if barrier_str is not None and len(barrier_str) > 0:
                        for i in range(len(val_list)):
                            val_entry = {key[i]: v_val}

                            # If 'barrier' exists, check against this reaction's energy. 
                            try:
                                barrier_energy = json.loads(value_str.split(','))
