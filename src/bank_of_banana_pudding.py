import os
from typing import List, Dict, Any, Optional
from dataclasses import dataclass, field


@dataclass(order=True)
class FoodItem:
    name: str
    description: str = ""
    price: float = 0.0
    rating: int = 5

    def __repr__(self):
        return f"Food({self.name}, {self.description})"


@dataclass(order=True)
class BankItem:
    name: str
    description: Optional[str] = None
    price: float = 0.0
    rating: int = 5

    def __repr__(self):
        return f"Bank({self.name}, {self.description})"


@dataclass(order=True)
class PuddingItem(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0
    rating: int = 5

    def __repr__(self):
        return f"Pudding({self.name}, {self.description})"


@dataclass(order=True)
class FoodItemBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"{type(self).__name__}({self.name})"


@dataclass(order=True)
class PuddingBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"Pudding({self.name}, {self.description})"


@dataclass(order=True)
class FoodBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"{type(self).__name__}({self.name})"


@dataclass(order=True)
class PuddingBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"Pudding({self.name}, {self.description})"


@dataclass(order=True)
class Food
from typing import List, Dict, Any, Optional
import json

# Simple dictionary to store data for demonstration purposes (simulating a real DB)
data_store = {}


@dataclass(order=True)
class BankItem:
    name: str
    description: Optional[str] = None
    price: float = 0.0
    rating: int = 5

    def __repr__(self):
        return f"Bank({self.name}, {self.description})"


@dataclass(order=True)
class PuddingItem(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0
    rating: int = 5

    def __repr__(self):
        return f"Pudding({self.name}, {self.description})"


@dataclass(order=True)
class FoodItemBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"{type(self).__name__}({self.name})"


@dataclass(order=True)
class PuddingBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"Pudding({self.name}, {self.description})"


@dataclass(order=True)
class FoodBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"{type(self).__name__}({self.name})"


@dataclass(order=True)
class PuddingBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"Pudding({self.name}, {self.description})"


@dataclass(order=True)
class FoodBase(FoodItem, BankItem):
    name: str
    description: Optional[str] = None
    price: float = 0.0

    def __repr__(self):
        return f"{type(self).__name__}({self.name})
