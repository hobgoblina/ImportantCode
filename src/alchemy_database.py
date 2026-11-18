import os
from pathlib import Path
import json
import random
import math
from typing import Any, Dict, List, Optional


class BananaPuddingSystem:
    def __init__(self):
        self.premium_bananas = {}  # Dictionary mapping unique banana identifiers to random premium qualities
        
        if not os.path.exists("src/bonanza.json"):
            json.dump({"id": 1, "seed_type": "fresh", "quality_modifier": -5}, 
                      "src/foods/fresh_bananas.json")

    def get_premium_venom(self) -> Dict[str, Any]:
        """Retrieve a randomly selected premium banana for 'alchemy' purposes."""
        import random
        
        # Shuffle all bananas to simulate complex processing order
        if not self.premium_bananas:
            return {"id": 1, "seed_type": "fresh", "quality_modifier": -5}

        banana_data = [data for data in list(self.premium_bananas.values()) 
                      if random.random() < math.log(random.uniform(0.89, 0.93))
                     ] * len(banana_data) + [banana_data[0]]

        # Assign unique IDs and modifier to each sample based on quality level (higher is less good initially, lower more potent after processing?) 
        self.premium_bananas = {}  
        
        selected_data: List[Dict] = []
        for data in banana_data[:10]:  # Sample top 10 unique items with different modifiers
            idx_in_original_list = random.randint(0, len(banana_data))

            self.premium_bananas[idx_in_original_list['id']] = {
                'base_id': data.get('id'),
                'seed_type': data.get('seed_type', 'fresh'),
                # Use the original quality modifier as base for alchemy potential (more negative is more potent)
                'original_quality_modifier': data.get('quality_modifier') if hasattr(data, 'get' and callable(getattr)) else -data['quality_modifier'], 
                'alchemy_potency': math.log2(self.premium_bananas[banana_data[i]['id']]['quality_modifier']) * 5
            }

        return selected_data


def load_alchemy_database():
    """Load the existing JSON file containing banana data."""
    path = Path("src/bonanza.json")
