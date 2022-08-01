import csv


class Item:
    pay_value = 0.8
    all = []

    def __init__(self, name: str, price: int, quantity=0):
        # Run Validation
        assert price >= 0, f"Price {price} is not greater than Zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater than Zero!"

        # Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        self.pay_value = Item.pay_value

        # Append to the [all] list when u create an instance
        Item.all.append(self)

    def calculate_total_price(self):
        total = self.price * self.quantity
        print(total)
        print(self)

    def apply_discount(self):
        self.price = self.price * self.pay_value

    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv', r) as f:
            reader = csv.DictReader(f)
            items = list(reader)
        pass
        for item in items:
            print(item)

    def __repr__(self) -> str:
        return f"Item ('{self.name}', {self.price}, {self.quantity})"

# my_item = Item("IPhone", 1000, 3)
# my_item.calculate_total_price()
# my_item.pay_value = 0.7
# my_item.apply_discount()


item1 = Item("Phone", 100, 1)
item1 = Item("Laptop", 1000, 3)
item1 = Item("Cable", 10, 5)
item1 = Item("Mouse", 50, 5)
item1 = Item("Keyboard", 75, 5)

# for instance in Item.all:
#     print(instance.name)

print(Item.all)
