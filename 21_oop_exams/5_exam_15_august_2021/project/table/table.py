from abc import ABC, abstractmethod

from project.baked_food.baked_food import BakedFood
from project.drink.drink import Drink
from project.validators import greater_than_zero_validator


class Table(ABC):
    CAPACITY_ERROR_MESSAGE = "Capacity has to be greater than 0!"

    def __init__(self, table_number: int, capacity: int):
        self.table_number = table_number
        self.capacity = capacity
        self.food_orders = []
        self.drink_orders = []
        self.number_of_people = 0
        self.is_reserved = False

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        greater_than_zero_validator(value, self.CAPACITY_ERROR_MESSAGE)
        self.__capacity = value

    def reserve(self, number_of_people: int):
        if self.is_reserved or number_of_people > self.capacity:
            return
        self.number_of_people = number_of_people
        self.is_reserved = True

    def order_food(self, baked_food: BakedFood):
        self.food_orders.append(baked_food)

    def order_drink(self, drink: Drink):
        self.drink_orders.append(drink)

    def get_bill(self):
        food_ordered_price = sum(f.price for f in self.food_orders)
        drink_ordered_price = sum([d.price for d in self.drink_orders])
        return food_ordered_price + drink_ordered_price

    def clear(self):
        self.food_orders.clear()
        self.drink_orders.clear()
        self.number_of_people = 0
        self.is_reserved = False

    @abstractmethod
    def free_table_info(self):
        ...
