class User:

    def __init__(self, name, privilege1, privilege2, privilege3, privilege4, privilege5):
        self.Admin_name = name
        self.first_privilege = privilege1
        self.second_privilege = privilege2
        self.third_privilege = privilege3
        self.fourth_privilege = privilege4
        self.fifth_privilege = privilege5

    
    def describe_user(self):
        print(f"My name is {self.Admin_name}. As an admin, my privilages are {self.first_privilege}, {self.second_privilege}, {self.third_privilege}, {self.fourth_privilege} and {self.fifth_privilege}.")

    def greet_user(self):
        print(f"My name is {self.first_name}.")

privileges  = User('Daniel', "permission to make new rules", "host events", "decide when events happen", "shout people out", "and invite users")

print (privileges.describe_user())
print (privileges.greet_user())


class Privilege:

    def __init__(self, privilege1, privilege2, privilege3, privilege4, privilege5):
        self.first_privilege = privilege1
        self.second_privilege = privilege2
        self.third_privilege = privilege3
        self.fourth_privilege = privilege4
        self.fifth_privilege = privilege5

    
    def describe_privileges(self):
        print(f"My privileges are {self.first_privilege}, {self.second_privilege}, {self.third_privilege}, {self.fourth_privilege} and {self.fifth_privilege}.")

    def mention_privileges(self):
        print(f"These are my privileges.")

privileges  = Privilege("permission to make new rules", "host events", "decide when events happen", "shout people out", "and invite users")

print (privileges.describe_privileges())
print (privileges.mention_privileges())