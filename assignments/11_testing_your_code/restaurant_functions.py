def get_formatted_restaurant(first, last, middle, salary=''):
    """Generate a neatly formatted full name."""
    if middle:
        full_formatted_restaurant = f"{first} {middle} {last} {salary}"
    else:
        full_formatted_restaurant = f"{first} {last} {salary}"
    return full_formatted_restaurant.title()