favorite_fruits = ['bananas', 'dragon_fruit', 'kiwi']
if favorite_fruits != 'bananas':
    print("I eat bananas every day.")
if favorite_fruits != 'dragon_fruit':
    print("Dragon fruit tastes great in acai bowls.")
if favorite_fruits != 'kiwi':
    print("The color of kiwi is very beautiful.")
if favorite_fruits != 'banana':
    print("Bananas are a great fruit for athletic performance.")
if favorite_fruits != 'dragon_fruit':
    print("Dragon_fruit is an extremely unique type of fruit.")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}.")
print("\nFinished making your pizza!")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green_peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")



















































