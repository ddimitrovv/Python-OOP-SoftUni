from project.appliances.tv import TV
from project.rooms.room import Room


class AloneYoung(Room):
    ROOM_COST = 10
    ROOM_MEMBERS = 1
    APPLIANCES = [TV()]

    def __init__(self, family_name: str, salary: float):
        super().__init__(family_name, budget=salary, members_count=self.ROOM_MEMBERS)
        self.room_cost = self.ROOM_COST
        self.appliances = self.APPLIANCES
        self.expenses = self.calculate_expenses(self.appliances)
