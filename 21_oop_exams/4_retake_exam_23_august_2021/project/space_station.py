from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet_repository import PlanetRepository
from project.planet.planet import Planet


class SpaceStation:
    astronaut_types = {
        "Biologist": Biologist,
        "Geodesist": Geodesist,
        "Meteorologist": Meteorologist,
    }

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()
        self.successful_missions = 0
        self.not_completed_missions = 0

    def add_astronaut(self, astronaut_type: str, name: str):
        current_astronaut = self.__find_by_name(name, self.astronaut_repository.astronauts)
        if current_astronaut is not None:
            return f"{name} is already added."
        if astronaut_type not in self.astronaut_types:
            raise Exception("Astronaut type is not valid!")

        current_astronaut = self.astronaut_types[astronaut_type](name)
        self.astronaut_repository.add(current_astronaut)
        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        current_planet = self.planet_repository.find_by_name(name)
        if current_planet is not None:
            return f"{name} is already added."
        current_planet = Planet(name)
        current_planet.items = [x for x in items.split(', ')]
        self.planet_repository.add(current_planet)
        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        current_astronaut = self.__find_by_name(name, self.astronaut_repository.astronauts)
        if current_astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")
        self.astronaut_repository.remove(current_astronaut)
        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        current_planet = self.__find_by_name(planet_name, self.planet_repository.planets)
        if current_planet is None:
            raise Exception("Invalid planet name!")
        astronauts_suitable_for_mission = self.__find_astronaut_for_mission(self.astronaut_repository.astronauts)

        if astronauts_suitable_for_mission is None:
            self.not_completed_missions += 1
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_for_mission = astronauts_suitable_for_mission if len(
            astronauts_suitable_for_mission) <= 5 else astronauts_suitable_for_mission[:5]
        successful_mission = False
        astronauts_collected_items = []
        for astronaut in astronauts_for_mission:
            while True:
                if astronaut.oxygen <= 0:
                    break
                if not current_planet.items:
                    successful_mission = True
                    break
                astronaut.backpack.append(current_planet.items.pop(-1))
                if astronaut not in astronauts_collected_items:
                    astronauts_collected_items.append(astronaut)
                astronaut.breathe()

        if not successful_mission:
            self.not_completed_missions += 1
            return "Mission is not completed."
        self.successful_missions += 1
        return f"Planet: {planet_name} was explored. {len(astronauts_collected_items)}" \
               f" astronauts participated in collecting items."

    def report(self):
        output = [f"{self.successful_missions} successful missions!",
                  f"{self.not_completed_missions} missions were not completed!",
                  f"Astronauts' info:"]
        for astronaut in self.astronaut_repository.astronauts:
            output.append(f"Name: {astronaut.name}")
            output.append(f"Oxygen: {astronaut.oxygen}")
            backpack_items = 'none' if not astronaut.backpack else ', '.join(astronaut.backpack)
            output.append(f"Backpack items: {backpack_items}")
        return '\n'.join(output)

    @staticmethod
    def __find_by_name(name, repository):
        for item in repository:
            if item.name == name:
                return item
        return None

    @staticmethod
    def __find_astronaut_for_mission(repo):
        astronauts = sorted(repo, key=lambda x: -x.oxygen)
        astronauts_for_mission = []
        for astronaut in astronauts:
            if len(astronauts) == 5:
                return astronauts_for_mission
            if astronaut.oxygen > 30:
                astronauts_for_mission.append(astronaut)
        return astronauts_for_mission if len(astronauts_for_mission) > 0 else None
