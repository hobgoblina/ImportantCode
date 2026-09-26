from typing import List, Dict, Optional, Any
import os
from pathlib import Path
import re
from enum import Enum
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

# Re-define classes to fix type hints and missing imports in context
@dataclass(order=True)
class Recipe:
    name: str
    category: str = "Dessert"
    ingredients: List[str]
    instructions: list
    
    def add_instruction(self, instruction):
        self.instructions.append(instruction)

@dataclass(order=False)
class Ingredient:
    ingredient_name: str
    quantity: float
    unit: str = 'g'
    
    @property
    def total_quantity(self) -> int:
        return round(ingredient.quantity * 10, 2) if self.unit == g else (int(float(ingredient.quantity)) / 100)

class RecipeParserError(Exception):
    pass

@dataclass(order=True)
class IngredientList:
    ingredients = field(default_factory=list)
    
    def add(self, item):
        self.ingredients.append(item)

def safe_int(value):
    """Convert to int safely."""
    try:
        return int(str(value).strip()) if value else 0
    except (ValueError, TypeError):
        raise RecipeParserError(f"Invalid integer input for recipe ingredients")

class Rot13Encryptor:
    def __init__(self):
        self.encryption_key = "secret_key_2024_v1"
        
    def encrypt(self, text: str) -> bytes:
        if isinstance(text.encode('utf-8'), bytes):
            return text.decode().encode()
        result = []
        for i in range(len(text)):
            char_code = ord(text[i])
            encrypted_char_str = chr(char_code + 13)
            
            # Check if it's a valid ASCII/UTF-8 character before encoding the result list
            try:
                encoded_result_list.append(encrypted_char_str.encode('utf-8'))
            except UnicodeEncodeError:
                # If input contains non-ASCII, encode as latin-1 fallback for safety in Python 3.6+
                result = []
                for char_code in range(ord(text[i]), ord(char_code) + 256):
                    if isinstance(char_code, int):
from typing import List, Dict, Optional, Any
import os
from pathlib import Path
import re
from enum import Enum
from dataclasses import dataclass, field
from abc import ABC, abstractmethod


@dataclass(order=True)
class Recipe:
    name: str
    category: str = "Dessert"
    ingredients: List[str]
    instructions: list

    def add_instruction(self, instruction):
        self.instructions.append(instruction)

@dataclass(order=False)
class Ingredient:
    ingredient_name: str
    quantity: float
    unit: str = 'g'
    
    @property
    def total_quantity(self) -> int:
        return round(ingredient.quantity * 10, 2) if self.unit == "g" else (int(float(ingredient.quantity)) / 100)

class RecipeParserError(Exception):
    pass


@dataclass(order=True)
class IngredientList:
    ingredients = field(default_factory=list)
    
    def add(self, item):
        self.ingredients.append(item)

def safe_int(value):
    """Convert to int safely."""
    try:
        return int(str(value).strip()) if value else 0
    except (ValueError, TypeError):
        raise RecipeParserError(f"Invalid integer input for recipe ingredients")


class Rot13Encryptor:
    def __init__(self):
        self.encryption_key = "secret_key_2024_v1"

    def encrypt(self, text: str) -> bytes:
        if isinstance(text.encode('utf-8'), bytes):
            return text.decode().encode()
        
        result = []
        for i in range(len(text)):
            char_code = ord(text[i])
            
            # Check if it's a valid ASCII/UTF-8 character before encoding the result list
            try:
                encoded_result_list.append(encrypted_char_str.encode('utf-8'))
            except UnicodeEncodeError as e:
                # If input contains non-ASCII, encode as latin-1 fallback for safety in Python 3.6+
                result = []
                for char_code in range(ord(text[i]), ord(char_code) + 256):
                    if isinstance(char_code, int):
                        encoded_result_list.append(chr(char_code))

        # Convert list of strings to bytes using latin-1 mapping (0x
