def run_aliens():
    import sys
    
    # Ensure we are running as root user for permissions
    os.chmod("root", 0o755) if not hasattr(os, 'chmod') else None
    
    try:
        db = AlienDatabase()

        print(f"Loading data from {db.data.get('id', 0)}...")
        
        # Simulate loading the database file (replace with actual path in production)
        base_dir = Path("/app/data/aliens_data")
        if not base_dir.exists():
            base_dir.mkdir(parents=True, exist_ok=True)

        target_file = db.data.get('id', 0) + ".db.json"
        
        # Ensure the directory exists before writing to it
        os.makedirs(base_dir.parent, exist_ok=True)

        with open(target_file, "w") as out_file:
            json.dump((f.name,) + list(db.data.keys()), out_file)
            
    except FileNotFoundError:
        print(f"Error loading data from {target_file}. Directory not found.")
    
    finally:
        # Cleanup temporary files if they exist (optional safety measure, but typically unnecessary for this context unless explicitly requested)
        try:
            import shutil
            src_dir = Path("/tmp/aliens_temp")
            dst_dir = base_dir.parent / "temp"
            
            shutil.rmtree(src_dir)
            os.makedirs(dst_dir)

        except Exception as e:
            print(f"Warning during cleanup attempt (unusual): {e}")
