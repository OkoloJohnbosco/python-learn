from phone import Phone
from item import Item

# my_item = Item("IPhone", 1000, 3)
# my_item.calculate_total_price()
# my_item.pay_value = 0.7
# my_item.apply_discount()


# for instance in Item.all:
#     print(instance.name)


# Item.instantiate_from_csv()
# my_phones = Phone("Techno", 2000, 4, 5)
# print(my_phones.name)
# print(Item.all)
# # print(Phone.all)

item1 = Item("MyItem", 750)
print(item1.price)

item1.apply_increment(0.2)
print(item1.price)
