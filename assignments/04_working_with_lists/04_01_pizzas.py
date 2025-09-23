"Looping Through an Entire List"
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
        print(magician)

cats = ['kittens', 'lions', 'tigers']
for cat in cats:
        print(cat)

dogs = ['puppies', 'canine', 'wolves' ]
for dog in dogs:
        print(dog)


"A Closer Look at Looping"
for magician in magicians:
        print(magician)
        for magician in magicians:
                print(magician)


for cat in cats:
        print(cat)
        for cat in cats:
              print(cat)

for dog in dogs:
        print(dog)
        for dog in dogs:
             print(dog)


"Doing More Work Within a for Loop"
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")

"Doing Something After a for Loop"
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
        print(f"{magician.title()}, that was a great trick!")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")
        print("Thank you, everyone. That was a great magic show!")

        "Avoiding Indentation Errors"

        "Forgetting to Indent"
        magicians = ['alice', 'david', 'carolina']
        for magician in magicians:
                print(magician)
        "The print message was originally further to the left. However, that caused an error, because the print always has to be indented in a loop."

        "Forgetting to Indent Additional Lines"
        magicians = ['alice', 'david', 'carolina']
        for magician in magicians:
                print(f"{magician.title()}, that was a great trick")
        print(f"I can't wait to see your next trick, {magician.title()}.\n")
        
        magicians = ['alice', 'david', 'carolina']
        for magician in magicians:
                print(f"{magician.title()}, that was a great trick")
                print(f"I can't wait to see your next trick, {magician.title()}.\n")



"Indenting Unnecessarily"
message = "Hello Python world!"
print(message)
print("indenting will not work one prints, that goes for loops only.")



"Indenting Unnecessarily After the Loop"
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
              print(f"{magician.title()}, that was a great trick!")
              print(f"I can't wait to see your next trick, {magician.title()}.\n")
              print("Thank you everyone, that was a great magic show!")


"Forgetting the Colon"
magicians = [ 'alice', 'david', 'carolina']
for magician in magicians:
        print(magician)


print("pizzas")
pizzas = ["veggie", "cheeseburger", "Buffalo Chicken"]
for pizza in pizzas:
        print(pizza)
        print("pizza is delicious.")
        print(f"{pizza.title()}, is one of the best flavors of pizza ever!")










