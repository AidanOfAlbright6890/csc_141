snake = 'python'
message =("Is snake == 'python'? I predict True.")
print(message)
message =(snake == 'python')
print(message)
message =("\nIs snake == 'kobra'? I predict False.")
print(message)
message =(snake == 'kobra')
print(message)


Fish = 'Goldfish'
print("Is Fish == 'Goldfish'? I predict true.")
print(Fish == 'Goldfish')
print(Fish.lower())

print("\nIs Fish == 'Tuna'? I predict False.")
print(Fish == 'Tuna')
print('Tuna'.lower())

sandwich_condiment = 'hot  sauce'
if sandwich_condiment != 'mayonnaise':
    print("No mayonnaise please.")

banned_users = ['Jackson', 'Caleb', 'Brandon']
user = 'Max'
if user not in banned_users:
    print(f"{user.title()}, You're up next.")



age = 19
if age >= 18:
    print("You are old enough to vote!")

age = 19
if age >=18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.")

requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")



requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")











