# task to students : 
# draw a square/ rectangle with all sides having different colors

# solutions
import turtle
pen = turtle.Turtle()
pen.speed(1)   

pen.penup()
pen.goto(100, 100)
pen.pendown()

pen.pencolor('red')         # try with different colors
pen.pensize(10)             # try with different pensizes

pen.goto(-100, 100)
pen.pencolor('blue')
pen.goto(-100, -100)
pen.pencolor('yellow')
pen.goto(100, -100)
pen.pencolor('pink')
pen.goto(100, 100)

turtle.done()

# if you did any mistake while writing the collor name you will get an error sying "bad color string: yello" 