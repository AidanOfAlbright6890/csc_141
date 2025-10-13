# Make some input

prompt = "How old are you for dating age range?"

age = input (prompt) 

age = int(age)

min_age = int(age/2 + 7)

prompt = "What's your name?"
name = input (prompt)

print(f"{name}, You can date someone who is {min_age} years old.")


message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

#("answer = "answer= input ("Pick a number:") if answer == 'quit': " break")




prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")


height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")


number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

even_odd = input ("Pick a number:")
even_odd = int(even_odd)
yes_or_no = even_odd % 2
if yes_or_no == 0:
    print ("It's even")
else:
    print ("It's odd")


car = input("What kind of rental car would you like?")
print(f"\nLet me see if I can find you a {car}.a")





















































































































































