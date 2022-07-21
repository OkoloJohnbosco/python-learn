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


my_dog = Dog(age=7, name="Victony")
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
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """A simple Electric car class inheirted from Car class"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        return "this is from the electric car class"


# my_new_car = Car('audi', 'a4', 2019)
# print(my_new_car.get_descriptive_name())
# print(type(my_new_car.get_descriptive_name()))


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
print(my_tesla.battery.describe_battery())
print(my_tesla.battery.battery_size)
print(my_tesla.battery.get_range())
# Overriding method from parent class - DONE
# Instance as Attributes - DONE


# class Animal(object):
#     """A simple Animal class"""

#     def __init__(self):
#         print("Instantiating animal class")

#     def eat(self):
#         print("I am eating")


# class Cat(Animal):
#     """Extending the Animal class"""

#     def __init__(self):
#         Animal.__init__(self)
#         print("cat created")

#     def meow(self):
#         Animal.eat(self)
#         print("meow")


# my_cat = Cat()
# my_cat.meow()
# my_cat.eat()


# import { useEffect } from 'react'

# export default function useClickOutside({ ref, callback }) {
#   useEffect(() => {
#     const handleClickOutside = (e) => {
#       if (ref.current && !ref.current.contains(e.target)) {
#         callback()
#       }
#     }
#     document.addEventListener('mousedown', handleClickOutside)
#     return () => {
#       document.removeEventListener('mousedown', handleClickOutside)
#     }
#   }, [ref, callback])
# }