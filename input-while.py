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


while True:
    age = int(input("Enter your age: "))
    if age < 3:
        print("Your ticket is free")
    elif age < 12:
        print("Your ticket fee is $10")
    else:
        print("Your ticket fee is $15")
    break
