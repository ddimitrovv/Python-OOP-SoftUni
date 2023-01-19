from abc import ABC, abstractmethod

from project.validators import name_validator


class Astronaut(ABC):
    NAME_ERROR_MESSAGE = "Astronaut name cannot be empty string or whitespace!"
    OXYGEN_NEEDED = 10

    def __init__(self, name, oxygen):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value

    @abstractmethod
    def breathe(self):
        if self.oxygen - self.OXYGEN_NEEDED < 0:
            self.oxygen = 0
            return
        self.oxygen -= self.OXYGEN_NEEDED

    @abstractmethod
    def increase_oxygen(self, amount: int):
        self.oxygen += amount
