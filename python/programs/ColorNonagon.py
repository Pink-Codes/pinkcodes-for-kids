# ColorNonagon.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 9
colors = [ "red" , "pink" , "blue" , "green" , "orange" , "white" , "purple" , "brown" , "yellow" ]
for x in range (120):
    t.pencolor(colors [x % sides ] )
    t.forward(x * 3 / sides + x)
    t.left(360/sides + 1)
    t.width(x*sides/100)
