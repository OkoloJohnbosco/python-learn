from item import Item


class Phone(Item):
    # all = []

    def __init__(self, name: str, price: int, quantity=0, broken_phones=0):
        super().__init__(name, price, quantity)

        # Run validation to receive arguments specific to the Phone class
        assert broken_phones >= 0, f"BrokenPhones {broken_phones} is not greater than Zero!"

        # Assign to self obj
        self.broken_phones = broken_phones

        # Actions to execute
        # Phone.all.append(self)
