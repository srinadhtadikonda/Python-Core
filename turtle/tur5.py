#creating a drawing board
from turtle import * 
title("My Application")

bgcolor("red")
shape("turtle")
shapesize(3)
color("yellow")
pencolor("green")
i=1
while(i<10):
 forward(100)
 left(90)
 forward(40)
 left(30)
 forward(40)
 left(190)
 forward(80)
 left(90)
 i=i+1
done()
