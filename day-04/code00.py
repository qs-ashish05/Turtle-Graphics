# drwa sun 
import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Set the background color

sun_turtle = turtle.Turtle()
sun_turtle.color("yellow")  # Set the color of the sun
sun_turtle.speed(5)

# Draw the sun
for i in range(36):
    sun_turtle.forward(100)  # Draw a ray
    sun_turtle.backward(100)  # Move back to the center
    sun_turtle.left(10)  # Turn 30 degrees

# Draw the center of the sun
sun_turtle.begin_fill()
"""
new_y_position = sun_turtle.ycor() - 10
sun_turtle.sety(new_y_position)
sun_turtle.circle(20)  # Draw a small circle for the center
sun_turtle.end_fill()
"""
sun_turtle.circle(20)  # Draw a small circle for the center
sun_turtle.end_fill()

# Hide the turtle and display the result
sun_turtle.hideturtle()
turtle.done()




