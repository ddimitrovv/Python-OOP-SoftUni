import os
from abc import ABC, abstractmethod

from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.validators import name_validator


class BaseAquarium(ABC):
    NAME_ERROR_MESSAGE = "Aquarium name cannot be an empty string."

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value

    def calculate_comfort(self):
        return sum([d.comfort for d in self.decorations])

    @abstractmethod
    def add_fish(self, fish):
        ...

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        if isinstance(decoration, Ornament) or isinstance(decoration, Plant):
            self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    @abstractmethod
    def __str__(self):
        fish_names = ' '.join([f.name for f in self.fish]) if self.fish else 'none'
        output = [f"{self.name}:", f"Fish: {fish_names}", f"Decorations: {len(self.decorations)}",
                  f"Comfort: {self.calculate_comfort()}"]
        return os.linesep.join(output)
