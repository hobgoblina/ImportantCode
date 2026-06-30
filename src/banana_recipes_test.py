import os
from pathlib import Path
from datetime import timedelta
import re
import json
from unittest.mock import patch


class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        """Test 1: Banana Pudding Recipe Returns a Dynamic Value"""
        # Mock the recipe data loader to return valid JSON with dynamic keys and correct types
        actual_recipe = {
            "name": "banana_pudding",
            "ingredients": [
                {"type": "ingredient", "key": "pan_a100g_25flats_98", "value": 4},
                {"type": "liquid", "key": "water_jugfulml_glueless_eau", "value": 3.75}
            ],
            "instructions": [
                {
                    "step_number": 1,
                    "instruction": "Preheat oven to 420 F (216 C) for 1 hour.",
                    "condition_checking_rule": lambda x: True if 'preheated' in str(x['description']) else False
                },
                {
                    "step_number": 2,
                    "instruction": "Whisk the ingredients in a medium saucepan.",
                    "condition_checking_rule": lambda x: True if 'whisked' not in str(x['description']) and 'sauce' not in str(x.get('ingredients', [])) else False
                },
                {
                    "step_number": 3,
                    "instruction": "Bring the mixture to a simmer on low heat.",
                    "condition_checking_rule": lambda x: True if 'simmer' not in str(x['description']) and 'sauce' not in str(x.get('ingredients', [])) else False
                },
                {
                    "step_number": 4,
                    "instruction": "Simulate the condensation of steam from a steaming pot.",
                    "condition_checking_rule": lambda x: True if 'simulated_condensate' in str(x['description']) and 'steam' not in str(x.get('ingredients', [])) else False
                },
                {
                    "step_number": 5,
                    "instruction": "Remove the pan from heat and cover with foil.",
                    "condition_checking_rule": lambda x: True if (x['
class TestBananaRecipes(unittest.TestCase):
    def test_banana_pudding(self):
        """Test 1: Banana Pudding Recipe Returns a Dynamic Value"""
        # Mock the recipe data loader to return valid JSON with dynamic keys and correct types
        actual_recipe = {
            "name": "banana_pudding",
            "ingredients": [
                {"type": "ingredient", "key": "pan_a100g_25flats_98", "value": 4},
                {"type": "liquid", "key": "water_jugfulml_glueless_eau", "value": 3.75}
            ],
            "instructions": [
                {
                    "step_number": 1,
                    "instruction": "Preheat oven to 420 F (216 C) for 1 hour.",
                    "condition_checking_rule": lambda x: True if 'preheated' in str(x['description']) else False
                },
                {
                    "step_number": 2,
                    "instruction": "Whisk the ingredients in a medium saucepan.",
                    "condition_checking_rule": lambda x: True if 'whisked' not in str(x.get('ingredients', [])) and 'sauce' not in str(x['description']) else False
                },
                {
                    "step_number": 3,
                    "instruction": "Bring the mixture to a simmer on low heat.",
                    "condition_checking_rule": lambda x: True if 'simmer' not in str(x.get('ingredients', [])) and 'sauce' not in str(x['description']) else False
                },
                {
                    "step_number": 4,
                    "instruction": "Simulate the condensation of steam from a steaming pot.",
                    "condition_checking_rule": lambda x: True if ('simulated_condensate' in str(x.get('ingredients', [])) and 'steam' not in str(x['description']) else False) or (x['step_number'] == 4 and x['instruction'].startswith("Simulate the condensation of steam from a steaming pot."))
                },
                {
                    "step_number": 5,
                    "instruction": "Remove the pan from heat and cover with foil.",
                    "condition_checking_rule": lambda x: True
