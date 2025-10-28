class User:

    def __init__(self, first, last, hair_color, sex, eye_color):
        self.first_name = first
        self.last_name = last
        self.hair_color = hair_color
        self.person_gender = sex
        self.eye_color = eye_color
        self.login_attempts = 1
        self.new_login_attempts = 0

    
    def describe_user(self):
        print(f"My name is {self.first_name} {self.last_name}. My gender is {self.person_gender}, and he has {self.hair_color} hair, and {self.eye_color} eyes.")

    def greet_user(self):
        print(f"Hello there {self.first_name}.")

    def attempt_login(self):
        print(f"{self.first_name} attempted to login {self.login_attempts} time.")

    def repeat_login(self):
        print(f"{self.first_name} attempted to login {self.new_login_attempts} times.")

person  = User('Daniel', "Swanson", "brown", "Male", "green")

print (person.describe_user())
print (person.greet_user())
print (person.attempt_login())
print (person.repeat_login())


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
    if mileage >= self.odometer_reading:
        self.odometer_reading = mileage
    else:
        print("You can't roll back an odometer!")

  def increment_odometer(self, miles):
    """Add the given amount to the odometer reading."""
    self.odometer_reading += miles


class Battery:
   """A simple attempt to a model a battery for an electric car."""
   def __init__(self, battery_size=40):
      """Initializing the battery's attributes."""
      self.battery_size = battery_size
   def describe_battery(self):
      """Print a statement describing the battery size."""
      print(f"This car has a {self.battery_size}-KWh battery.")
   def get_range(self):
      """Print a statement about the range this battery provides."""
      if self.battery_size == 40:
         range = 150
      elif self.battery_size == 65:
         range = 225
      print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
   def fill_gas_tank(self):
      """Electric cars don't have gas tanks."""
      print("This car doesn't have a gas tank!")
   """Represents aspects of a car, specific to electric vehicles."""
   def __init__(self, make, model, year):
      """Initialize attributes of the parent class. Then initialize attributes specific to an electric car."""
      super().__init__(make, model, year)
      self.battery = Battery()
      self.battery_size = 40
   def describe_battery(self):
      """Print a statement describing the battery size."""
      print(f"This car has a {self.battery_size}-KWh battery.")
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()














