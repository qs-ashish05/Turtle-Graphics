import turtle

pen = turtle.Turtle()

pen.speed(1)     # lower the value slowest the speed --> only allowed values are 1 to 5     

pen.goto(100, 100)

pen.goto(-100, 100)
pen.goto(-100, -100)
pen.goto(100, -100)
pen.goto(100, 100)


turtle.done()