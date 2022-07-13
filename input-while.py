# age = int(input("What's ur age u sucker? "))
# print(f"he is {age}years old")

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)


# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

# Solution
def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    print(odds)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


sorted_bro = sort_array([3, 8, 2, 7, 9])
print(sorted_bro)

active = True
prompt = "Enter a cool city "

# while active:
#     message = input(prompt)

#     if message == "quit":
#         active = False
#         print("Program ended")
#     else:
#         print(message)

# Break example
# while True:
#     city = input(prompt)

#     if city == "quit":
#         break
#     else:
#         print(f"I would love to visit {city.title()}!")

# Continue example
# current_number = 0
# while current_number < 10:
#     current_number += 1
#     if current_number % 2 == 0:
#         continue
#     print(current_number)


# Exercise from texbook
# while True:
#     age = int(input("Enter your age: "))
#     if age < 3:
#         print("Your ticket is free")
#     elif age < 12:
#         print("Your ticket fee is $10")
#     else:
#         print("Your ticket fee is $15")
#     break

# Adding from a list to anotheer list
# unconfirmed_users = ['alice', "brian", "candance"]
# confirmed_users = []

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all confirmed users
# print(f"\nThe following users have been confirmed: ")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# FILLING A DICTIONARY WITH USER INPUT
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    # Store the response in the dictionary.
    responses[name] = response
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        print(responses)
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
