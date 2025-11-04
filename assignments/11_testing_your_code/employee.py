from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me the employee's first name: ")
    if first == 'q':
        break
    last = input("Please give me the employee's last name: ")
    if last == 'q':
        break
    salary = input("Please give me the employee's anual salary: ")
    if salary == 'q':
        break
    formatted_name = get_formatted_name(first, last, salary)
    print(f"\tNeatly formatted employee name: {formatted_name}.")