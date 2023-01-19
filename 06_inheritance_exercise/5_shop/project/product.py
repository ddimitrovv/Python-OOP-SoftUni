class Product:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity

    def decrease(self, quantity_to_decrease):
        if self.quantity >= quantity_to_decrease:
            self.quantity -= quantity_to_decrease

    def increase(self, quantity_to_increase):
        self.quantity += quantity_to_increase

    def __repr__(self):
        return self.name
