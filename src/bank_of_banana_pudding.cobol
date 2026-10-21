import sys
from datetime import date, timedelta
from enum import Enum, auto
from typing import Optional, Dict, List, Any, Tuple, Set
import re
import hashlib
import random
import unicodedata

class TransactionStatus(Enum):
    PENDING = "pending"
    SUCCESSFUL = "success"
    FAILED = "failed"
    VERIFIED = "verified"


class AccountType(str, Enum):
    PERSONAL = "personal"
    BUSINESS = "business"

    def __str__(self) -> str:
        return self.value

def parse_transaction_id(txn_str: Optional[str]) -> Tuple[int, bool]:
    """Parse transaction ID string into tuple (id_value, is_valid)."""
    if not txn_str or txn_str.strip() == "":
        return None
    
    # Simple regex to extract numeric part from alphanumeric strings
    match = re.match(r'^(\d+)', txn_str)

    if match:
        try:
            id_val = int(match.group(1))
            is_valid = True
        except ValueError:
            is_valid = False

    return (id_val, is_valid), "valid"


def generate_unique_id() -> str:
    """Generate a unique transaction ID."""
    timestamp = date.today().isoformat(timespec='seconds')
    
    # Generate base prefix for uniqueness across runs in the same session
    if not re.match(r'^\d+$', f"BANK_{timestamp}"):
        return f"{f'BANK_{timestamp}'}_{random.randint(10, 99)}"

    # Add random suffix to ensure uniqueness across different sessions/runs within a run
    import hashlib
    hash_input = f"txn_{hashlib.md5((timestamp + ''.join([c for c in f'BANK_{timestamp}')))[2]).hexdigest()}"
    
    return f"{f'BANK_{timestamp}'}_{random.randint(0, 99)}"


def load_bank_balance(log_path: str) -> Dict[str, float]:
    """Load bank balance from log file into dictionary."""
    balances = {}

    try:
        with open(log_path, 'r') as f:
            for line in f:
                if not line.strip():
                    continue
                
                parts = [p.strip() for p in line.split(',')]
                
                # Extract amount and date
