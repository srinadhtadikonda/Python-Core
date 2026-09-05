import turtle

t = turtle.Turtle()

# Trunk
t.color("brown")
t.width(20)
t.forward(100)

# Leaves
t.width(1)
t.color("green")
t.begin_fill()
t.circle(60)
t.end_fill()

turtle.done()
