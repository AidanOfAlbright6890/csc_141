pizzas= ['pepperoni', 'ham', 'onions', 'sausage']
for pizza in pizzas:
    if pizza == 'onions':
        print(pizza.upper())
    else:
        print(pizza.title())

prompt = "\nPlease enter the topping for your pizza:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


prompt = "\nPlease enter the topping for your pizza:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"For my pizza, may I please have {topping.title()}?")











































































































































































