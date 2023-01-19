import os

from project.rooms.room import Room


class Everland:
    def __init__(self):
        self.rooms = []

    def add_room(self, room: Room):
        self.rooms.append(room)

    def get_monthly_consumptions(self):
        total = 0
        for room in self.rooms:
            total += room.expenses + room.room_cost
        return f"Monthly consumption: {total:.2f}$."

    def pay(self):
        output = []
        for room in self.rooms:
            if room.budget >= room.expenses + room.room_cost:
                expenses = room.expenses + room.room_cost
                room.budget -= expenses
                output.append(f"{room.family_name} paid {(room.expenses + room.room_cost):.2f}$ "
                              f"and have {room.budget:.2f}$ left.")
            else:
                self.rooms.remove(room)
                output.append(f"{room.family_name} does not have enough budget and must leave the hotel.")

        return os.linesep.join(output)

    def status(self):
        members = sum(r.members_count for r in self.rooms)
        output = [f"Total population: {members}"]
        for room in self.rooms:
            output.append(f"{room.family_name} with {room.members_count} members. Budget: {room.budget:.2f}$, ")
            output.append(f"Expenses: {room.expenses:.2f}$")
            if room.children:
                for idx, child in enumerate(room.children):
                    output.append(f"--- Child {idx + 1} monthly cost: {child.get_monthly_expense():.2f}$")
            if room.appliances:
                cost_of_all_appliances_for_one_month = sum([x.get_monthly_expense() for x in room.appliances])\
                                                       * room.members_count
                output.append(f"--- Appliances monthly cost: {cost_of_all_appliances_for_one_month:.2f}$")

        return os.linesep.join(output)
