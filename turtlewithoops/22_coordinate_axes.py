import turtle

t = turtle.Turtle()

# X-axis
t.penup()
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)

# Y-axis
t.penup()
t.goto(0, -300)
t.pendown()
t.goto(0, 300)

turtle.done()
