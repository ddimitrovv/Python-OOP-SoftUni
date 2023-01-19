from project.supply.supply import Supply


class Drink(Supply):
    ENERGY = 15

    def __init__(self, name):
        super().__init__(name, energy=self.ENERGY)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
