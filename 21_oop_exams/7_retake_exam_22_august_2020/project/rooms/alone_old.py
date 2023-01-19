from project.rooms.room import Room


class AloneOld(Room):
    ROOM_COST = 10
    ROOM_MEMBERS = 1
    APPLIANCES = []

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, budget=pension, members_count=self.ROOM_MEMBERS)
        self.room_cost = self.ROOM_COST
        self.appliances = self.APPLIANCES
        self.expenses = self.calculate_expenses(self.appliances)
