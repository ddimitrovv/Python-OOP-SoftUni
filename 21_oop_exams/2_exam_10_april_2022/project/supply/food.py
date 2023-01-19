from project.supply.supply import Supply


class Food(Supply):
    ENERGY_OPTIONAL = 25

    def __init__(self, name, energy=ENERGY_OPTIONAL):
        super().__init__(name, energy)

    def details(self):
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
