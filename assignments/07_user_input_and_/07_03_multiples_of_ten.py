answer = input ("Pick a number:")
yes_or_no = int(answer) % 10
if yes_or_no == 0:
    print ("It's a multiple of 10")
else:
    print ("It's not.")


current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


while True:

    answer = input ("Enter the name of your city:")
    if answer == 'quit':
     break
    if answer == 'Reading':
        print("It's a fine place.")
    else:
        print ("Avoid at at all cost!")


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)


prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")

    
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)


x = 1
while x <= 5:
    print(x)
    x += 1
"# This loop runs forever!"
"x = 1"
"while x <= 5:"
"print(x)"































































































