# remember to use comments!
import turtle
h = -100
turtle.speed(100)

def drawAHouse(size, house_color, roof_color):
    turtle.begin_fill()
    turtle.fillcolor(house_color)
    for x in range(4):
        turtle.left(90)
        turtle.forward(size)
    turtle.end_fill()
    turtle.begin_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(size)
    turtle.left(-90)
    turtle.pendown()
    turtle.fillcolor(roof_color)
    for x in range(3):
        turtle.left(120)
        turtle.forward(size)
    turtle.end_fill()

turtle.penup()
turtle.goto(-400,-350)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("cyan")
for x in range(4):
    turtle.forward(1000)
    turtle.left(90)
turtle.end_fill()
turtle.penup()
turtle.goto(-200,-325)
turtle.pendown()
drawAHouse(100, "red", "blue")
turtle.penup()
h = h + 110
turtle.goto(h,-325)
turtle.pendown()
drawAHouse(120, "purple", "pink")
turtle.penup()
h = h + 110
turtle.goto(h,-325)
turtle.pendown()
drawAHouse(50, "green", "yellow")
turtle.penup()
h = h + 110
turtle.goto(h,-325)
turtle.forward(50)
turtle.pendown()
drawAHouse(100, "brown", "black")
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("yellow")
for x in range(120):
    turtle.forward(3)
    turtle.left(3)
turtle.end_fill()


turtle.exitonclick()