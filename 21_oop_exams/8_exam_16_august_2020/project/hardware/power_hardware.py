from math import floor

from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    HARDWARE_TYPE = "Power"
    CAPACITY_CONSUMPTION_MULTIPLIER = 0.25
    MEMORY_CONSUMPTION_MULTIPLIER = 1.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, self.HARDWARE_TYPE,
                         capacity=floor(capacity*self.CAPACITY_CONSUMPTION_MULTIPLIER),
                         memory=floor(memory*self.MEMORY_CONSUMPTION_MULTIPLIER))
