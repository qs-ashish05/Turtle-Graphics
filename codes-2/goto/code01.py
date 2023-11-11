import turtle

# in the previous code we are getting the square of side lenght 200 by 200

# but in the middle we are also getting the unwanted line 

# how  to remove that ?

# first use penup then go to the desired location use pendown and then draw it 

pen = turtle.Turtle()

pen.speed(1)   

pen.penup()
pen.goto(100, 100)
pen.pendown()    


pen.goto(-100, 100)
pen.goto(-100, -100)
pen.goto(100, -100)
pen.goto(100, 100)

turtle.done()