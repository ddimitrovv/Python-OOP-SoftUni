from abc import ABC, abstractmethod

from project.validators import name_validator, greater_than_zero_validator


class BaseFish(ABC):
    NAME_ERROR_MESSAGE = "Fish name cannot be an empty string."
    SPECIES_ERROR_MESSAGE = "Fish species cannot be an empty string."
    PRICE_ERROR_MESSAGE = "Price cannot be equal to or below zero."
    FISH_SIZE_INCREASE = 5

    def __init__(self, name: str, species: str, size: int, price: float):
        self.name = name
        self.species = species
        self.size = size
        self.price = price

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value
        
    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        name_validator(value, self.SPECIES_ERROR_MESSAGE)
        self.__species = value

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        greater_than_zero_validator(value, self.PRICE_ERROR_MESSAGE)
        self.__price = value

    @abstractmethod
    def eat(self):
        self.size += self.FISH_SIZE_INCREASE
