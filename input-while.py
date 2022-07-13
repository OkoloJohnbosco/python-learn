# age = int(input("What's ur age u sucker? "))
# print(f"he is {age}years old")

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

def sort_array(arr):
    odds = sorted((x for x in arr if x % 2 != 0), reverse=True)
    print(odds)
    return [x if x % 2 == 0 else odds.pop() for x in arr]


sorted_bro = sort_array([3, 8, 2, 7, 9])
print(sorted_bro)

