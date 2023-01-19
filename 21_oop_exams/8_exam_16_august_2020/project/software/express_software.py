from math import floor

from project.software.software import Software


class ExpressSoftware(Software):
    SOFTWARE_TYPE = "Express"
    CAPACITY_CONSUMPTION_MULTIPLIER = 1
    MEMORY_CONSUMPTION_MULTIPLIER = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, self.SOFTWARE_TYPE,
                         capacity_consumption=floor(capacity_consumption * self.CAPACITY_CONSUMPTION_MULTIPLIER),
                         memory_consumption=floor(memory_consumption * self.MEMORY_CONSUMPTION_MULTIPLIER))
