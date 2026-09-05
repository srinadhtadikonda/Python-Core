import turtle
import random

screen = turtle.Screen()
screen.setup(600, 400)

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.color("red")
t2.color("blue")

t1.penup()
t2.penup()

t1.goto(-250, 50)
t2.goto(-250, -50)

while t1.xcor() < 250 and t2.xcor() < 250:
    t1.forward(random.randint(1, 10))
    t2.forward(random.randint(1, 10))

if t1.xcor() > t2.xcor():
    print("Red Turtle Wins!")
else:
    print("Blue Turtle Wins!")

turtle.done()
