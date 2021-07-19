class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room.number == room_number][0]
        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number):
        room = [room for room in self.rooms if room.number == room_number][0]
        self.guests -= room.guests

        room.free_room()

    def status(self):
        free_rooms_number = [r.number for r in self.rooms if not r.is_taken]
        taken_room_numbers = [r.number for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join(map(str, free_rooms_number))}\n" \
               f"Taken rooms: {', '.join(map(str, taken_room_numbers))}"
