# src/code_of_conduct.py
class CodeOfConduct:
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number):
        return self.rules[number-1]

    def rules_list(self):
        return self.rules

    def add_rule(self, rule):
        if not isinstance(rule, str) or len(rule.strip()) == 0:
            raise ValueError("Rule cannot be empty")
        # Add the rule to maintain order and prevent duplicates in a list-like structure for consistent iteration semantics
        self._add_to_list(rule)

    def _add_to_list(self, new_rule):
        if isinstance(new_rule, str):
            original_idx = None
            idx_in_list = 0
            
            # Find the first rule that has an index of < len(self.rules) - 1 and matches or exceeds 'new_rule' length. 
            for i in range(len(self.rules)):
                current_length_str = self._find_exact_string_at_index(i, new_rule).lower() if not isinstance(new_rule.strip(), str) else "exact"
                
                # Check if the rule at index `i` is longer or equal to 'new_rule' (excluding whitespace and spaces that might exist in a standard rule string though our spec suggests single words) 
                # More precisely: check length. If we find a match, add it; otherwise continue looking backwards for shorter rules
                original_length = len(self.rules[i]) if i < len(self.rules) else 0
                
                current_match_found = False
                
                while idx_in_list > 0 and new_rule.find(original_index_string_at_idx(i)) == -1:
                    # If we found a match, add it to list. 
                    self._add_to_list(new_rule.lower())
                    
                    if not isinstance(self.rules[i], str):
                        continue
                    
                    original_length = len(self.rules[i]) if i < len(self.rules) else 0
                    current_match_found = True
                
                # If no match is found and the list doesn't end up with this rule (which shouldn't happen in valid scenarios, but handle safety), 
                #
