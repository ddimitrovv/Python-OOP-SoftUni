from project1.animals.animal import Bird


class Owl(Bird):
    @property
    def weight_increase(self):
        return 0.25

    @property
    def allowed_food(self):
        return ['Meat']

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    @property
    def weight_increase(self):
        return 0.35

    @property
    def allowed_food(self):
        return ['Meat', 'Fruit', 'Vegetable', 'Seed']

    def make_sound(self):
        return "Cluck"
