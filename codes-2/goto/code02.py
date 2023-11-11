import turtle
pen = turtle.Turtle()
pen.speed(1)   

pen.penup()
pen.goto(100, 100)
pen.pendown()

pen.pencolor('red')         # try with different colors
pen.pensize(50)             # try with different pensizes

pen.goto(-100, 100)
pen.goto(-100, -100)
pen.goto(100, -100)
pen.goto(100, 100)

turtle.done()