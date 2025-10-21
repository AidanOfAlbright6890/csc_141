def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('Aidan', 'Smith', location='Reading', field='Computer Science', Occupation='College Student')
print(user_profile)













