class Dog:
    '''A simple attempt to model a dog.'''

    def __init__(self, name, age):
        '''Initializing name and age attributes.'''
        self.name = name
        self.age = age
     
    def sit(self):
        '''Simulate dog sitting'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''Simulate rolling over'''
        print(f"{self.name} rolled over!")


# Main Program
my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
my_dog.roll_over()


class Resteraunt:

    def __init__(self, resteraunt_name, cuisine_type):
        self.resteraunt_name = resteraunt_name
        self.cusine_type = cuisine_type
    
    def describe_resteraunt(self):
        print(f"The resteraunt is called {self.resteraunt_name} and serves {self.cusine_type}.")

    def open_resteraunt(self):
            print(f"The resteraunt is open.")

        
resteraunt = Resteraunt('Austins', 'All american food')

print(f"The restaurant's name is {resteraunt.resteraunt_name}")
resteraunt.open_resteraunt()
resteraunt.describe_resteraunt()






        









