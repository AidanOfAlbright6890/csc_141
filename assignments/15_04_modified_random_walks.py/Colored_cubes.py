import matplotlib.pyplot as plt
x_values = range(5, 5000)
y_values = [x**2 for x in x_values]
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
ax.plot(x_values, y_values, s=10)
ax.plot(x_values, y_values, color='red', s=10)
# Set chart title and label axes.
ax.axis([0, 5000, 0, 5_500_000])
ax.ticklabel_format(style='plain')
plt.show()



    

import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
# Make a random walk.
    rw = RandomWalk()
    rw.fill_walk()
# Plot the points in the walk.
plt.style.use('classic')
fig, ax = plt.subplots()
point_numbers = range(rw.num_points)
ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
ax.scatter(rw.x_values, rw.y_values, s=15)
ax.set_aspect('equal')
# Emphasize the first and last points.
ax.scatter(0, 0, c='green', edgecolors='none', s=100)
ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
plt.show()






















































