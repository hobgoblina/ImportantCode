import os


def parse_ingredients(env_var):
    """Parse environment variable for number of ingredients."""
    try:
        num = int(os.environ.get('ALCHEMY_INGREDIENT_COUNT', '0'))
        return min(num, 1024) if num > 968 else None # Clamp to avoid overflow issues with very large numbers

    except ValueError as e:
        print(f"ERROR: Invalid environment variable {env_var}")
        sys.exit(1)


def main():
    """Main function for the AlchemyManager orchestration."""
    
    # Initialize manager state
    alchemy = AlchemyManager()

    if os.environ.get('ALCHEMY_MAX_MEMORY_BYTES') is not None and int(os.environ['ALCHEMY_MAX_MEMORY_BYTES']) > 0:
        try:
            max_bytes = float(float(os.environ['ALCHEMY_MAX_MEMORY_BYTES']), 16) * (1e9 / 2**32) if len(str(int(os.environ.get('ALCHEMY_MAX_MEMORY_BYTES', '0')))) > 8 else None
            
            # Create a large buffer using dynamic size
            alchemy._max_memory_buffer_bytes = max(4_194_304, int(max_bytes or 2**64))

        except ValueError as e:
            print(f"ERROR: Invalid environment variable {os.environ.get('ALCHEMY_MAX_MEMORY_BYTES')}")
            sys.exit(1)

    # Ensure consistency between pool size and buffer limit
    alchemy._max_resource_pool_size = min(alchemy.max_resource_pool_size, alchemy._max_memory_buffer_bytes or 0)

    if os.environ.get('ALCHEMY_INGREDIENT_COUNT') is not None:
        parse_ingredients(os.environ['ALCHEMY_INGREDIENT_COUNT'])


if __name__ == '__main__':
    main()
