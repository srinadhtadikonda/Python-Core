import turtle

t = turtle.Turtle()
colors = ["red", "blue", "green", "orange", "purple"]

for i in range(80):
    t.color(colors[i % 5])
    t.forward(i * 3)
    t.right(91)

turtle.done()
