import os

from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware
from project.validators import if_item_name_exists, find_by_name


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        current_hardware = PowerHardware(name, capacity, memory)
        System._hardware.append(current_hardware)

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        current_hardware = HeavyHardware(name, capacity, memory)
        System._hardware.append(current_hardware)

    @staticmethod
    def register_express_software(hardware_name: str, name: str,
                                  capacity_consumption: int, memory_consumption: int):
        current_software = ExpressSoftware(name, capacity_consumption, memory_consumption)
        if not if_item_name_exists(hardware_name, System._hardware):
            return "Hardware does not exist"
        current_hardware = find_by_name(hardware_name, System._hardware)
        current_hardware.install(current_software)
        System._software.append(current_software)

    @staticmethod
    def register_light_software(hardware_name: str, name: str,
                                capacity_consumption: int, memory_consumption: int):
        current_software = LightSoftware(name, capacity_consumption, memory_consumption)
        if not if_item_name_exists(hardware_name, System._hardware):
            return "Hardware does not exist"
        current_hardware = find_by_name(hardware_name, System._hardware)
        current_hardware.install(current_software)
        System._software.append(current_software)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        current_software = find_by_name(software_name, System._software)
        current_hardware = find_by_name(hardware_name, System._hardware)

        if not current_software or not current_hardware:
            return "Some of the components do not exist"

        current_hardware.uninstall(current_software)
        System._software.remove(current_software)

    @staticmethod
    def analyze():
        return f"""System Analysis
Hardware Components: {len(System._hardware)}
Software Components: {len(System._software)}
Total Operational Memory: {sum([x.memory_consumption for x in System._software])} / {sum(
            [x.memory for x in System._hardware])}
Total Capacity Taken: {sum([x.capacity_consumption for x in System._software])} / {sum(
            [x.capacity for x in System._hardware])}"""

    @staticmethod
    def system_split():
        output = ''
        for hardware in System._hardware:
            software_components_names = [x.name for x in hardware.software_components]
            s_components_names = ", ".join(software_components_names) if software_components_names else 'None'
            output += f"""Hardware Component - {hardware.name}
Express Software Components: {len([x for x in hardware.software_components if x.software_type == 'Express'])}
Light Software Components: {len([x for x in hardware.software_components if x.software_type == 'Light'])}
Memory Usage: {sum([x.memory_consumption for x in hardware.software_components])} / {hardware.memory}
Capacity Usage: {sum([x.capacity_consumption for x in hardware.software_components])} / {hardware.capacity}
Type: {hardware.hardware_type}
Software Components: {s_components_names}""" + os.linesep
        return output.strip()
