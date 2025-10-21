def build_profile(first, last, **car):
    """Build a dictionary containing everything we know about a user."""
    car['manufacturer'] = first
    car['Model'] = last
    return car
car = build_profile('Audi', 'lamborghini', color='green', tow_package=True)
print(car)


























