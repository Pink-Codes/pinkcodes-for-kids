# ColorRubberBandBall.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 6
colors = [ "green" ,"orange", "yellow" , "blue" ,"pink" , "purple" , "white" ,"red" , "light pink" , "light blue" ] 
for x in range(180):
     t.pencolor(colors[x % sides ] )
     t.forward(x * 3 / sides + x)
     t.left(360 /sides + 91)
     t.width( x * sides / 100)
#     t.left(90)
