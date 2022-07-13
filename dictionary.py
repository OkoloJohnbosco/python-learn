alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])


new_points = alien_0['points']
# print(f"You just earned {new_points} points!")


# alien_0['x_position'] = 0
# alien_0['y_position'] = 25

# print(alien_0.copy())

# del alien_0['points']
# # print(alien_0.copy())
# print(alien_0.items())

# point_value = alien_0.get('points', "No point returned for this key")
# # print(point_value)

# favorite_languages = {
#     "john": "Javascript",
#     "odi": "Dart",
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
# }

# print(favorite_languages['john'])

# people = ['jen', "john", "odi"]

# for person in people:
#     print(f"{person} best language is {favorite_languages[person]}")

# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens:
#     for key, value in alien.items():
#         print(f"this key-{key} has a value of {value}")

# print(list(range(30)))


users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")