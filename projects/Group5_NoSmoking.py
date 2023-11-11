import turtle
t = turtle.Turtle()


t.speed(0) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

t.left(120)
t.forward(20)
t.right(90)
t.forward(90)
t.right(90)
t.forward(20)
t.right(180)
t.forward(20)
t.right(90)

t.fillcolor("brown")
t.begin_fill() 
t.forward(30)
t.right(90)
t.forward(20)
t.right(90)
t.forward(30)
t.end_fill() 
t.forward(90)
t.fillcolor("grey")
t.begin_fill()


t.penup()


t.goto(0,120)
t.pendown()
t.pensize(30)
t.color("red")
t.circle(100)
t.penup()
t.goto(0,110)
t.right(260)
t.pendown()
t.forward(180)
t.penup()
t.goto(0,-100)
t.right(130)
t.forward(160)
font_setup=('Avoid',24,'bold')
t.write("Be brighter put",font=font_setup)
t.left(80)
t.forward(40)
t.write("down the lighter",font=font_setup)



