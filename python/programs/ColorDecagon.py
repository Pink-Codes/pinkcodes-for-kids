 # ColorDecagon.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 10
colors = [ "green" ,"orange", "yellow" , "blue" ,"pink" , "purple" , "white" ,"red" , "light pink" , "light blue" ] 
for x in range(100):
     t.pencolor(colors[x % sides ] )
     t.forward(x * 1 / sides + x)
     t.left(360 /sides + 1)
     t.width( x * sides / 100)
