from project1.animals.animal import Mammal


class Mouse(Mammal):
    @property
    def weight_increase(self):
        return 0.1

    @property
    def allowed_food(self):
        return ['Vegetable', 'Fruit']

    def make_sound(self):
        return 'Squeak'


class Dog(Mammal):
    @property
    def weight_increase(self):
        return 0.4

    @property
    def allowed_food(self):
        return ['Meat']

    def make_sound(self):
        return 'Woof!'


class Cat(Mammal):
    @property
    def weight_increase(self):
        return 0.3

    @property
    def allowed_food(self):
        return ['Vegetable', 'Meat']

    def make_sound(self):
        return 'Meow'


class Tiger(Mammal):
    @property
    def weight_increase(self):
        return 1.00

    @property
    def allowed_food(self):
        return ['Meat']

    def make_sound(self):
        return 'ROAR!!!'
