import turtle

# Set up the turtle
screen = turtle.Screen()
screen.bgcolor("white")  # Set the background color

pen = turtle.Turtle()
pen.speed(0)  # Set the fastest drawing speed

# Function to draw a square
def draw_square(size, color):
    pen.begin_fill()
    pen.fillcolor(color)
    for _ in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()

# Draw the chessboard
square_size = 30  # Size of each square
num_squares = 8  # Number of squares per side

for i in range(num_squares):
    for j in range(num_squares):
        if (i + j) % 2 == 0:
            draw_square(square_size, "white")
        else:
            draw_square(square_size, "black")
        pen.forward(square_size)
    pen.backward(square_size * num_squares)
    pen.right(90)
    pen.forward(square_size)
    pen.left(90)

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()
