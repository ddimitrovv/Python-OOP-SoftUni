from project.software.software import Software


class Hardware:
    def __init__(self, name: str, hardware_type: str, capacity: int, memory: int):
        self.name = name
        self.hardware_type = hardware_type
        self.capacity = capacity
        self.capacity_taken = 0
        self.memory = memory
        self.memory_taken = 0
        self.software_components = []

    def install(self, software: Software):
        if self.capacity < software.capacity_consumption + self.capacity_taken or\
                self.memory < software.memory_consumption + self.memory_taken:
            raise Exception("Software cannot be installed")
        self.capacity_taken += software.capacity_consumption
        self.memory_taken += software.memory_consumption
        self.software_components.append(software)

    def uninstall(self, software: Software):
        if software in self.software_components:
            self.capacity_taken -= software.capacity_consumption
            self.memory_taken -= software.memory_consumption
            self.software_components.remove(software)
