def get_formatted_parameter(city, country=''):
    """Generate a neatly formatted full name."""
    if city:
        full_name = f"{city} {country}"
    else:
        full_name = f"{city} {country}"
    return full_name.title()