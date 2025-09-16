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

print("Index Position Start at 0, Not 1")
print(Cities[-1])

print("Using individual Values from a List")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
message = f"One of my favorite cities is {Cities[3].title()}."
print(message)

message = ("London is a very old city")
print(message)

print (Cities[1].lower())



print("Removing an Item by Value")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Cities.remove('London')
print(Cities)

print("Appending Elements to the End of a List")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Cities.append("San Diego")
print(Cities)
Cities = []
Cities.append('Philadelphia')
Cities.append('London')
Cities.append('New York City')
Cities.append('Tokyo')
print(Cities)

("Popping items")
Favorite_City = Cities.pop(3)
print(f"My favorite city in the world is {Favorite_City.title()}.")

Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Cities[1] = 'Rome'
print(Cities)

("Inserting items")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
Cities.insert(0, 'Reading')
Cities.insert(1, 'Lancaster')
Cities.insert(2, 'Indianapolis')
Cities.insert(3, 'Miami')
print(Cities)


print("Sorting Lists")
print("Original order")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
print("Reverse order")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Cities.reverse()
print(Cities)
print("Alphebetical order")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(sorted(Cities))
print("Reverse-Alphebetical order")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
Cities.sort(reverse=True)
print(Cities)

print("Number of Cities")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(len(Cities))

print("Deleting")
Cities = ['Philadelphia', 'London', 'New York City', 'Tokyo']
print(Cities)
del Cities[1]
print(Cities)


