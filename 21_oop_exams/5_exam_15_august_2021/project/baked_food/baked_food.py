from abc import ABC, abstractmethod

from project.validators import name_validator, greater_than_zero_validator


class BakedFood(ABC):
    NAME_ERROR_MESSAGE = "Name cannot be empty string or white space!"
    PRICE_ERROR_MESSAGE = "Price cannot be less than or equal to zero!"
    PORTION_ERROR_MESSAGE = "Portion cannot be less than or equal to zero!"

    def __init__(self, name: str, portion: float, price: float):
        self.name = name
        self.portion = portion
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def portion(self):
        return self.__portion

    @portion.setter
    def portion(self, value):
        greater_than_zero_validator(value, self.PORTION_ERROR_MESSAGE)
        self.__portion = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        greater_than_zero_validator(value, self.PRICE_ERROR_MESSAGE)
        self.__price = value

    @abstractmethod
    def __repr__(self):
        ...
