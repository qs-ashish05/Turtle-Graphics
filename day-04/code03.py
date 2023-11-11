# first animation
import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")

# Define the animation loop
for _ in range(100):
    my_turtle.forward(100)  # Move the turtle forward by 10 units
    my_turtle.left(90)
    screen.update()  # Update the screen
    turtle.delay(50)  # Add a small delay for smooth animation

turtle.done()
