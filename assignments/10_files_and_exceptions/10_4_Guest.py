
from hello_guest import Guest
guest = Guest('Aidan', 'Smith')
print(f"Hello guest, please tell me your name.")
print(f"My name is {guest.first_name} {guest.last_name}.")
print(f"Hello {guest.first_name} {guest.last_name}, welcome to my home")
guest.meet_guest()
guest.describe_guest()
guest.greet_guest()