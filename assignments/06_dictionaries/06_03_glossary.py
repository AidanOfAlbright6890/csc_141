programming_words = {'comments': 'deny the computer from reading a code selected as a comment.', 'message': 'sends a message for the computer to print.', 'List': 'a group of words listed together inbetween 2 braces.', 'Slice': 'method used to show only a portion of items from a list.', 'Integer': 'a subject used to name a list.'}

word = programming_words['comments']
print(f"Comments {word}")

word = programming_words['message']
print(f"A message {word}")

word = programming_words['List']
print(F"A list is {word}")

word = programming_words['Slice']
print(F"Slice is a {word}")

word = programming_words['Integer']
print(F"An integer is {word}")

user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi',}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python',}
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python',}
for name in favorite_languages.keys():
    print(name.title())

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python',}
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}, {language}!")

if name in friends:
    language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")
if 'erin' not in favorite_languages.keys():
        print("Erin, please take our poll!")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python',}
for name in sorted(favorite_languages.keys()):
     print(f"{name.title()}, thank you for taking the poll.")

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python',}
print("The following languages have been mentioned:")
for language in favorite_languages.values():
     print(language.title())

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
     print(language.title())

































































































































































































