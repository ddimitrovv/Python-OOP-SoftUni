from project1.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = list()

    @property
    def guests(self):
        return sum(room.guests for room in self.rooms)

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                room.free_room()

    def status(self):
        free_rooms = ', '.join(str(room.number) for room in self.rooms if not room.is_taken)
        taken_rooms = ', '.join(str(room.number) for room in self.rooms if room.is_taken)
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {free_rooms}\n" \
               f"Taken rooms: {taken_rooms}"
