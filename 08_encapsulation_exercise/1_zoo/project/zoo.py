from project1.caretaker import Caretaker
from project1.cheetah import Cheetah
from project1.keeper import Keeper
from project1.lion import Lion
from project1.tiger import Tiger
from project1.vet import Vet


class Zoo:
    def __init__(self, name: str, budget: int, anima_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = anima_capacity
        self.__workers_capacity = workers_capacity
        self.animals = list()
        self.workers = list()

    def add_animal(self, animal, price):
        if self.__budget < price and self.__animal_capacity > len(self.animals):
            return 'Not enough budget'
        if self.__animal_capacity == len(self.animals):
            return 'Not enough space for animal'
        self.animals.append(animal)
        self.__budget -= price
        return f'{animal.name} the {animal.__class__.__name__} added to the zoo'

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f'{worker.name} the {worker.__class__.__name__} hired successfully'
        return 'Not enough space for worker'

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        total_salaries = sum(x.salary for x in self.workers)

        if self.__budget >= total_salaries:
            self.__budget -= total_salaries
            return f'You payed your workers. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to pay your workers. They are unhappy'

    def tend_animals(self):
        animal_care_budget = sum(x.money_for_care for x in self.animals)

        if self.__budget >= animal_care_budget:
            self.__budget -= animal_care_budget
            return f'You tended all the animals. They are happy. Budget left: {self.__budget}'
        return 'You have no budget to tend the animals. They are unhappy.'

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = list()
        output.append(f'You have {len(self.animals)} animals')
        lions = list(lion for lion in self.animals if isinstance(lion, Lion))
        tigers = list(tiger for tiger in self.animals if isinstance(tiger, Tiger))
        cheetahs = list(cheetah for cheetah in self.animals if isinstance(cheetah, Cheetah))
        output.append(f'----- {len(lions)} Lions:')
        for lion in lions:
            output.append(lion.__repr__())
        output.append(f'----- {len(tigers)} Tigers:')
        for tiger in tigers:
            output.append(tiger.__repr__())
        output.append(f'----- {len(cheetahs)} Cheetahs:')
        for cheetah in cheetahs:
            output.append(cheetah.__repr__())
        return '\n'.join(output)

    def workers_status(self):
        output = list()
        output.append(f'You have {len(self.workers)} workers')
        keepers = list(keeper for keeper in self.workers if isinstance(keeper, Keeper))
        caretakers = list(caretaker for caretaker in self.workers if isinstance(caretaker, Caretaker))
        vets = list(vet for vet in self.workers if isinstance(vet, Vet))
        output.append(f'----- {len(keepers)} Keepers:')
        for keeper in keepers:
            output.append(keeper.__repr__())
        output.append(f'----- {len(caretakers)} Caretakers:')
        for caretaker in caretakers:
            output.append(caretaker.__repr__())
        output.append(f'----- {len(vets)} Vets:')
        for vet in vets:
            output.append(vet.__repr__())
        return '\n'.join(output)
