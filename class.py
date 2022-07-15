class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        return ""

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog("wille", 7)
my_dog.sit()


class Resturant:
    """A simple Resturant class"""

    def __init__(self, resturant_name, cuisine_type):
        """Initialize resturant_name and cuisine_type"""
        self.resturant_name = resturant_name
        self.cuisine_type = cuisine_type

    def set_number_served(customer_number):
        print(f"The number of customers served is {customer_number}")

    def describe_restaurant(self):
        """Fxn that describes the resturant_name and cuisine_type"""
        print(f"{self.resturant_name} serves {self.cuisine_type}")


# dad_resturant = Resturant("Mama Put", "Jollof Ric")
# dad_resturant.describe_restaurant()


class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()


my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
