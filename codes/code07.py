# practice code shape 

import turtle
pen = turtle.Turtle()
pen.shape('turtle')

number_list = [1,2,3,4,5,6,7,8,9,10] 

pen.color("green") 
for number in number_list: 
    pen.forward(number*10) 
    pen.left(60)