def explore(obj, prefix=""):
    """Print the shape of a nested dict/list structure for quick inspection."""
    if isinstance(obj, dict):
        for k, v in obj.items():
            print(f"{prefix}{k}: {type(v).__name__}")
            explore(v, prefix + "  ")
    elif isinstance(obj, list) and obj:
        print(f"{prefix}[list of {len(obj)}] -> sample fields:")
        explore(obj[0], prefix + "  ")