import turtle

t = turtle.Turtle()
t.width(5)

colors = ["blue", "black", "red"]
x = -120

for c in colors:
    t.penup()
    t.goto(x, 50)
    t.pendown()
    t.color(c)
    t.circle(50)
    x += 120

t.penup()
t.goto(-60, 0)
t.pendown()
t.color("yellow")
t.circle(50)

t.penup()
t.goto(60, 0)
t.pendown()
t.color("green")
t.circle(50)

turtle.done()
