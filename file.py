# Things to learn files and exeception
# with open('digits.txt') as file_object:
#     contents = file_object.read().rstrip()
#     print(file_object)
# print(contents)

file_path = "/src/flutter/examples/README.md"

with open(file_path) as file_object:
    mdFile = file_object.readlines()

# for line in mdFile:
#     print(line.rstrip())

# pi_string = ''
# for line in mdFile:
#     pi_string += line.strip()

# print(pi_string)
# print(len(pi_string))

with open('digits.txt', "a") as file_object:
    file_object.write("\nI love programming.")
    file_object.write("\nI love creating new games.")


def count_words(filename):
    """Count the approximate number of words in a file."""
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")
