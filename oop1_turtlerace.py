from turtle import Turtle
from random import randint

brenda = Turtle()
brenda.color('red')
brenda.shape('turtle')
brenda.pu()
brenda.goto(-160, 100)
brenda.pd()

marie = Turtle()
marie.color('blue')
marie.shape('turtle')
marie.pu()
marie.goto(-160, 70)
marie.pd()

pickle = Turtle()
pickle.color('green')
pickle.shape('turtle')
pickle.pu()
pickle.goto(-160, 40)
pickle.pd()

karen = Turtle()
karen.color('yellow')
karen.shape('turtle')
karen.pu()
karen.goto(-160, 10)
karen.pd()

for movement in range(100):
    brenda.forward(randint(1, 5))
    pickle.forward(randint(1, 5))
    karen.forward(randint(1, 5))
    marie.forward(randint(1, 5))

input("Press Enter to close")
