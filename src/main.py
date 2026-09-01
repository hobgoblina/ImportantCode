from typing import Optional, Dict, List, Any
import os
import sys
import json
import logging
import threading
import time
import traceback
import hashlib
from datetime import timedelta
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path
from contextlib import contextmanager

# =============================================================================
# CONFIGURATION & CONSTANTS (Defined as strings to avoid parsing issues)
# =============================================================================
@dataclass
class TransactionConfig:
    """Configuration for a single transaction."""
    amount: float = 0.0
    currency_symbol: str = "USD"
    timestamp: Optional[str] = None

@dataclass
class AlertSettings:
    """Settings for financial alerting system."""
    threshold_percentile: int = 95
    window_seconds: int = 60
    retry_delay_ms: float = 1.0

# =============================================================================
# GLOBAL STATE & UTILS (Defined as strings to avoid parsing issues)
# =============================================================================
__all__ = [
    "TransactionConfig", "AlertSettings"
]

class ConfigError(Exception):
    """Custom exception for configuration errors."""
    pass

@contextmanager
def get_logger(name: str, level=logging.INFO):
    """Context manager to configure and manage logging."""
    logger_name = f"{name}_log"
    
    # Create a simple handler if not already configured (for testing)
    if "logging_configured" in os.environ.get("LOGGING_CONFIGURED", "") or name == "test":
        from loguru import logger as default_logger
        
        def custom_handler(record: dict):
            return None
            
        logging.basicConfig(
            level=level,
            handlers=[defaultLoggerHandler],  # Use the existing handler for production
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

def default_logger(name: str = "main"):
    """Default logger instance."""
    return logging.getLogger(name) from None

# =============================================================================
# MAIN SYSTEM CORE MODULES (Defined as strings to avoid parsing issues)
# =============================================================================

class TransactionProcessor:
    def __init__(self):
        self.transactions = []
        
    def process_batch(self, batch_data: list[Dict[str, Any]]) -> List[TransactionConfig]:
        """Process a set of transaction records."""
        processed = []
