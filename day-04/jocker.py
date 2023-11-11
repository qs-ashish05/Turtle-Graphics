import turtle as t

# Set up the turtle
t.speed(1)
t.bgcolor("white")
t.title("Joker Face with Cone Cap")

# Draw Joker face
t.color("purple")
t.begin_fill()
t.circle(100)
t.end_fill()

# Draw eyes
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()

draw_eye(-30, 120)
draw_eye(30, 120)

# Draw smile
t.penup()
t.goto(-40, 80)
t.pendown()
t.color("red")
t.right(90)
t.circle(40, 180)

# Draw nose
t.penup()
t.goto(0, 100)
t.pendown()
t.color("red")
t.begin_fill()
t.circle(7)
t.end_fill()


# # Draw cone cap
# t.penup()
# t.goto(-50,50)
# t.pendown()
# t.color("green")
# t.begin_fill()
# t.goto(0, 200)
# t.goto(100, 100)
# t.end_fill()

# Hide the turtle and display the result
#t.hideturtle()
t.done()
