def sanitize_text(value, default=""):
    if value is None:
        return default
    return str(value).strip()
