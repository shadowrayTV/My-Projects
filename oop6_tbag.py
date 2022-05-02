from oop5_room import Room

kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")

kitchen.set_description("A dingy, poorly lit room, teeming with the smell of rotting waste and burning coal")
ballroom.set_description("Long forgotten, and untouched for who knows how long, the crumbling walls of this room")
dining_hall.set_description("A table, so long that it may as well fit a 100 people, is the centre of attraction here")

kitchen.describe()
