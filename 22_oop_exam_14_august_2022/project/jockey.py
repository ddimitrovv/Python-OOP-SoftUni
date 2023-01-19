from project.validators import name_validator, greater_than_value_validator


class Jockey:

    NAME_ERROR_MESSAGE = "Name should contain at least one character!"
    MIN_AGE = 18
    AGE_ERROR_MESSAGE = "Jockeys must be at least {} to participate in the race!"

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.horse = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = name_validator(
            value, self.NAME_ERROR_MESSAGE
        )

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = greater_than_value_validator(
            value, self.MIN_AGE, self.AGE_ERROR_MESSAGE.format(self.MIN_AGE)
        )
