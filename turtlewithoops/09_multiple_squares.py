import turtle

t = turtle.Turtle()

for i in range(20):
    for j in range(4):
        t.forward(100)
        t.right(90)
    t.right(18)

turtle.done()
