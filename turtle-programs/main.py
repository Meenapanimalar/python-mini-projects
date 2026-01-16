from turtle import Turtle,Screen

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()
turtle.color("aquamarine")
# for j in range(4):


for i in range(25):

    turtle.penup()
    turtle.forward(4)
    turtle.pendown()
    turtle.forward(4)
screen.exitonclick()


