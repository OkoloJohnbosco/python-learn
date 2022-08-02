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
        with open('item.csv', "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        pass
        for item in items:
            # Instantiate the class
            Item(
                name=item.get('name'),
                price=int(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # we will count out the floats that are point zero
        # I.E 5.0, 10.0

        if isinstance(num, float):
            # Count out the float that are point zero
            return num.is_integer
        elif isinstance(num, int):
            return True
        else:
            return False
        pass

    def __repr__(self) -> str:
        return f"Item ('{self.name}', {self.price}, {self.quantity})"

# my_item = Item("IPhone", 1000, 3)
# my_item.calculate_total_price()
# my_item.pay_value = 0.7
# my_item.apply_discount()


# for instance in Item.all:
#     print(instance.name)

class Phone(Item):
    all = []
    def __init__(self,name: str, price: int, quantity=0, broken_phones = 0):
        super().__init__(name, price, quantity)

        # Run validation to receive arguments specific to the Phone class
        assert broken_phones >= 0, f"BrokenPhones {broken_phones} is not greater than Zero!"
        
        # Assign to self obj
        self.broken_phones = broken_phones

Item.instantiate_from_csv()
my_phones = Phone("Techno", 2000, 4, 5)
print(Item.all)
