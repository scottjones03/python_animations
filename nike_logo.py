import turtle

nikeTurtle = turtle.Turtle()
screen = turtle.Screen()
screen.setup(1000, 1000, 300, 0)

screen.bgcolor("white")
nikeTurtle.color("red")

nikeTurtle.penup()
nikeTurtle.setpos(-100, 0)
nikeTurtle.pendown()

def draw_tick(turtle: turtle.Turtle) -> None:
    turtle.begin_fill()

    turtle.left(180)
    turtle.circle(30, 200)
    turtle.forward(200)
    turtle.left(173)
    turtle.forward(190)
    turtle.circle(-18, 170)

    turtle.end_fill()

draw_tick(nikeTurtle)
turtle.done()