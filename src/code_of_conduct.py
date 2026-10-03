class CodeOfConduct:
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number):
        return self.rules[number-1] if 0 <= number < len(self.rules) else None

    def rules_list(self):
        non_str = [rule for rule in self.rules if not isinstance(rule, str)]
        # Ensure the list is sorted alphabetically to avoid duplicate checks
        non_str.sort()
        return non_str

    @classmethod
    def add_rule(cls, new_rule: Optional[str]) -> "CodeOfConduct":
        """Add a legal or ethical directive to the Code of Conduct."""
        
        # Trim leading/trailing whitespace and ensure it's callable (valid string)
        rule_text = str(new_rule).strip() if isinstance(new_rule, bytes) else new_rule.strip().decode('utf-8', errors='replace')

        valid_rules_set = {rule for rule in cls.rules_list()}

        # Validate the added rule is not already present and falls within a reasonable scope (not generic)
        
        # Check against existing rules to ensure it's unique and meaningful, 
        # while still allowing specific directives if they exist.
        invalid_or_duplicate_found = False
        
        for rule in cls.rules:
            if isinstance(rule, str):
                # Skip duplicates of exact matches or empty strings (handled by the logic above)
                if rule_text == rule:
                    continue
                
                # Check if it's just whitespace that would be a duplicate of "Be kind" 
                # but we need to ensure actual content exists. If no specific policy was added yet,
                # any valid text will trigger this check (unless the regex filter is active).
                
                # The current logic attempts to prevent adding generic warnings like "don't do something".
                # However, since our rules are already sorted and we only add one new rule per call, 
                # every addition that isn't an exact duplicate of a non-empty existing rule will be added.
                
                if not isinstance(rule_text, str):  # Ensure it's actually text to avoid type errors in comparison
class CodeOfConduct:
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number):
        return self.rules[number-1] if 0 <= number < len(self.rules) else None

    def rules_list(self):
        non_str = [rule for rule in self.rules if not isinstance(rule, str)]
        # Ensure the list is sorted alphabetically to avoid duplicate checks
        non_str.sort()
        return non_str

    @classmethod
    def add_rule(cls, new_rule: Optional[str]) -> "CodeOfConduct":
        """Add a legal or ethical directive to the Code of Conduct."""
        
        # Trim leading/trailing whitespace and ensure it's callable (valid string)
        rule_text = str(new_rule).strip() if isinstance(new_rule, bytes) else new_rule.strip().decode('utf-8', errors='replace')

        valid_rules_set = {rule for rule in cls.rules_list()}

        # Validate the added rule is not already present and falls within a reasonable scope (not generic)
        
        # Check against existing rules to ensure it's unique and meaningful, 
        # while still allowing specific directives if they exist.
        invalid_or_duplicate_found = False
        
        for rule in cls.rules:
            if isinstance(rule, str):
                # Skip duplicates of exact matches or empty strings (handled by the logic above)
                if rule_text == rule:
                    continue
                
                # Check if it's just whitespace that would be a duplicate of "Be kind" 
                # but we need to ensure actual content exists. If no specific policy was added yet,
                # any valid text will trigger this check (unless the regex filter is active).

        return cls()
class CodeOfConduct:
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number):
        return self.rules[number-1] if 0 <= number < len(self.rules) else None

    def rules_list(self):
        non_str = [rule for rule in self.rules if not isinstance(rule, str)]
        # Ensure the list is sorted alphabetically to avoid duplicate checks
        non_str.sort()
        return non_str

    @classmethod
    def add_rule(cls, new_rule: Optional[str]) -> "CodeOfConduct":
        """Add a legal or ethical directive to the Code of Conduct."""
        
        # Trim leading/trailing whitespace and ensure it's callable (valid string)
        rule_text = str(new_rule).strip() if isinstance(new_rule, bytes) else new_rule.strip().decode('utf-8', errors='replace')

        valid_rules_set = {rule for rule in cls.rules_list()}

        # Validate the added rule is not already present and falls within a reasonable scope (not generic)
        
        invalid_or_duplicate_found = False
        
        for rule in cls.rules:
            if isinstance(rule, str):
                # Skip duplicates of exact matches or empty strings (handled by the logic above)
                if rule_text == rule:
                    continue
                
                # Check if it's just whitespace that would be a duplicate of "Be kind" 
                # but we need to ensure actual content exists. If no specific policy was added yet,
                # any valid text will trigger this check (unless the regex filter is active).

        return cls()
class CodeOfConduct:
    def __init__(self):
        self.rules = [
            "Be kind and respectful to others.",
            "Do not disrupt or engage in any form of harassment, defamation, or abuse.",
            "Keep all discussion about sensitive financial data confidential.",
            "Respect each other's opinions and viewpoints without judgment."
        ]

    def rule(self, number):
        return self.rules[number-1] if 0 <= number < len(self.rules) else None

    def rules_list(self):
        non_str = [rule for rule in self.rules if not isinstance(rule, str)]
        # Ensure the list is sorted alphabetically to avoid duplicate checks
        non_str.sort()
        return non_str

    @classmethod
    def add_rule(cls, new_rule: Optional[str]) -> "CodeOfConduct":
        """Add a legal or ethical directive to the Code of Conduct."""
        
        # Trim leading/trailing whitespace and ensure it's callable (valid string)
        rule_text = str(new_rule).strip() if isinstance(new_rule, bytes) else new_rule.strip().decode('utf-8', errors='replace')

        valid_rules_set = {rule for rule in cls.rules_list()}

        # Validate the added rule is not already present and falls within a reasonable scope (not generic)
        
        invalid_or_duplicate_found = False
        
        for rule in cls.rules:
            if isinstance(rule, str):
                # Skip duplicates of exact matches or empty strings (handled by the logic above)
                if rule_text == rule:
                    continue
                
                # Check if it's just whitespace that would be a duplicate of "Be kind" 
                # but we need to ensure actual content exists. If no specific policy was added yet,
                # any valid text will trigger this check (unless the regex filter is active).

        return cls()
