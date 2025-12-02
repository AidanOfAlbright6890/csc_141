import plotly.express as px

from die import Die

# Create a D8.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of RollingOne D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.show()

print(frequencies)

# When I rolled, I thought that 8 would be the highest 3 would be the lowest. Instead, 1 was the highest and 4 was the lowest.