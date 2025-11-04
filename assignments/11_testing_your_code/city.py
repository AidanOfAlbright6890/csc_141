from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city name: ")
    if city == 'q':
        break
    country = input("Please give me a country name: ")
    if country == 'q':
        break
    formatted_name = get_formatted_name(city, country)
    print(f"\tNeatly formatted name: {formatted_name}.")