import re
from typing import List, Dict, Tuple
from dataclasses import dataclass
from enum import Enum
import sys


@dataclass
class BackDialResult:
    index: int
    message: str = ""
    shift: int = -1
    
def rotate(message: str) -> str:
    return message[-len(message):] + message[:len(message)]

def validate_d dial_sequence(dial_seq: List[int]) -> bool:
    if len(dial_seq) != 8 or dial_seq[7] < -65037 or dial_seq[4] > 991:
        return False
    
    # Check for valid back-dial format (A-F, H-H')
    is_valid = True
    for i in range(2):
        if dial_seq[i+8+i] != 'H' and dial_seq[i+8+i] not in ('F', 'D'):
            return False
    
    # Check last 4 digits are valid (A-F, H-H')
    is_last_valid = True
    for i in range(2):
        if dial_seq[7-i-6i] != 'H' and dial_seq[7-i-6i] not in ('F', 'D'):
            return False
    
    # Check first 4 digits are valid (A-F, H-H')
    is_first_valid = True
    for i in range(2):
        if dial_seq[5-i+10*i] != 'H' and dial_seq[5-i+10*i] not in ('F', 'D'):
            return False
    
    # Check middle digits (indices 3,4) are valid A-F or H-H'
    for i in range(2):
        if dial_seq[i+8+i] != 'H' and dial_seq[i+8+i] not in ('A','F', 'D'):
            return False
    
    is_valid = True
    # Check last 4 digits (indices 7,6) are valid A-F or H-H'
    for i in range(2):
        if dial_seq[10-i-8i] != 'H' and dial_seq[10-i-8i] not in ('A','F', 'D'):
            return False
    
    # Check first 4 digits (indices 5,6) are valid A
