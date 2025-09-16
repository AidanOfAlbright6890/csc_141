print("Every Function")
print("making a list")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities[0])
print(Cities[1])
print(Cities[2])
print(Cities[3])
print("Accessing Elements in a list")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities[1])
print(Cities[0].title())

"Index Position Start at 0, Not 1"
print(Cities[-1])

"Using individual Values from a List"
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
message = f"One of my favorite cities is {Cities[3].title()}."
print(message)

message = ("London is a very old city")
print(message)

print (Cities[1].lower())

Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities[-1])

"Inserting Elements into a List"
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
Cities.insert(0, 'Rome')
print(Cities)

"Appending Elements to the End of a List"
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
Cities.append('Reading')
print(Cities)

Cities = []
Cities.append('honda')
Cities.append('yamaha')
Cities.append('suzuki')
print(Cities)

"Removing Elements from a List"
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
del Cities[0]
print(Cities)

"Removing an Item Using the pop() Method"
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Favorite_City = Cities.pop(3)
print(f"The city that I would love to visit the most is {Favorite_City.title()}.")

"Removing an Item by Value"
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Cities.remove('London')
print(Cities)

Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Least_interested = 'London'
Cities.remove(Least_interested)
print(Cities)
print(f"\n {Least_interested.title()} is the City I am least interested out of the 4 I have chosen.")


