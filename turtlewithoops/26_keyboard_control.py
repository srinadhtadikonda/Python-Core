import turtle

t = turtle.Turtle()

def move_forward():
    t.forward(20)

def move_backward():
    t.backward(20)

def turn_left():
    t.left(20)

def turn_right():
    t.right(20)

screen = turtle.Screen()
screen.listen()

screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.mainloop()
