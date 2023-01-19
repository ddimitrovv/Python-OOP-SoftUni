from math import floor

from project.software.software import Software


class LightSoftware(Software):
    SOFTWARE_TYPE = "Light"
    CAPACITY_CONSUMPTION_MULTIPLIER = 1.5
    MEMORY_CONSUMPTION_MULTIPLIER = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.SOFTWARE_TYPE,
                         capacity_consumption=floor(capacity_consumption * self.CAPACITY_CONSUMPTION_MULTIPLIER),
                         memory_consumption=floor(memory_consumption * self.MEMORY_CONSUMPTION_MULTIPLIER))
