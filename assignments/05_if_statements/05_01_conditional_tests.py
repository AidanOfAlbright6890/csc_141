# Make the cars.py demo
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())

    else:
        print(car.title())

"Checking for Equality"

car = 'bmw'
car == 'bmw'

"Checking for Inequality"

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

"Numerical Comparisons"
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

"Checking Whether a Value Is Not in a List"
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

"Conditional Tests"
Jedi = 'Darth Vader'
print("Is Jedi == 'Darth Vader'? I predict True.")
print(Jedi == 'Darth Vader')

print("\nIs Jedi == 'Yoda'? I predict False.")
print(Jedi == 'Yoda')

Ice_Cream = 'Vanilla'
print("is Ice_Cream == 'Vanilla'? I predict True.")
print(Ice_Cream == 'Vanilla')

print("\nIs Ice_Cream == 'Chocolate'? I predict False.")
print(Ice_Cream == 'Chocolate')

Holidays = 'Halloween'
print("is Holidays == 'Halloween'? I predict True.")
print(Holidays == 'Halloween')

print("\nIs Holidays == 'Christmas'? I predict False.")
print(Holidays == 'Christmas')

seasons = 'spring'
print("is seasons == 'spring'? I predict True.")
print(seasons == 'spring')

print("\nIs seasons == 'fall'? I predict False.")
print(Holidays == 'fall')

soda = 'coke'
print("is soda == 'coke'? I predict True.")
print(soda == 'coke')

print("\nIs soda == 'pepsi'? I predict False.")
print(soda == 'pepsi')

print('The reason why 5 of the programs result as being true is because typing in "true" programmed the test to become true. the same applies for the test that end up being false.')







