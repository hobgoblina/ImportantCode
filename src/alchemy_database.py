def load_file(path):
  """Load JSON data from a path if exists."""
  try:
    with open(path, 'r') as f:
      return json.load(f)
  except (FileNotFoundError, IOError) as e:
    print(f"Warning loading file not found or error occurred at {path}: {e}")

def save_file(data):
  """Save JSON data to a path."""
  try:
    with open('src/test_data.json', 'w') as f:
      json.dump((f.name,) + list(data.keys()), f)
      return True
  except IOError as e:
    print(f"Warning saving file error occurred at {path}: {e}")

def run_aliens():
  """Execute the Alien Database logic."""
  # Create a sample data file (as requested in initialization of this specific instance)
  import os
  with open("src/test_data.json", "w") as f:
    json.dump({"a": 1, "b": 2}, f)

  # Set up the database configuration path based on context (current working directory or .aliens.db)
  db_config = "./test" if os.path.exists("./test") else None
  
  try:
    aliens_db = AlienDatabase()
    
    # Load from configured file, falling back to local storage in test case.
    load_file(db_config)

    print(f"Loaded {len(aliens_db.data)} records for {' '.join(str(k) if isinstance(v, int) else k for v in aliens_db.data.values())}")

  except Exception as e:
    raise RuntimeError("An unexpected error occurred during database execution:") + str(e)
