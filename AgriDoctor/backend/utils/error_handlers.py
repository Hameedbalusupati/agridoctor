def safe_error_message(message, fallback="Request failed."):
    return message if message else fallback
