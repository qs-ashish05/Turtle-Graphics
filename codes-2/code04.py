# Write a program to draw a sun.

import turtle

# Create a turtle object
pen = turtle.Turtle()

# Draw the sun
pen.color("yellow")
pen.begin_fill()

for i in range(12):
    pen.forward(100)  # Draw a sunray
    pen.backward(100)  # Move back to the center
    pen.right(30)  # Turn the turtle 30 degrees

pen.end_fill()

# Draw the sun's center
pen.color("yellow")
pen.begin_fill()
pen.circle(10)  # Draw a circle for the sun's center
pen.end_fill()

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()
