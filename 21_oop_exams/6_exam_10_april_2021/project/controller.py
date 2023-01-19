import os

from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish
from project.validators import find_by_name


class Controller:
    aquarium_types = {
        'FreshwaterAquarium': FreshwaterAquarium,
        'SaltwaterAquarium': SaltwaterAquarium,
    }

    decoration_types = {
        'Ornament': Ornament,
        'Plant': Plant,
    }

    fish_types = {
        'FreshwaterFish': FreshwaterFish,
        'SaltwaterFish': SaltwaterFish,
    }

    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type not in self.aquarium_types:
            return "Invalid aquarium type."
        current_aquarium = self.aquarium_types[aquarium_type](aquarium_name)
        self.aquariums.append(current_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        if decoration_type not in self.decoration_types:
            return "Invalid decoration type."
        current_decoration = self.decoration_types[decoration_type]()
        self.decorations_repository.add(current_decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        current_aquarium = find_by_name(aquarium_name, self.aquariums)
        if current_aquarium is None:
            return
        if decoration_type not in self.decoration_types:
            return
        current_decoration = self.decoration_types[decoration_type]()
        for i, d in enumerate(self.decorations_repository.decorations):
            if decoration_type == current_decoration.decoration_type:
                current_aquarium.add_decoration(current_decoration)
                self.decorations_repository.decorations.pop(i)
                return f"Successfully added {decoration_type} to {aquarium_name}."
        return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in self.fish_types:
            return f"There isn't a fish of type {fish_type}."
        current_aquarium = find_by_name(aquarium_name, self.aquariums)
        if current_aquarium is None:
            return

        current_fish = self.fish_types[fish_type](fish_name, fish_species, price)
        return current_aquarium.add_fish(current_fish)

    def feed_fish(self, aquarium_name: str):
        current_aquarium = find_by_name(aquarium_name, self.aquariums)
        if current_aquarium is None:
            return
        current_aquarium.feed()
        return f"Fish fed: {len(current_aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        current_aquarium = find_by_name(aquarium_name, self.aquariums)
        if current_aquarium is None:
            return
        f_price = 0 if not current_aquarium.fish else sum([f.price for f in current_aquarium.fish])
        d_price = 0 if not current_aquarium.decorations else sum([d.price for d in current_aquarium.decorations])
        return f"The value of Aquarium {aquarium_name} is {(f_price + d_price):.2f}."

    def report(self):
        output = []
        for aquarium in self.aquariums:
            output.append(str(aquarium))
        return os.linesep.join(output)
