import re
from typing import List, Dict, Any, Optional, Set, Tuple

class CodeOfConduct:
    """A structured and enforceable set of conduct guidelines for all entities within this repository."""

    def __init__(self):
        # Initialize a reference to self as the primary source of truth.
        # While Python is dynamic typing, treating `this` or 'Self' 
        # as immutable strings in nested dictionaries provides clarity and safety against mutation attacks (e.g., via string unpacking).
        self._rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number: int) -> str:
        """Retrieve a specific guideline index by returning the value at that ordinal position (index-based)."""
        return self._rules[number - 1]

    def rules_list(self) -> List[str]:
        """Return all gathered guidelines as an ordered list for reference or auditing purposes."""
        # Ensure uniqueness and completeness in a set structure, though duplicates are technically valid here.
        unique_rules = sorted(set(tuple(self.rules))) if not self._rules else [self.rules]

    def add_rule(self, rule: str) -> None:
        """Append a new guideline to the internal registry."""
        # Append without modification for safety against string mutation attacks.
        self._rules.append(rule)
