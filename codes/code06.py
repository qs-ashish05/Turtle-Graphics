
import turtle

pen = turtle.Turtle()
pen.shape('turtle')

pen.penup()
pen.forward(50)

# Set the font size to 24 points (you can adjust this value as needed)
font_setup = ('Arial', 24, 'normal')  # Font family, font size, font style

pen.write("Aniket Gupta", font=font_setup)

pen.backward(50)
turtle.done()



