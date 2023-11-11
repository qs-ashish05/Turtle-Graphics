import turtle
t = turtle.Turtle()


screen = turtle.Screen()
screen.bgcolor("red")

pen = turtle.Turtle()

pen.goto(0, -70)

pen.color("black")
pen.pensize(10)

t.delay(8)
pen.color('black')

pen.left(40)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.penup()
pen.forward(20)
pen.pendown()
pen.color("white")


pen.color("black")

pen.left(190)
pen.penup()
pen.circle(-30, extent = 40)
pen.pendown()
pen.right(60)
pen.forward(100)

pen.pensize(10)

pen.backward(100)
pen.left(100)
pen.circle(-30, extent = 40)
pen.right(60)
pen.forward(100)

pen.backward(105)
pen.left(100)
pen.circle(-30, extent = 40)
pen.right(60)
pen.forward(120)

pen.backward(120)
pen.left(100)
pen.circle(-30, extent = 40)
pen.right(60)
pen.forward(100)

pen.backward(105)
pen.left(100)
pen.circle(-30, extent = 40)
pen.right(60)
pen.forward(100)


pen.penup()
pen.goto(-17,121)
pen.right(100)

pen.pendown()
pen.forward(100)

pen.circle(-20,extent = 125)
pen.right(50)
pen.forward(80)
pen.left(20)

pen.circle(20,extent = 60)
pen.right(40)

pen.circle(20,extent = 20)
pen.forward(10)
pen.circle(20,extent = 60)
pen.right(40)
