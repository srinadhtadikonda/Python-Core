import turtle
import random

t = turtle.Turtle()
colors = ["red", "green", "blue", "orange", "purple", "yellow"]

for i in range(100):
    t.color(random.choice(colors))
    t.forward(random.randint(20, 100))
    t.right(random.randint(0, 360))

turtle.done()
