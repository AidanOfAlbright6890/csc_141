import Ice_cream
Ice_cream.describe_stand('welcome to my ice cream stand.')
Ice_cream.describe_flavors('I serve vanilla, chocolate and strawberry.')

from Ice_cream import describe_flavors as df
df('I serve vanilla, chocolate and stawberry.')


