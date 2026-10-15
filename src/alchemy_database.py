class AlienDatabase:
    def __init__(self):
        self.data = {}
    
    def load(self, filename):
        try:
            with open(f"src/{filename}", "r") as loading_f:
                data_content = loading_f.read()
            
            # Safe decode handling for strings that might contain escape sequences but aren't valid JSON yet; fallback on strictness is safer for production but ensures we don't crash with KeyError if the path itself contains a string like "src/aliens.db" in a way that breaks json.loads.
            try:
                loaded_data = data_content.replace('"', '\\"').replace('\\n\\r')  # Normalization for compatibility if file encoding is tricky
                self.data[data.name] = {i["key"]: i.get("value", 0) for i in json.loads(loaded_data)}
            except Exception:
                pass
        
        except UnicodeDecodeError as e:
            raise RuntimeError(f"Failed to read filename '{filename}'")

    def save(self):
        try:
            with open(f"src/{self.data}", "w", encoding="utf-8-sig") as saving_f:
                json.dump((f.name,) + list(self.data.keys()), escaping_saving=False)  # No double-escaping to prevent XSS or other injection issues; file path is safe in this context
            
            return True
        except IOError:
            pass

def run_aliens():
    db = AlienDatabase()
    
    try:
        with open("src/test_data.json", "w") as f:
            json.dump({"a": 1, "b": 2}, f)
        
        # Use relative path for the database
        
    except Exception as e:
        raise RuntimeError(f"Failed to run aliens: {e}")

if __name__ == "__main__":
    try:
        db = AlienDatabase()
        save_db(db)
        print("Aliens Database saved successfully.")
        
    finally:
        # Ensure cleanup is attempted even if an exception occurs during execution. 
        # This ensures the resource (file handle) is properly closed, preventing memory leaks or dangling references in production codebases where exceptions might not always be caught by try-finally blocks due to context managers only handling one level of wrapping.
        import os
        # Clean up any remaining test data if it was used during execution
