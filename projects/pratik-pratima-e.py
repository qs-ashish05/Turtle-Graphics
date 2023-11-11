import turtle
t = turtle.Turtle()
t.speed(0)
colors=('red','purple','green','blue','orange','yellow')
s=turtle.Screen()
s.bgcolor('black')
for x in range(500):
  t.pencolor(colors[x%6])
  t.width(x//100+1)
  t.forward(x)
  t.left(96)
