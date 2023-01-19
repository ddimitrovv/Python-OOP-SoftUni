from abc import ABC, abstractmethod

from project.validators import str_len_less_than_value


class Horse(ABC):

    MIN_LEN_OF_NAME = 4
    SPEED_ERROR_MESSAGE = "Horse speed is too high!"
    NAME_ERROR_MESSAGE = "Horse name {} is less than 4 symbols!"

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken = False
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = str_len_less_than_value(
            value, self.MIN_LEN_OF_NAME, self.NAME_ERROR_MESSAGE.format(value)
        )

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > self.max_speed():
            raise ValueError(self.SPEED_ERROR_MESSAGE)
        self.__speed = value

    def train(self):
        self.speed = min((self.speed + self.speed_increment()), self.max_speed())

    @abstractmethod
    def max_speed(self):
        ...

    @abstractmethod
    def speed_increment(self):
        ...
