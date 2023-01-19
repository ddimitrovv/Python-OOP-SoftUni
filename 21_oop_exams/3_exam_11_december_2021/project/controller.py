from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    car_types = {
        "SportsCar": SportsCar,
        "MuscleCar": MuscleCar,
    }

    def __init__(self):
        self.cars = list()
        self.drivers = list()
        self.races = list()

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type not in self.car_types:
            return
        for car in self.cars:
            if car.model == model:
                raise Exception(f"Car {model} is already created!")
        try:
            current_car = self.car_types[car_type](model, speed_limit)
            self.cars.append(current_car)
            return f"{car_type} {model} is created."
        except ValueError:
            ...

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")
        try:
            current_driver = Driver(driver_name)
            self.drivers.append(current_driver)
            return f"Driver {driver_name} is created."
        except ValueError:
            ...

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")
        try:
            current_race = Race(race_name)
            self.races.append(current_race)
            return f"Race {race_name} is created."
        except ValueError:
            ...

    def add_car_to_driver(self, driver_name: str, car_type: str):
        current_drivers = [driver for driver in self.drivers if driver.name == driver_name]
        if not current_drivers:
            raise Exception(f"Driver {driver_name} could not be found!")
        current_cars = [car for car in self.cars if (car.__class__.__name__ == car_type and not car.is_taken)]
        if not current_cars:
            raise Exception(f"Car {car_type} could not be found!")
        current_car = current_cars[-1]
        current_driver = current_drivers[0]
        if current_driver.car:
            old_car = current_driver.car
            old_car.is_taken = False
            current_driver.car = current_car
            current_car.is_taken = True
            return f"Driver {current_driver.name} changed his car from {old_car.model} to {current_car.model}."
        else:
            current_car.is_taken = True
            current_driver.car = current_car
            return f"Driver {driver_name} chose the car {current_car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        races = [race for race in self.races if race.name == race_name]
        if not races:
            raise Exception(f"Race {race_name} could not be found!")
        drivers = [driver for driver in self.drivers if driver.name == driver_name]
        if not drivers:
            raise Exception(f"Driver {driver_name} could not be found!")
        current_race = races[0]
        current_driver = drivers[0]
        if not current_driver.car:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if current_driver in current_race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."
        current_race.drivers.append(current_driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        current_races = [race for race in self.races if race.name == race_name]
        if not current_races:
            raise Exception(f"Race {race_name} could not be found!")
        current_race = current_races[0]
        if len(current_race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")
        drivers = current_race.drivers
        sorted_drivers = sorted(drivers, key=lambda x: -x.car.speed_limit)
        output = list()
        for driver in sorted_drivers[:3]:
            driver.number_of_wins += 1
            output.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")
        return '\n'.join(output)
