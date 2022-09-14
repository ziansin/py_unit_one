# remember to use comments!
import turtle

turtle.speed(100)

for x in range(4):
    turtle.left(90)
    turtle.forward(100)
turtle.left(90)
turtle.penup()
turtle.forward(100)
turtle.left(-90)
turtle.pendown()
for x in range(2):
    turtle.left(120)
    turtle.forward(100)

turtle.exitonclick()