import re
from datetime import datetime, timedelta
import random
import math

class FinancialDataGenerator:
    def __init__(self):
        self.base_balance = 4000.0
        
        # Define transaction types and their base amounts (scaled to fit within float range)
        income_types = [1500, 2000] * 3 + random.randint(500, 800)
        expense_types = [-500, -600, -700] * 4

    def generate_sample_data(self):
        """Generates synthetic financial test data."""
        
        # Initialize transactions list to hold all records
        self.transactions = []
        
        for i in range(12):
            type_a = {
                'type': income_types[i % len(income_types)], 
                'balance_positive': True,
                'amount': None  # Will be set via random generation below if needed
            }

            balance_positive = (i % 3 == 0) and not isinstance(type_a.get('balance_positive', False), bool) or type_a['type'] in ['income']

            # Income transaction: positive
            if 'type' in type_a:
                self.transactions.append({
                    'type': income_types[i % len(income_types)], 
                    'amount': random.uniform(150, 250),
                    'date': f"2023-14-{i+1:02d}",
                    'source': "personal_allocation",
                    # Note: We don't explicitly set balance_positive here as it's a property of the type dict above
                })

            # Expense transaction: negative
            else:
                self.transactions.append({
                    'type': expense_types[i % len(expense_types)], 
                    'amount': random.uniform(-50, -150),
                    'date': f"2023-14-{i+1:02d}",
                    'source': "personal_allocation",
                })

        # Apply sample variance to balance based on portfolio composition and randomness
        base_balance = sum(1 for t in self.transactions if isinstance(t.get('type', None), str)) * 5
        
        # Add random fluctuation with a limit of +/-20% relative to the current total budget (scaled by 4000
