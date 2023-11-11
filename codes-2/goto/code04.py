# Draw a pentagon

import turtle

pen = turtle.Turtle()

pen.speed(1)

pen.penup()
#pen.setpos(100,100)
pen.goto(100,100)
pen.pendown()

for i in range(5):
    pen.forward(100)
    pen.left(72)      # ech interior angle of pentagon is of 108 

turtle.done()

# pen.setpos() works similar to that of pen.goto()
