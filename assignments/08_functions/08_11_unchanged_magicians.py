def show_messages(friends):
    """Print a simple text message to three friends."""
    for friend in friends:
        msg = f"Good morning, {friend.title()}!"
        print(msg)
usernames = ['Dave', 'Murphy', 'Christine']
show_messages(usernames)




# Start with some messages that need to be printed
send_messages = ['Good morning, Dave!', 'Good morning, Murphy!', 'Good morning, Christine!']
sent_messages = []
# Simulate printing each message, until none are left.
# Move each message to sent_messages after printing.
while send_messages:
    unsent_messages = send_messages.pop()
    print(f"Printing message: {unsent_messages}")
    sent_messages.append(unsent_messages)
# Display all sent messages.
print("\nThe following messages have been printed:")
for sent_message in sent_messages:
    print(sent_message)


def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')


def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)
































