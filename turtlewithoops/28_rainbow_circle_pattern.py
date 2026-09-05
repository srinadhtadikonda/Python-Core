import turtle

t = turtle.Turtle()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
t.speed(0)

for i in range(100):
    t.color(colors[i % 6])
    t.circle(i)
    t.right(10)

turtle.done()
