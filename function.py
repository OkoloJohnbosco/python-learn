# Defining a simple fxn
def greet_user():
    print("Hello world")

# Keyword Argument with default value


def describe_pet(animal_type, pet_name="Harry"):
    print(f"\nI have a {animal_type.title()}")
    print(f"my {animal_type.title()} name is {pet_name}")


# Calling the function with keyword
# describe_pet(animal_type="rabbit")
# describe_pet("dog")
# describe_pet(pet_name="Josh", animal_type="Cat")


# def get_formatted_name(first_name, last_name, middle_name=''):
#     if middle_name:
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()


# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)


# def make_pizza(*toppings):
#     """Print the list of toppings that have been requested."""
#     print(type(toppings))
#     print(toppings.count('mushrooms'))
#     print('pepperoni' in toppings)
#     print(toppings)

#     # return


# make_pizza('pepperoni')
# make_pizza('mushrooms', 'extra cheese',
#            'green peppers', 'extra cheese')

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
