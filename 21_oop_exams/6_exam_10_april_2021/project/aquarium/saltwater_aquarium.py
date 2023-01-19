import os

from project.aquarium.base_aquarium import BaseAquarium
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class SaltwaterAquarium(BaseAquarium):
    CAPACITY = 25

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def __str__(self):
        fish_names = ' '.join([f.name for f in self.fish]) if self.fish else 'none'
        output = [f"{self.name}:", f"Fish: {fish_names}", f"Decorations: {len(self.decorations)}",
                  f"Comfort: {self.calculate_comfort()}"]
        return os.linesep.join(output)

    def add_fish(self, fish):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        if isinstance(fish, FreshwaterFish):
            return "Water not suitable."
        if isinstance(fish, SaltwaterFish):
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
