import turtle

t = turtle.Turtle()
t.shape("turtle")

for i in range(36):
    t.forward(100)
    t.stamp()
    t.backward(100)
    t.right(10)

turtle.done()
