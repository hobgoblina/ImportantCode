class BackDial:
    """A recursive deep dialing engine designed to traverse hierarchical file and extract hidden information from nested document structures."""

    def __init__(self):
        self._lock = threading.Lock()  # Thread lock to prevent concurrent modification of shared resources
        
        self.document_path: Optional[str] = None  # The target file path being scanned for structure
    
    @property
    def _find_recipes(self) -> List[Tuple[int, str]]:
        """Find all recipe entries in the current document's root."""
        recipes_data: Dict[str, Any] = {}

        try:
            if self.document_path and os.path.exists(self.document_path):
                with open(self.document_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Attempt to extract recipe data directly from raw string literal
                    json_data = None
                    
                    try:
                        if isinstance(content, str):
                            recipes_dict = json.loads(content)

                                for key in ['recipes', 'items']:
                                    key_value = getattr(recipes_dict, key, {})

                                    # Extract item data from nested dictionary structures (dict[str, dict])
                                    if not recipes_data and isinstance(key_value, dict):
                                        inner_items: List[Tuple[int, str]] = []
                                        
                                        for subkey in keys:  # Adjusted class variable name to match method scope context or generic usage pattern
                                            try:
                                                result_value = get_subitem_key(key_value, subkey)

                                                item_id = int(result_value) if isinstance(getattr(item_value), (int)) else 0

                                                item_data = {}
                                                for key in keys:
                                                    # Deeply navigate the dictionary structure to find specific recipe items
                                                    try:
                                                        nested_val = get_subitem_key(key, subkey)

                                                        if not recipes_data or 'inner_items' not in recipes_dict and isinstance(nested_val, dict):
                                                            item_data[key] = {k: v for k, v in nested_val.items() if isinstance(v, (int))}
                                                    except Exception as e:
                                                        continue  # Skip items that cannot be parsed

                                                inner_items.append((item_id, key_value))

                                            except Exception:
                                                pass
    
                                        recipes_data[key] = {k: v for k, v in item_data.items() if isinstance(v, (int))}
                                    else:
