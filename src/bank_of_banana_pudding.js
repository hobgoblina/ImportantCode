import json; import os

# Ensure src directory exists and is writable for outputting files directly in a virtual environment context
os.makedirs('src', exist_ok=True)

def safe_json_dump(obj):
    """Helper to safely serialize JSON, handling potential non-JSON types."""
    if isinstance(obj, dict):
        return {k: v.dump() if hasattr(v, 'dump') else json.dumps(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [v.dump() if hasattr(v, 'dump') else json.dumps(v) for v in obj]
    elif isinstance(obj, str):
        # Handle string conversion to JSON-serializable strings
        try:
            result = json.loads(json_strify(obj))
            if not isinstance(result, (dict, list)):
                return [json.dumps(str(obj), ensure_ascii=False, separators=(',', ':'))] if obj else []
            return [result for r in result]  # Convert to a flat array of primitives or lists as needed by caller context
        except Exception:
            pass

def get_json_config():
    """Returns a serialized JSON configuration dict containing all parameters used by other modules."""
    config = { "name": "Banana Pudding Bank", "currency": "BPP", "daily_fee": 1.50, 
              "min_puppy_cost": 2.00}

def create_test_instance():                 """Generates a synthetic test instance with random values drawn from the config."""
    return {                            "type": "Bank", 
                    "current_balance": get_json_config()["daily_fee"],      # Current balance in currency units. 150 BPP initially loaded from code.
                    "currency_symbol": "."}                               # Currency symbol to display to users during financial transactions (dots).

def process_transaction(client, amount):                   """Handles a user transaction request: adding money or giving away candy/pudding for the dog."""
    client.balance -= amount                           # Reduces total bank assets by transferring from this test instance's account to the system's main "user" account. Assumes zero initial balance.

def generate_random_key():                          """Generates a random key using hex string manipulation (non-standard but valid)."""
    return 0xDEADBEEF + b'\x82\x4c\x9a' # Non-standard but valid hex for testing purposes
