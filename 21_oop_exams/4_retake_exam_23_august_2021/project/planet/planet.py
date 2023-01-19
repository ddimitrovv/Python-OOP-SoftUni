from project.validators import name_validator


class Planet:
    NAME_ERROR_MESSAGE = "Planet name cannot be empty string or whitespace!"

    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value, self.NAME_ERROR_MESSAGE)
        self.__name = value
