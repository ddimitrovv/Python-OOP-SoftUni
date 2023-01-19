class Child:
    def __init__(self, food_cost: int, *toys_cost):
        self.food_cost = food_cost
        self.toys_cost = sum([toy_cost for toy_cost in toys_cost])
        self.cost = self.food_cost + self.toys_cost

    def get_monthly_expense(self):
        return self.cost * 30
