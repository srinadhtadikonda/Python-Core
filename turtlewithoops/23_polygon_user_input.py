import turtle

t = turtle.Turtle()

n = int(input("Enter number of sides: "))
length = int(input("Enter side length: "))

angle = 360 / n

for i in range(n):
    t.forward(length)
    t.right(angle)

turtle.done()
