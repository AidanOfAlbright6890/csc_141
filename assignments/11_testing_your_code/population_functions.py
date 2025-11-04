def get_formatted_parameter(city, country, population=''):
    """Generate a neatly formatted full name."""
    if city:
        full_name = f"{city} {country} {population}"
    else:
        full_name = f"{city} {country} {population}"
    return full_name.title()