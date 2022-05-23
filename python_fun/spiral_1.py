import turtle
import random


a = turtle.Turtle()
wn = turtle.Screen()
wn.screensize(50, 50, "white")
a.pencolor("red")
a.pensize(2)
a.speed(100000)
start = a.pos()
colors = ["red", "black", "blue", "yellow", "green"]
turning_factor = random.randint(10, 90)

for j in range(1000):
    a.pencolor(colors[random.randint(0, 3)])
    a.penup()
    a.setposition(start)
    a.pendown()
    size = random.randint(10, 50)
    angle_subtended= 0
    while (angle_subtended <= 360):
        a.forward(size)
        a.right(turning_factor)
        angle_subtended+=turning_factor

turtle.done()