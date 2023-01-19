from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.rooms.room import Room


class YoungCouple(Room):
    ROOM_COST = 20
    ROOM_MEMBERS = 2
    APPLIANCES = [TV(), Fridge(), Laptop()]

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, budget=salary_one + salary_two, members_count=self.ROOM_MEMBERS)
        self.room_cost = self.ROOM_COST
        self.appliances = self.APPLIANCES * self.ROOM_MEMBERS
        self.expenses = self.calculate_expenses(self.appliances)
