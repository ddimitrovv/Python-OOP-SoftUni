from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN = 90
    OXYGEN_NEEDED = 15

    def __init__(self, name):
        super().__init__(name, oxygen=self.OXYGEN)

    def breathe(self):
        if self.oxygen - self.OXYGEN_NEEDED < 0:
            self.oxygen = 0
            return
        self.oxygen -= self.OXYGEN_NEEDED

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
