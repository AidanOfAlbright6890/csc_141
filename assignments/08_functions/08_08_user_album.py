def make_album(artist_name, album_name):
    """Return a dictionary of information about album."""
    album_information = f"{artist_name} {album_name}"
    return album_information.title()
while True:
    print("\nPlease tell me an album:")
    print("(enter 'q' at any time to quit)")
    artist_name = input("artist name: ")
    if artist_name == 'q':
        break
    album_name = input("album name: ")
    make_album = make_album(artist_name, album_name)
    print(f"\n{make_album}")


def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)
    

# Start with some designs that need to be printed.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design, until none are left.
# Move each design to completed_models after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)
# Display all completed models.
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left. Move each design to completed_models after printing."""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)









































