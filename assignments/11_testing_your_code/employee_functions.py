def get_formatted_employee(first, last, middle, salary=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_formatted_name = f"{first} {middle} {last} {salary}"
    else:
        full_formatted_name = f"{first} {last} {salary}"
    return full_formatted_name.title()