from project1.worker import Worker


class Vet(Worker):
    def __init__(self, name, age, salary):
        super().__init__(name, age, salary)
