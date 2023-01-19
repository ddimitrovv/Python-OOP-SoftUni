from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV
from project.rooms.room import Room


class OldCouple(Room):
    ROOM_COST = 15
    ROOM_MEMBERS = 2
    APPLIANCES = [TV(), Fridge(), Stove()]

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, budget=pension_one + pension_two, members_count=self.ROOM_MEMBERS)
        self.room_cost = self.ROOM_COST
        self.appliances = self.APPLIANCES * self.ROOM_MEMBERS
        self.expenses = self.calculate_expenses(self.appliances)
