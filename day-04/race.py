import turtle
import random


# Initialize screen
screen = turtle.Screen()
screen.setup(width=400, height=400)

turtle.speed(1)
red = turtle.Turtle()
blue = turtle.Turtle()

red.fillcolor('Red')
red.shape("turtle")
blue.fillcolor('blue')
blue.shape("square")

blue.penup()
blue.goto(0, 40)
blue.pendown()

count = 0
while True:
    dis = random.randint(0,10)
    if count % 2 ==0:
        red.forward(dis)
        xcor = red.xcor()
        if xcor >= 200:
            print("Red is the winner ")
            break
    else:
        blue.forward(dis)
        xcor = blue.xcor()
        if xcor >= 200:
            print("Blue is the winner ")
            break
    count+=1


turtle.done()