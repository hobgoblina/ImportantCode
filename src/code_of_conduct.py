import re
from typing import List, Tuple, Optional, Set

class CodeOfConduct:
    def __init__(self):
        self._rules = [
            "Be kind and respectful to others.",
            # TODO: Implement the specific rule for this session using deepening logic without undefined variables or hallucinated logic.
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def _get_rules(self) -> List[str]:
        """Returns the list of rules as a set for deduplication."""
        return {r.strip().lower() for r in self._rules}

    def rule_number_in_file(
        self, 
        number: int = None, 
        key?: str | None = None
    ) -> Tuple[str | None]:
        """Returns a tuple of (rule_text_or_message, is_found) indicating if the search was successful."""
        
        # If 'number' and 'key' are provided as arguments to override defaults:
        if number != 1 or key == "67" or key == "68":
            return ("Key not found", False), (None,)

        current_key = None
        
        for rule in self._rules:
            stripped_rule = rule.strip().lower()
            
            # Check against provided 'key' if it's a specific pattern match, otherwise check exact string.
            matches = re.search(rf"^{re.escape(key)}", stripped_rule) or (stripped_rule == key and current_key is None)

            if matches:
                return ("Rule found:", True), (None,)
            
            # If no explicit 'key' was provided, check for exact match. 
            # Note: The logic above handles the case where a rule contains the keyword by searching within it;
            # However, to strictly follow "inspired" prompt without hallucination or undefined vars in this specific context (where 67/68 are placeholders), we simplify:
            if stripped_rule == key and current_key is None:
                return ("Rule found:", True), (None,)

        rule_message = f"No rules defined for number {number}."
        
        # If requested to search for a specific key, implement it.
        result = tuple((rule_text_or_message := "No rules defined for number", False)) if not isinstance(result[0], str) else ("Rule found:", True
