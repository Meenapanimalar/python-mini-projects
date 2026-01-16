import random
from turtle import Turtle,Screen

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()


colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "cyan", "magenta"]


def shape(sides,color_of_turtle):
    turtle.color(color_of_turtle)
    for i in range(sides):
        turtle.forward(100)
        turtle.right(360 / sides)


for i in range (3,11):
    shape(i,random.choice(colors))





