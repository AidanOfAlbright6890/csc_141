"Animals"
dinosaur_descendants = ["Birds", "Crocodiles", "Lizards"]
for dinosaur_descendant in dinosaur_descendants:
    print(dinosaur_descendant)
    print("are related to dinosaurs.")
    print(f"{dinosaur_descendant.title()}, are among one of many animals to descend from dinosaurs.")


"Making Numerical Lists"
"Using the range() Function"
for value in range(1, 5):
    print(value)
for value in range(1, 6):
    print(value)

"Using range() to Make a List of Numbers"
numbers = list(range(1, 6))
print(numbers)


even_numbers = list(range(2, 11, 2))
print(even_numbers)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
    print(squares)


squares = []
for value in range(1, 11):
    squares.append(value**2)
    print(squares)


"Simple Statistics with a List of Numbers"
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(digits)
min(digits)
print(min(digits))
max(digits)
print(max(digits))
sum(digits)
print(sum(digits))


"List Comprehensions"
squares = [value**2 for value in range(1, 11)]
print(squares)








