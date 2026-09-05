import turtle

t = turtle.Turtle()

# Face
t.circle(100)

# Left eye
t.penup()
t.goto(-35, 120)
t.pendown()
t.dot(15)

# Right eye
t.penup()
t.goto(35, 120)
t.pendown()
t.dot(15)

# Smile
t.penup()
t.goto(-40, 70)
t.setheading(-60)
t.pendown()
t.circle(50, 120)

turtle.done()
