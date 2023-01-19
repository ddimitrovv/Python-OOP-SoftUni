# Create a class called Shop. Upon initialization, it should receive
# a name (str), type (str), capacity (int).
# The store should also have an attribute called items
# (an empty dictionary that stores the name of an item and its quantity).
# The class should have 4 methods:
#     • small_shop(name: str, type: str) - a new shop with a capacity of 10 should be created
#     • add_item(item_name:str) - adds 1 to the quantity of the given item.
#       On success, the method should return "{item_name} added to the shop".
#       If the addition is not possible, the following message should be returned
#       "Not enough capacity in the shop"
#     • remove_item(item_name:str, amount:int) - removes the given amount from the item.
#       On success, it should return "{amount} {item_name} removed from the shop".
#       Otherwise, the method should return "Cannot remove {amount} {item_name}"
#         ◦ If the item quantity reaches 0, the item should be removed from the items' dictionary.
#     • __repr__() - returns a string representation in the format
#       "{shop_name} of type {shop_type} with capacity {shop_capacity}"

class Shop:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = dict()

    @classmethod
    def small_shop(cls, name, type):
        return cls(name, type, 10)

    def add_item(self, item_name):
        if sum(self.items.values()) == self.capacity:
            return f'Not enough capacity in the shop'
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        return f'{item_name} added to the shop'

    def remove_item(self, item_name, amount):
        if item_name in self.items and self.items[item_name] >= amount:
            self.items[item_name] -= amount
            if self.items[item_name] == 0:
                del self.items[item_name]
            return f'{amount} {item_name} removed from the shop'
        return f'Cannot remove {amount} {item_name}'

    def __repr__(self):
        return f'{self.name} of type {self.type} with capacity {self.capacity}'


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
print(small_shop.items)
