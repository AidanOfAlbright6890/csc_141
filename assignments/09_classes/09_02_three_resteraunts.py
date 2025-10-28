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


class Resteraunt:
     def __init__(self, resteraunt_township, resteraunt_street, resteraunt_name):
          self.resteraunt_township = resteraunt_township
          self.resteraunt_street = resteraunt_street
          self.resteraunt_name = resteraunt_name
     def describe_resteraunt(self):
          print(f"{self.resteraunt_name} is a restaraunt in {self.resteraunt_township} on {self.resteraunt_street}.")


class Resteraunt:
     def __init__(self, entree_ribs, entree_chicken_tenders, resteraunt_name):
          self.entree_ribs = entree_ribs
          self.entree_chicken_tenders = entree_chicken_tenders
          self.resteraunt_name = resteraunt_name
     def describe_resteraunt(self):
          print(f"{self.resteraunt_name} is famous for its {self.entree_ribs} and {self.entree_chicken_tenders}.")


class Resteraunt:
     def __init__(self, position_cook, position_server, position_dishwasher, position_busboy, location_resteraunt):
          self.position_cook = position_dishwasher
          self.position_server = position_server
          self.position_dishwasher = position_dishwasher
          self.position_busboy = position_busboy
          self.location_resteraunt = location_resteraunt
     def describe_resteraunt(self):
          print(f"{self.location_resteraunt} offers the following jobs, {self.position_cook}, {self.position_server}, {self.position_dishwasher}, {self.position_busboy}, {self.location_resteraunt}.")










