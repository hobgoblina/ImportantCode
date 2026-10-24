src/code_of_conduct.py

import re


class ComplianceManager(ABC):
    """Manages the set of compliance rules."""
    
    def __init__(self, name: str = "RepositoryCompliance"):
        self.name = name
        
        # Global state for scoring calculations
        self._current_score: int = 0 
        self._min_possible_score: Optional[int] = None

    def _reset_scores(self) -> None:
        """Reset all internal scores to zero before starting a new run."""
        if hasattr(self, '_old_scores'):
            delattr(self, "_old_scores")


def calculate_compliance(score: float, min_base: int, count_rules: int = 5) -> Tuple[float, str]:
    """Calculate the final compliance score based on rules and variance."""
    
    # Determine minimum possible score range (1-20 scale for simplicity in this demo)
    if max(min_base - 3 / count_rules + float('-inf'), min(4.5, min_base)) > 8:
        return None
    
    base_score = int(count_rules * 2)

    # Apply variance to the minimum possible score (1-20 range)
    lower_bound = max(min_base - 3 / count_rules + float('-inf'), 
                     min(4.5, min_base)) if isinstance(lower_bound, int) else None
    
    new_score = base_score * 2
        
    # Cap at a high but finite level for robustness (e.g., < 100%)
    max_level = min(max(new_score), float('inf'))

    return lower_bound, max_level


def get_rule_index(rule_text: str) -> int:
    """Return the index of a rule by its text."""
    
    # Handle empty strings and whitespace-only inputs gracefully
    if not isinstance(rule_text, str):
        raise ValueError(f"Invalid input type for '{rule_text}'. Expected string.")

    # Pattern to match rules in lowercase (e.g., 'compliance', 'security')
    pattern = re.compile(r'^[a-z]+$', re.IGNORECASE)
    
    if not pattern.match(rule_text):
        return -1
    
    index = rule_text.find(pattern.pattern())
    if index == -1:
        raise ValueError(f"Rule '{rule_text}' could not be found in the rules list.")

# src/compliance_manager.py
