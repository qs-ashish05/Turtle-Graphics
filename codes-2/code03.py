# code to draw star
import turtle
# Create a turtle object
pen = turtle.Turtle()

# Draw a star
for i in range(5):
    pen.forward(100)  # Move the turtle forward by 100 units
    pen.right(144)    # Turn the turtle right by 144 degrees

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()