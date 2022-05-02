class Room:
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    def set_name(self, room_name):
        self.name = room_name

    def get_name(self):
        return self.name

    def set_description(self, room_description):
        self.description = room_description

    def get_description(self):
        return self.description

    def describe(self):
        print(f'{self.name}: {self.description}')

    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

