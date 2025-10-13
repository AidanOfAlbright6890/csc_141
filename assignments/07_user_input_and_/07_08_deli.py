# Start with sandwiches that have been ordered,
# and an empty list to hold finished sandwiches.
sandwich_orders = ['pb&j', 'Cheesesteak', 'Breakfast sandwich']
finished_sandwiches = []
# Verify each sandwich until there are no more ordered sandwiches.
# Move each verified sandwich into the list of finished sandwiches.
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Verifying sandwich: {sandwich.title()}")
    finished_sandwiches.append(sandwich)
# Display all finished sandwiches.
print("\nThe following sandwiches have been finished.:")
for finished_sandwich in finished_sandwiches:
    print(f"{finished_sandwich} has been made.")
    print("finished_sandwiches = ['pb&j', 'Cheesesteak', 'Breakfast sandwich']")




























































































































