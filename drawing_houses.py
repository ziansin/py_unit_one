# remember to use comments!
import turtle
h = 0
turtle.speed(100)

def makeASquare(squarecolor):
    turtle.fillcolor(squarecolor)
    for x in range(4):
        turtle.left(90)
        turtle.forward(100)

def makeATriangle(color):
    turtle.fillcolor(color)
    for x in range(3):
        turtle.left(120)
        turtle.forward(100)

def drawAHouse():
    turtle.begin_fill()
    makeASquare("red")
    turtle.end_fill()
    turtle.begin_fill()
    turtle.left(90)
    turtle.penup()
    turtle.forward(100)
    turtle.left(-90)
    turtle.pendown()
    makeATriangle("blue")
    turtle.end_fill()

for x in range(4):
    turtle.pendown()
    drawAHouse()
    turtle.penup()
    h = h + 110
    turtle.goto(h,0)

turtle.exitonclick()