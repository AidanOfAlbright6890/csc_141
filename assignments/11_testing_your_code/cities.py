from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me the first city's name: ")
    if first == 'q':
        break
    last = input("Please give me the last city's name: ")
    if last == 'q':
        break
    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted employee name: {formatted_name}.")