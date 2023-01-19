from project.baked_food.baked_food import BakedFood


class Cake(BakedFood):
    PORTION = 245

    def __init__(self, name: str, price: float):
        super().__init__(name, self.PORTION, price)

    def __repr__(self):
        return f" - {self.name}: {self.PORTION:.2f}g - {self.price:.2f}lv"
