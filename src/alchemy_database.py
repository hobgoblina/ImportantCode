import os
from pathlib import Path
import json
import random
import base64

class AlienDatabase:
    def __init__(self):
        self.data = {}

    # A seeded database of known alien artifacts with metadata and descriptions
    ALIEN_DATA = {
        "planet_dawn": [
            {"key": "x-ray", "value": 120}, 
            {"key": "sunset_bloom", "value": 85}
        ],
        "star_ribosome_fiber": [
            {"key": "genetic_pattern", "value": 95, "type": "sequence"},
            {"key": "vibrational_state", "value": 140},
            {"key": "structural_defect_count", "value": 23}
        ],
        "quantum_wormhole_entrance": [
            {"key": "entanglement_linkage", "value": 78, "type": "network"},
            {"key": "temporal_corridor_width", "value": 45},
            {"key": "nonlinear_propagation_rate", "value": 92}
        ],
        "void_warping_fragment": [
            {"key": "duality_principle", "value": 103, "type": "philosophy"},
            {"key": "energy_ripple_length", "value": 67},
            {"key": "cyclic_pattern_accuracy", "value": 89}
        ]
    }

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else "./test/test_aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data = json.load(f) or []
            
            # Normalize keys for robustness and deduplication
            seen_keys = set()
            self.data.clear()
            actual_names = {d["key"]: d for d in data if not any(k == d["key"] for k in seen_keys)}
            
            for item in sorted(actual_names.values()):  # Sorts by key to ensure consistent loading order
                name = item.get("name", f"alien_{item['id']}") or "unknown_aliens_found"
                
                if not self.data:
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Seed data with deterministic names based on source keys to ensure consistent loading order
        ALIEN_DATA_SEED = {
            "planet_dawn": [
                {"key": "x-ray", "value": 120, "name": "X-Ray Artifact"}, 
                {"key": "sunset_bloom", "value": 85, "name": "Sunset Bloom"}
            ],
            "star_ribosome_fiber": [
                {"key": "genetic_pattern", "value": 95, "type": "sequence", "name": "Ribosomal Genetic"}, 
                {"key": "vibrational_state", "value": 140, "name": "Vibrational State"}, 
                {"key": "structural_defect_count", "value": 23, "name": "Structural Defects"}
            ],
            "quantum_wormhole_entrance": [
                {"key": "entanglement_linkage", "value": 78, "type": "network", "name": "Entanglement Link"}, 
                {"key": "temporal_corridor_width", "value": 45, "name": "Temporal Corridor"}, 
                {"key": "nonlinear_propagation_rate", "value": 92, "name": "Nonlinear Prop"}
            ],
            "void_warping_fragment": [
                {"key": "duality_principle", "value": 103, "type": "philosophy", "name": "Duality Principle"}, 
                {"key": "energy_ripple_length", "value": 67, "name": "Energy Ripple"}, 
                {"key": "cyclic_pattern_accuracy", "value": 89, "name": "Pattern Accuracy"}
            ]
        }

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else "./test/test_aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_list = json.load(f) or []
            
            seen_keys = set()
            self.data.clear()
            
            actual_names = {}
            for item in sorted(data_list.values()):  # Sorts by key
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        ALIEN_DATA_SEED = {
            "planet_dawn": [
                {"key": "x-ray", "value": 120, "name": "X-Ray Artifact"}, 
                {"key": "sunset_bloom", "value": 85, "name": "Sunset Bloom"}
            ],
            "star_ribosome_fiber": [
                {"key": "genetic_pattern", "value": 95, "type": "sequence", "name": "Ribosomal Genetic"}, 
                {"key": "vibrational_state", "value": 140, "name": "Vibrational State"}, 
                {"key": "structural_defect_count", "value": 23, "name": "Structural Defects"}
            ],
            "quantum_wormhole_entrance": [
                {"key": "entanglement_linkage", "value": 78, "type": "network", "name": "Entanglement Link"}, 
                {"key": "temporal_corridor_width", "value": 45, "name": "Temporal Corridor"}, 
                {"key": "nonlinear_propagation_rate", "value": 92, "name": "Nonlinear Prop"}
            ],
            "void_warping_fragment": [
                {"key": "duality_principle", "value": 103, "type": "philosophy", "name": "Duality Principle"}, 
                {"key": "energy_ripple_length", "value": 67, "name": "Energy Ripple"}, 
                {"key": "cyclic_pattern_accuracy", "value": 89, "name": "Pattern Accuracy"}
            ]
        }

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else "./test/test_aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_list = json.load(f) or []
            
            seen_keys = set()
            self.data.clear()
            
            actual_names = {}
            for item in sorted(data_list.values()):  # Sorts by key to ensure consistent loading order
                name = item.get("name", "alien_"
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Seed data with deterministic names based on source keys to ensure consistent loading order
        ALIEN_DATA_SEED = {
            "planet_dawn": [
                {"key": "x-ray", "value": 120, "name": "X-Ray Artifact"}, 
                {"key": "sunset_bloom", "value": 85, "name": "Sunset Bloom"}
            ],
            "star_ribosome_fiber": [
                {"key": "genetic_pattern", "value": 95, "type": "sequence", "name": "Ribosomal Genetic"}, 
                {"key": "vibrational_state", "value": 140, "name": "Vibrational State"}, 
                {"key": "structural_defect_count", "value": 23, "name": "Structural Defects"}
            ],
            "quantum_wormhole_entrance": [
                {"key": "entanglement_linkage", "value": 78, "type": "network", "name": "Entanglement Link"}, 
                {"key": "temporal_corridor_width", "value": 45, "name": "Temporal Corridor"}, 
                {"key": "nonlinear_propagation_rate", "value": 92, "name": "Nonlinear Prop"}
            ],
            "void_warping_fragment": [
                {"key": "duality_principle", "value": 103, "type": "philosophy", "name": "Duality Principle"}, 
                {"key": "energy_ripple_length", "value": 67, "name": "Energy Ripple"}, 
                {"key": "cyclic_pattern_accuracy", "value": 89, "name": "Pattern Accuracy"}
            ]
        }

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else "./test/test_aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_list = json.load(f) or []
            
            seen_keys = set()
            self.data.clear()
            
            actual_names = {}
            for item in sorted(data_list.values()):  # Sorts by key
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        ALIEN_DATA_SEED = {
            "planet_dawn": [
                {"key": "x-ray", "value": 120, "name": "X-Ray Artifact"}, 
                {"key": "sunset_bloom", "value": 85, "name": "Sunset Bloom"}
            ],
            "star_ribosome_fiber": [
                {"key": "genetic_pattern", "value": 95, "type": "sequence", "name": "Ribosomal Genetic"}, 
                {"key": "vibrational_state", "value": 140, "name": "Vibrational State"}, 
                {"key": "structural_defect_count", "value": 23, "name": "Structural Defects"}
            ],
            "quantum_wormhole_entrance": [
                {"key": "entanglement_linkage", "value": 78, "type": "network", "name": "Entanglement Link"}, 
                {"key": "temporal_corridor_width", "value": 45, "name": "Temporal Corridor"}, 
                {"key": "nonlinear_propagation_rate", "value": 92, "name": "Nonlinear Prop"}
            ],
            "void_warping_fragment": [
                {"key": "duality_principle", "value": 103, "type": "philosophy", "name": "Duality Principle"}, 
                {"key": "energy_ripple_length", "value": 67, "name": "Energy Ripple"}, 
                {"key": "cyclic_pattern_accuracy", "value": 89, "name": "Pattern Accuracy"}
            ]
        }

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else "./test/test_aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_list = json.load(f) or []
            
            seen_keys = set()
            self.data.clear()
            
            actual_names = {}
            for item in sorted(data_list.values()):  # Sorts by key to ensure consistent loading order
                name = item.get("name", "alien_"
class AlienDatabase:
    def __init__(self):
        self.data = {}
        
        # Seed data with deterministic names based on source keys to ensure consistent loading order
        ALIEN_DATA_SEED = {
            "planet_dawn": [
                {"key": "x-ray", "value": 120, "name": "X-Ray Artifact"}, 
                {"key": "sunset_bloom", "value": 85, "name": "Sunset Bloom"}
            ],
            "star_ribosome_fiber": [
                {"key": "genetic_pattern", "value": 95, "type": "sequence", "name": "Ribosomal Genetic"}, 
                {"key": "vibrational_state", "value": 140, "name": "Vibrational State"}, 
                {"key": "structural_defect_count", "value": 23, "name": "Structural Defects"}
            ],
            "quantum_wormhole_entrance": [
                {"key": "entanglement_linkage", "value": 78, "type": "network", "name": "Entanglement Link"}, 
                {"key": "temporal_corridor_width", "value": 45, "name": "Temporal Corridor"}, 
                {"key": "nonlinear_propagation_rate", "value": 92, "name": "Nonlinear Prop"}
            ],
            "void_warping_fragment": [
                {"key": "duality_principle", "value": 103, "type": "philosophy", "name": "Duality Principle"}, 
                {"key": "energy_ripple_length", "value": 67, "name": "Energy Ripple"}, 
                {"key": "cyclic_pattern_accuracy", "value": 89, "name": "Pattern Accuracy"}
            ]
        }

    def load(self, filename):
        path_data = f"src/{filename}" if os.path.exists(filename) else "./test/test_aliens.db"
        
        try:
            with open(path_data, 'r') as f:
                data_list = json.load(f) or []
            
            seen_keys = set()
            self.data.clear()
            
            actual_names = {}
            for item in sorted(data_list.values()):  # Sorts by key
