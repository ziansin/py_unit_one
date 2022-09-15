import turtle

turtle.speed(100)

#starting position
turtle.penup()
turtle.goto(-150,-150)
turtle.pendown()
def makeAnOctagon(color):
#to make the shortcut for creating octagons
    turtle.pencolor(color)
    turtle.fillcolor(color)
    for x in range(8):
        turtle.forward(50)
        turtle.left(45)

#putting end_fill will reset the color so that it can be changed
#creation of the four octagons, starting with the red octagon
turtle.begin_fill()
makeAnOctagon("red")
turtle.end_fill()
#second octagon (blue)
turtle.penup()
turtle.goto(50,-150)
turtle.pendown()
turtle.begin_fill()
makeAnOctagon("blue")
turtle.end_fill()
#third octagon (purple)
turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.begin_fill()
makeAnOctagon("purple")
turtle.end_fill()
#fourth and final octagon (yellow)
turtle.penup()
turtle.goto(50,50)
turtle.pendown()
turtle.begin_fill()
makeAnOctagon("yellow")
turtle.end_fill()

turtle.exitonclick()