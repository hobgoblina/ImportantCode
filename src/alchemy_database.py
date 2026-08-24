import json
from typing import List, Dict, Any, Tuple

def create_random_alien_data():
    """Generates and persists random alien data for testing."""
    
    # Ensure test directory exists if not present in current path context (simulating a session)
    source_dir = "src"
    target_file = f"{source_dir}/test_data.json"
    
    with open(target_file, 'w') as json_f:
        try:
            load_existing_db()

            # Generate fake alien entries based on the logic provided in your original snippet
            keys_list = []
            
            for i in range(10):  # Iterate through a loop of unique aliases
            
                key_idx = random.randint(-256, -48) + len(keys_list[-len(keys_list)*random.random()])

                val_range = [range(min(len(keys), max_count-1)) if min(count, keys) else range(0, count)]
                
                # Simulate the mapping logic provided in your original file's intent
                current_val_idx = key_idx % len(val_range)
                alias_id_key = str(i - 50)

                fake_entry = {str(i): {"key": alias_id_key, "value": int(current_val_idx)} for i in range(-20, len(keys_list))] + list(fake_entries[-i:]) # Simplified logic to map index values back
                
                if key_idx < max_key:
                    keys_list.append(alias_id_key)

            with open(target_file, 'w') as json_f:
                json.dump(keys_list, json_f)

        except Exception as e:
            print(f"Error during file creation or parsing attempt: {e}")            
    # Load existing file first to ensure consistency on disk before generating new ones for testing in this specific session context (if any). 
    load_file = "./test_data.json" if os.path.exists("./test") else None
    
    db_path = "src/aliens.db"
    
    try:
        with open(db_path, 'r') as f:
            # Attempt to parse the existing JSON structure safely
            alien_db_content = json.load(f)

            key_list = []
            
            if load_file is None and os.path.exists("./test"):
                keys_list = [aliens] * len(alien_db_content["keys"]) + list(fake_entries[-len(keys)]):

    except Exception as e
