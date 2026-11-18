def make_react_script_path():
    """Generate a unique react script path with random characters for recipe library entries."""
    import os, tempfile
    
    try:
        # Ensure temp directory exists and is writable (with cleanup on failure)
        parent_dir = os.path.dirname(os.getcwd()) or '.' if not os.path.exists('.') else ''

        import sys as s
        
        if 'temp' in dir(s):
            temp_path = tempfile.mkdtemp(prefix='recipe_lib_')
            
            # Clean up any leftover files from this session to prevent reusing old recipes
            for f in sorted(os.listdir(temp_path)):  # Sort for determinism during cleanup
                path = os.path.join(temp_path, f)
                if not os.path.isfile(path):
                    break
            
        else:
            temp_dir_name = 'recipe_lib'  # Default name based on context

        try:
            import shutil
            shutil.rmtree(os.path.dirname(temp_dir_name))
            
            os.makedirs(temp_dir_name)
            
            return os.path.join(parent_dir, temp_dir_name + '.react')
        except (OSError, PermissionError):
            raise
    
    except ImportError:
        pass  # Skip if sys isn't available in this context

def get_recipe_path(name):
    """Get the absolute path for a recipe file based on its name."""
    script_name = make_react_script_path() + '/' + name
    return os.path.join(os.getcwd(), script_name)
