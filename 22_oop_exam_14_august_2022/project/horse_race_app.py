from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey
from project.validators import find_by_name


class HorseRaceApp:

    HORSE_TYPES = {
        'Appaloosa': Appaloosa,
        'Thoroughbred': Thoroughbred
    }

    def __init__(self):
        self.horses = []  # An empty list that will contain all the horses (objects).
        self.jockeys = []  # An empty list that will contain all the jockeys (objects).
        self.horse_races = []  # An empty list that will contain all the horse races (objects).

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_type not in self.HORSE_TYPES:
            return
        horse = find_by_name(horse_name, self.horses)
        if horse is not None:
            raise Exception(f"Horse {horse_name} has been already added!")
        current_horse = self.HORSE_TYPES[horse_type](horse_name, horse_speed)
        self.horses.append(current_horse)
        return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = find_by_name(jockey_name, self.jockeys)
        if jockey is not None:
            raise Exception(f"Jockey {jockey_name} has been already added!")
        current_jockey = Jockey(jockey_name, age)
        self.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = [r for r in self.horse_races if r.race_type == race_type]
        if race:
            raise Exception(f"Race {race_type} has been already created!")
        current_race = HorseRace(race_type)
        self.horse_races.append(current_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        current_jockey = find_by_name(jockey_name, self.jockeys)
        if current_jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        available_horses = [h for h in self.horses if h.__class__.__name__ == horse_type and not h.is_taken]
        if not available_horses:
            raise Exception(f"Horse breed {horse_type} could not be found!")
        if current_jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."
        current_horse = available_horses[-1]
        current_horse.is_taken = True
        current_jockey.horse = current_horse
        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        races = [r for r in self.horse_races if r.race_type == race_type]
        if not races:
            raise Exception(f"Race {race_type} could not be found!")

        current_race = races[0]
        current_jockey = find_by_name(jockey_name, self.jockeys)

        if current_jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")
        if current_jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")
        if current_jockey in current_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        current_race.jockeys.append(current_jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        races = [r for r in self.horse_races if r.race_type == race_type]
        if not races:
            raise Exception(f"Race {race_type} could not be found!")
        current_race = races[0]
        if len(current_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        sorted_participants = sorted(current_race.jockeys, key=lambda jockey: -jockey.horse.speed)
        winner = sorted_participants[0]

        return f"The winner of the {current_race.race_type} race, " \
               f"with a speed of {winner.horse.speed}km/h is {winner.name}! " \
               f"Winner's horse: {winner.horse.name}."
