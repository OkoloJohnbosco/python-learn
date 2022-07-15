import time
import pizz

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

# Sometimes you’ll want to accept an arbitrary number of arguments, but you
# won’t know ahead of time what kind of information will be passed to the
# function. In this case, you can write functions that accept as many key-value
# pairs as the calling statement provides. One example involves building user
# profiles: you know you’ll get information about a user, but you’re not sure
# what kind of information you’ll receive. The function build_profile() in the
# Functions 149
# following example always takes in a first and last name, but it accepts an
# arbitrary number of keyword arguments as well:


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     # The double asterisks before the parameter **user_info cause Python to create
#     # an empty dictionary called user_info and pack whatever name-value pairs
#     # it receives into this dictionary.

#     print(type(user_info))
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info


# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics')
# print(user_profile)

pizz.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


def is_prime(given):
    start = time.time()
    answer = False
    if given <= 1:
        end = time.time()
        print(end - start)
        return answer
    if given == 2:
        answer = True
        end = time.time()
        print(end - start)
        return answer
    divisible_by = [value for value in range(2, given) if given % value == 0]
    if divisible_by:
        end = time.time()
        print(end - start)
        return answer
    else:
        answer = True
        return True
    end = time.time()
    print(end - start)

    flag = False


def is_prime(given_number):
    if given_number <= 1:
        return False
    elif given_number == 2:
        return True

    for each_number in range(2, given_number):
        if given_number % each_number == 0:
            return False
    return True
