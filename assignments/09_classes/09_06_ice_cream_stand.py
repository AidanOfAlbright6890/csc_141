class IceCreamStand:

    def __init__(self, Ice_Cream_Stand, Ice_Cream_Flavors):
        self.Ice_Cream_Stand = Ice_Cream_Stand
        self.Ice_Cream_Flavors = Ice_Cream_Flavors
    
    def describe_stand(self):
        print(f"My {self.Ice_Cream_Stand} sells the following flavors, {self.Ice_Cream_Flavors}.")

    def describe_flavors(self):
            print(f"Welcome to my {self.Ice_Cream_Stand}.")

        
icecream = IceCreamStand('Ice Cream Stand', 'Vanilla, Chocolate and Stawberry')

print(f"My {icecream.Ice_Cream_Stand} serves the following flavors, {icecream.Ice_Cream_Flavors}.")
icecream.describe_stand()
icecream.describe_flavors()













