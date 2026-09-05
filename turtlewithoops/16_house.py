import turtle

t = turtle.Turtle()

# House body
for i in range(4):
    t.forward(150)
    t.right(90)

# Roof
t.left(45)
t.forward(106)
t.right(90)
t.forward(106)

turtle.done()
