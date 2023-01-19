from project1.motorcycle import Motorcycle


class CrossMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
