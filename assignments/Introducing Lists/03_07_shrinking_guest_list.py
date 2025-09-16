"Shrinking Guest List"
Guests_for_Dinner = ['David Kaul', 'John Pankratz', 'Mark Baldridge']
Guests_for_Dinner.insert(0, 'Jean Paul')
Guests_for_Dinner.insert(1, 'Sapphire')
Guests_for_Dinner.insert(2, 'Austin')
print(Guests_for_Dinner)
print("David Kaul, I invite you to dinner.")
print("John Pankratz, I invite you to dinner.")
print("Mark Baldridge, I invite you to dinner.")
print("Jean Paul, I invite you to dinner.")
print("Sapphire, I invite you to dinner.")
print("Austin, I invite you to dinner.")
print("Dear guests, I am terribly sorry, but I will only be able to invite two people over for dinner.")

first_guest = Guests_for_Dinner.pop(0)
print(f"I'm sorry I couldn't invite you to dinner {first_guest.title()}.")
second_guest = Guests_for_Dinner.pop(1)
print(f"I'm sorry I couldn't invite you to dinner {second_guest.title()}.")
third_guest = Guests_for_Dinner.pop(3)
print(f"I'm sorry I couldn't invite you to dinner {third_guest.title()}.")
fourth_guest = Guests_for_Dinner.pop(0)
print(f"I'm sorry I couldn't invite you to dinner {fourth_guest.title()}.")
first_guest = Guests_for_Dinner.pop(0)
print(f"You are invited to dinner {first_guest.title()}.")
second_guest = Guests_for_Dinner.pop(0)
print(f"You are invited to dinner {second_guest.title()}.")

Guests_for_Dinner = ['David Kaul', 'John Pankratz']
print(Guests_for_Dinner)
del Guests_for_Dinner[0]
print(Guests_for_Dinner)


Guests_for_Dinner = ['David Kaul', 'John Pankratz']
print(Guests_for_Dinner)

del Guests_for_Dinner[0]
print(Guests_for_Dinner)

Guests_for_Dinner = ['David Kaul', 'John Pankratz']
print(Guests_for_Dinner)

"Sorting a List Permanently with the sort() Method"
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

print("Sorting a List Temporarily with the sorted() Function")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

"Printing a List in Reverse Order"
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

"Finding the Length of a List"
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
"Since there are four items in the list of cars, the answer 4"



