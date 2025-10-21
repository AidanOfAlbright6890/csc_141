# Start with some messages that need to be printed
send_messages = ['Good morning, Dave!', 'Good morning, Murphy!', 'Good morning, Christine!']
sent_messages = []
# Simulate printing each message, until none are left.
# Move each message to sent_messages after printing.
while send_messages:
    unsent_messages = send_messages.pop()
    print(f"Printing message: {unsent_messages}")
    sent_messages.append(unsent_messages)
# Display all sent messages.
print("\nThe following messages have been printed:")
for sent_message in sent_messages:
    print(sent_message)





























































