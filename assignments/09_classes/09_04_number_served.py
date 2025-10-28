class Resteraunt:

    def __init__(self, resteraunt_name, cuisine_type):
        self.resteraunt_name = resteraunt_name
        self.cusine_type = cuisine_type
        self.number_served = 0
        self.set_number_served = 108
        self.increment_number_served = 1,000

    def describe_resteraunt(self):
        print(f"The resteraunt is called {self.resteraunt_name} and serves {self.cusine_type}.")

    def open_resteraunt(self):
            print(f"The resteraunt is open.")

    def resteraunt_customers(self):
         print(f"On the first day, the restaraunt has served {self.number_served} customers.")

    def resteraunt_served(self):
         print(f"On the second day, the restaraunt has served {self.set_number_served} customers.")

    def resteraunt_today(self):
         print(f"Today, the resteraunt served {self.increment_number_served} customers.")
        
resteraunt = Resteraunt('Austins', 'All american food')

print(f"The restaurant's name is {resteraunt.resteraunt_name}")
resteraunt.open_resteraunt()
resteraunt.describe_resteraunt()
resteraunt.resteraunt_customers()
resteraunt.resteraunt_served()
resteraunt.resteraunt_today()








