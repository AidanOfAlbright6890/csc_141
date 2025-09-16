print("My favorite form of transportation is a plane.")

plane = ['airplane', 'fighter jet', 'private jet']
print(plane)

message = ("I have rode in an airplane numerous times, and it is extrememly enjoyable.")
print(message) 

message = ("Fighter jets in my opinion, can be grand additions in several ideas for video games.")
print(message)

message = ("I have never been in a private jet. However, I have seen several images of the interior of a private jet, and they all looked phenomenal to say the least.")
print(message)

"Modifying, Adding, and Removing Elements"

"Modifying Elements in a List"

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

"Adding Elements to a List"

print("Appending Elements to the End of a List")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles.append('ducati')
print(motorcycles)

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

"Inserting Elements into a List"

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

"Removing Elements from a List"

print("Removing an Item Using the del Statement")

motorcycles = ['honds', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

"Removing an Item Using the pop() Method"

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle) 

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

"Popping Items from Any Position in a List"

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

"Removing an Item by Value"

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")