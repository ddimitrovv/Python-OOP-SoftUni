from project.validators import zero_or_positive_number_validator


class Room:
    EXPENSES_ERROR_MESSAGE = "Expenses cannot be negative"
    
    def __init__(self, name: str, budget: float, members_count: int, *children):
        self.family_name = name
        self.budget = budget
        self.members_count = members_count
        self.children = list(children) if children else []
        self.expenses = self.calculate_expenses()

    @property
    def expenses(self):
        return self.__expenses
    
    @expenses.setter
    def expenses(self, value):
        zero_or_positive_number_validator(value, self.EXPENSES_ERROR_MESSAGE)
        self.__expenses = value

    def calculate_expenses(self, *args):
        total = 0
        for arg in args:
            for item in arg:
                total += item.cost * 30
        self.expenses = total
        return total
