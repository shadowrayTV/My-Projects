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
        # print(self.name + " linked rooms :" + repr(self.linked_rooms))

    def get_details(self):
        print(f'The {self.name}:')
        print(f'{self.description}')
        print(f'------------------')
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f'The {room.get_name()} is to the {direction}.')
        print(f'')

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        elif direction == "north" or direction == "east" or direction == "west" or direction == "south":
            print("You can't go that way")
            return self
        else:
            print("That's not a valid command. Try again.")
            return self

