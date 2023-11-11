# draw a sqaure and fill it with red color 

import turtle

screen = turtle.Screen()
screen.bgcolor("white")

pen = turtle.Turtle()

pen.color("red")
pen.begin_fill()

pen.fillcolor("Blue")    # execute the code without this logic
# then it wil use the color of pen itlsef to fill the region

for i in range(4):
    pen.forward(100)
    pen.left(90)

pen.end_fill()

turtle.done()
