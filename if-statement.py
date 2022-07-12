cars = ["bnw", "audi", "tesla", "ferrari"]

for car in cars:
    if car == "bnw":
        print(car.upper())
    else:
        print(car.lower())

car = 'subaru'  
age = 18

if age < 4:
    print("your addmission fee is $0")
elif age < 18:
    print("your addmission fee is $25")
else:
    print("your addmission fee is $40")

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40

print(f"Your admission cost is ${price}.")

available_toppings = ['mushrooms', 'olives', 'green peppers',
'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")