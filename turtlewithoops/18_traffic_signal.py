import turtle

t = turtle.Turtle()
t.penup()
t.goto(0, 100)

colors = ["red", "yellow", "green"]

for c in colors:
    t.color(c)
    t.dot(60)
    t.backward(80)

turtle.done()
