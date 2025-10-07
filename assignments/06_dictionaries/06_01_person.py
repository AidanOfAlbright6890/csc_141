# Start dictionary

alien_0 = {'color': 'green', 'points' : 5}
print(alien_0['color'])
print(alien_0['points'])

alien_0 = {'color': 'green'}
print(alien_0['color'])

alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python',}

favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'rust', 'phil': 'python',}
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

"alien_0 = {'color': 'green', 'speed': 'slow'} print(alien_0['points'])"
"The code above causes an error. Therefor, it won't be used."

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

person_0 = {'first_name': 'Martin', 'last_name': 'Smith'}
print(person_0['first_name'])
print(person_0['last_name'])


person_0 = {'first_name': 'Martin', 'last_name': 'Smith'}
person_0 = {'Martin': 'Smith'}

person_0 = {'first_name': 'Martin'}
print(person_0['first_name'])

person_0 = {'first_name': 'Martin', 'last_name': 'Smith', 'city': 'Reading', 'age': 50}
city = person_0['city']
age = person_0['age']
print(f"Martin Smith is {age} years old and lives in the the city of {city}, Pennsylvania.")




























































































