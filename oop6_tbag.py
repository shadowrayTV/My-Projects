from oop5_room import Room

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

kitchen.set_description("A dingy, poorly lit room, teeming with the smell of rotting waste and burning coal.")
ballroom.set_description("Long untouched, the crumbling walls of this room bear distinct marks of violence.")
dining_hall.set_description("The room has a funky smell. Someone, or something, has been here recently.")

kitchen.link_room(dining_hall, "south")
ballroom.link_room(dining_hall, "east")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")

current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input(">").lower()
    current_room = current_room.move(command)
