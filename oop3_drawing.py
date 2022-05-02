from oop2_shapes import Paper, Rectangle

paper = Paper()

rect1 = Rectangle()
rect1.set_width(200), rect1.set_height(100), rect1.set_color("green")
rect1.draw()

rect2 = Rectangle()
rect2.set_width(-150), rect2.set_height(-350), rect2.set_color("red")
rect2.draw()

paper.display()
