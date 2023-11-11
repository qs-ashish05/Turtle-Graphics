# Draw B 

import turtle

# Create a turtle object
pen = turtle.Turtle()

# Draw the letter "B"
pen.left(90)  # Turn the turtle to point upwards
pen.forward(100)  # Draw the vertical line
pen.right(90)  # Turn the turtle to point right
pen.circle(-25, 180)  # Draw the top curve
pen.right(180)  # Turn the turtle around
pen.circle(-25, 180)  # Draw the bottom curve

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()
