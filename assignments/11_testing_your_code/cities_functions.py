def get_formatted_name(first, second, last=''):
    """Generate a neatly formatted full name."""
    if second:
        full_formatted_name = f"{first}, {second} and {last}"
    else:
        full_formatted_name = f"{first}, {second} and {last}"
    return full_formatted_name.title()