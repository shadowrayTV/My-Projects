from oop2_shapes import Paper, Rectangle, Oval
# Documentation at: https://rpf-futurelearn.s3-eu-west-1.amazonaws.com/OOP2/code/shapes.html#Shape

from random import randint

field = Paper()


class Player:
    # noinspection PyMethodMayBeStatic
    def __init__(self):
        self.pos_y = randint(50, 550)
        self.pos_x = randint(50, 550)

    # noinspection PyMethodMayBeStatic
    def bar(self):

        health = 100
        if (self.pos_x > 300 + int(diameter / 2) or self.pos_y > 300 + int(diameter / 2)) or (self.pos_x < 300 - int(diameter / 2) or self.pos_y < 300 - int(diameter / 2)):
            health = randint(0, 25)
        elif 300 - int(diameter / 2) < self.pos_y < 300 + int(diameter / 2) and 300 - int(diameter / 2) < self.pos_y < 300 + int(diameter / 2):
            health = randint(25, 66)
        elif 300 - int(diameter / 3) < self.pos_y < 300 + int(diameter / 3) and 300 - int(diameter / 3) < self.pos_y < 300 + int(diameter / 3):
            health = randint(66, 100)

        health_bar = Rectangle()
        health_bar.set_height(3)
        health_bar.set_width(int(health / 2))
        health_bar.set_y(self.pos_y - 15)
        health_bar.set_x(self.pos_x)
        if health < 10:
            health_bar.set_color("red")
        elif health < 30:
            health_bar.set_color("orange")
        elif health < 75:
            health_bar.set_color("yellow")
        elif health < 100:
            health_bar.set_color("green")
        elif health == 100:
            health_bar.set_color("dark green")
        health_bar.draw()
        print(health)

    # noinspection PyMethodMayBeStatic
    def body(self):
        torso = Rectangle()
        torso.set_color("white")
        torso.set_width(20)
        torso.set_height(30)
        torso.set_y(self.pos_y + 20)
        torso.set_x(self.pos_x + 2)

        head = Oval()
        head.set_color("white")
        head.set_width(25)
        head.set_height(25)
        head.set_y(self.pos_y - 5)
        head.set_x(self.pos_x)

        torso.draw()
        head.draw()


diameter = randint(200, 600)
zone = Oval()
zone.set_color("gray")
zone.set_width(diameter)
zone.set_height(diameter)
zone.set_x(300 - int(diameter / 2))
zone.set_y(300 - int(diameter / 2))
zone.draw()

p1 = Player()
print("P1: ")
p1.bar()
p1.body()

p2 = Player()
print("P2: ")
p2.bar()
p2.body()

p3 = Player()
print("P3: ")
p3.bar()
p3.body()

p4 = Player()
print("P4: ")
p4.bar()
p4.body()

p5 = Player()
print("P5: ")
p5.bar()
p5.body()

p6 = Player()
print("P6: ")
p6.bar()
p6.body()

p7 = Player()
print("P7: ")
p7.bar()
p7.body()

p8 = Player()
print("P8: ")
p8.bar()
p8.body()

print(f'Diameter: {diameter}')

field.display()
