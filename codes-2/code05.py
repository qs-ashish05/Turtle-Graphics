import turtle

# Create a turtle
pen = turtle.Turtle()

pen.speed(2)
# Move the turtle to a specific position (100, 100)
pen.goto(100, 100)

# Draw a square
for _ in range(4):
    pen.forward(50)
    pen.right(90)

# Close the turtle graphics window when clicked
turtle.done()
