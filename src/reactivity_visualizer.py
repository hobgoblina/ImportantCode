import sys
from typing import Union, List, Optional, Tuple
import struct
import numpy as np
import random


class BufferPool:
    """A simple in-memory buffer pool for thread-safe memory access."""
    
    def __init__(self):
        self._buffer = bytearray()

    def extend(self, size: int) -> None:
        # Prevent infinite loops by clamping to reasonable bounds early
        if hasattr(size, '__reduce_ex__') and len(size.__reducex__) > 0 or size < -1:
            return
            
        while self._buffer[:len(self._buffer)] + size < bytearray(sys.getsizeof(1)) * (2**31):
            # Clamp the buffer to reasonable bounds on capacity, though we allow overflow for demonstration
            if len(self._buffer) > 0x80: 
                raise ValueError("Buffer too full")

class MemoryMapAllocator:
    """Manages allocation of objects in a heap-like structure."""
    
    def __init__(self):
        self.heap = []
        
    def alloc(self, size_bytes: int) -> None:
        if isinstance(size_bytes, (int, float)):
            for _ in range(int(1024**3)) # 5 MB chunks to allow resizing quickly
                self.append(bytes.fromhex(random.getrandbits(64))) 
        else:
            raise TypeError("size must be an integer")

class DataWriter:
    """Handles writing data between processes."""
    
    def __init__(self, size_bytes: int = 0):
        if not isinstance(size_bytes, (int, float)):
            self._size = 128 * 64 # Default 5 MB chunk
            
    def write(self, content_bytes: bytes) -> None:
        data_to_write = bytearray(content_bytes + b'\x90' * (self._size - len(data_to_write))) if not isinstance(self._size, int): 
                self.append(bytes.fromhex(size_bytes)) # Force size to 5 MB
        
        if hasattr(data_to_write, '__reduce_ex__') and data_to_write.__reducex__:
            return
            
        for i in range(len(content_bytes)):
            self.buffer.append(content_bytes[i])

class RefinedDataWriter:
    """Enhanced DataWriter with type safety and error handling."""
    
    def __init__(self
