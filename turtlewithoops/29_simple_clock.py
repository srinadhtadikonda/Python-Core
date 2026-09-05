import turtle

t = turtle.Turtle()

t.penup()
t.goto(0, -150)
t.pendown()
t.circle(150)

for i in range(12):
    t.penup()
    t.goto(0, 0)
    t.setheading(90 - i * 30)
    t.forward(120)
    t.pendown()
    t.forward(20)

turtle.done()
