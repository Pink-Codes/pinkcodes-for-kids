# SpiralMyName.py
import turtle
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red" , "pink" , "purple" , "blue" , "green" , "yellow", "white"]
your_name = turtle.textinput("What is your name", "Please enter your name:")
for x in range(70):
    t.pencolor( colors[ x % 7 ] )
    t.penup()
    t.forward( x * 7 )
    t.pendown()
    t.write(your_name, font =("Cursive",int( (x + 7) / 7),"bold"))
    t.left(96);
