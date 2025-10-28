class User:

    def __init__(self, first, last, hair_color, sex, eye_color):
        self.first_name = first
        self.last_name = last
        self.hair_color = hair_color
        self.person_gender = sex
        self.eye_color = eye_color

    
    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}. My gender is {self.person_gender}, and he has {self.hair_color} hair, and {self.eye_color} eyes.")

    def greet_user(self):
        print(f"Hello there {self.first_name}.")

person  = User('Daniel', "Swanson", "brown", "Male", "green")

print (person.describe_user())
print (person.greet_user())


class User:

    def __init__(self, first, last, hair_color, sex, eye_color):
        self.first_name = first
        self.last_name = last
        self.hair_color = hair_color
        self.person_gender = sex
        self.eye_color = eye_color

    
    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}. My gender is {self.person_gender}, and he has {self.hair_color} hair, and {self.eye_color} eyes.")

    def greet_user(self):
        print(f"Hello there {self.first_name}.")

person  = User('Brandon', "Griffin", "gray", "Male", "blue")

print (person.describe_user())
print (person.greet_user())


class User:

    def __init__(self, first, last, hair_color, sex, eye_color):
        self.first_name = first
        self.last_name = last
        self.hair_color = hair_color
        self.person_gender = sex
        self.eye_color = eye_color

    
    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}. My gender is {self.person_gender}, and he has {self.hair_color} hair, and {self.eye_color} eyes.")

    def greet_user(self):
        print(f"Hello there {self.first_name}.")

person  = User('Aidan', "Smith", "brown", "Male", "blue")

print (person.describe_user())
print (person.greet_user())

'''
class Car:
  """A simple attempt to represent a car."""
  def __init__(self, make, model, year):
    """Initializing attributes to describe a car."""
    self.make = make
    self.model = model
    self.year = year
    self.odomoter_reading = 0
def get_descriptive_name(self):
  """Return a neatly formatted descriptive name."""
  long_name = f"{self.year} {self.make} {self.model}"
  return long_name.title()
def read_opometer(self):
  """Print a statement showing the car's mileage."""
  print(f"This car has {self.odomoter_reading} miles on it.")
def update_odometer(self, mileage):
  """Set the odometer reading to the given value."""
  """Reject the change if it attempts to roll the odometer back."""
  if mileage >= self.odometer_reading:
      self.odometer_reading = mileage
  else:
     print("You can't roll back an odometer!")
my_new_car = Car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())
my_new_car.update_odometer(23)
my_new_car.read_odomoter
''' 
























