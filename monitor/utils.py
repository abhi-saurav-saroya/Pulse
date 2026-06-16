def format_bytes(num_bytes: float) -> float:
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if num_bytes < 1024:
            return f"{num_bytes:.2f} {unit}"

        num_bytes /= 1024