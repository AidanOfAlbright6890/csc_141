from name_function import get_formatted_name
print("Enter 'q' at any time to quit.")
while True:
    city = input("\nPlease give me a city name: ")
    if city == 'q':
        break
    country = input("Please give me a country name: ")
    if country == 'q':
        break
    population = input("Please tell me the population of your location: ")
    if population == 'q':
        break
    formatted_name = get_formatted_name(city, country, population)
    print(f"\tNeatly formatted name: {formatted_name}.")
    