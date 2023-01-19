from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCoupleWithChildren(Room):
    ROOM_COST = 30
    ROOM_MEMBERS = 2
    APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float, *children):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=self.ROOM_MEMBERS + len(children))
        self.room_cost = self.ROOM_COST
        self.appliances = self.APPLIANCES * (self.ROOM_MEMBERS + len(children))
        self.children = list(children)
        self.expenses = sum(
            [(self.calculate_expenses(self.appliances)),
             self.calculate_expenses(children)])
