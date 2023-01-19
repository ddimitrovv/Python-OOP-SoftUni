from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN = 70
    OXYGEN_NEEDED = 5

    def __init__(self, name):
        super().__init__(name, oxygen=self.OXYGEN)

    def breathe(self):
        if self.oxygen - self.OXYGEN_NEEDED < 0:
            self.oxygen = 0
            return
        self.oxygen -= self.OXYGEN_NEEDED

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
