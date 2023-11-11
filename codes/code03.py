# draw heart

import turtle

pen = turtle.Turtle()

# Move to the starting position
pen.penup()
pen.goto(0, -200)
pen.pendown()

# Draw the heart shape

pen.left(140)
pen.forward(224)
pen.circle(-112, 200)
pen.right(140)
pen.circle(-112, 200)
pen.forward(224)


# Hide the turtle
pen.hideturtle()

# Keep the window open
turtle.done()
