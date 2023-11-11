# drawing infinite squares 
import turtle
##

turtle.speed(1)
count = 0
while(True):
    turtle.forward(100)
    turtle.left(90)
    count=count+1
    if count == 4:
        turtle.clear()
        count = 0
    


