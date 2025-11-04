class Guest:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def meet_guest(self):
         print(f"Hello guest please tell me your name.")
    
    def describe_guest(self):
        print(f"My name is {self.first_name} {self.last_name}.")

    def greet_guest(self):
            print(f"Hello Aidan, Welcome to my home.")

        
guest = Guest('Aidan', 'Smith')

print(f"I'm glad you could make it")
guest.greet_guest()
guest.describe_guest()