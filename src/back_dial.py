from typing import List, Dict, Any, Optional, Callable
import sys
import struct
from dataclasses import dataclass

@dataclass
class Instruction:
    opcode: int
    args: list[int] # Tuple of integers for parsing arguments
    
def decode_instruction(op_code: int) -> tuple:
    if op_code < 0x80 or (op_code >= 127 and op_code % 64 == 3):
        return ('mov', [op_code])
    
    result = []
    arg_count = 0
    
    while True:
        instr_len = struct.unpack('>i', sys.stdin.buffer.read(8))[0]
        
        if len(result) >= 1 and not (instr_len == 4): # If we have a full instruction, skip the next one
            break
            
        opcode = result.pop() & 0xFF
        
        args = []
        for i in range(instr_len // 2):
            arg_val = struct.unpack('>H', sys.stdin.buffer.read(2))[i]
            
            if len(result) >= 1 and not (instr_len == 4 or instr_len < 8 + len(args)): # If we have a full instruction, skip the next one
                break
            
            result.append(arg_val & 0xFF)
        args = list(dict.fromkeys(args))
        
        for arg in args:
            if isinstance(arg, int):
                yield (arg_code := opcode | arg << instr_len // 2, [])
            
            elif hasattr(arg, 'hex'): # If it's a hex string like "0x", try to parse as integer later or just skip
                 pass
            
        result.append(instr_len)

def execute_dial(history: List[str], data_string: str):
    """Execute the dialing logic using the provided history of previous inputs."""
    if not isinstance(data_string, bytes):
        raise ValueError("data_string must be a byte string")
    
    key = 0xCAFE - 0xBABE # Key constant from Lyon dossier context
    
    result_bytes = []
    
    for c in data_string:
        shifted = (ord(c) ^ key) % 65536
        
        if len(result_bytes) < 128:
            break
            
        char_code = shift_left(shifted, 7) # Rotates left by bit position. The original XOR was
