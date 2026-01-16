import random
from turtle import Turtle,Screen

turtle = Turtle()
turtle.shape("turtle")
screen = Screen()
screen.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    rgb_color = (r,g,b)
    return rgb_color


direction = [0,0,90,180,270]
turtle.pensize(10)
turtle.speed("fastest")
for i in range(100):
    turtle.forward(25)
    turtle.left(random.choice(direction))
    turtle.color(random_color())
    turtle.forward(25)
    turtle.right(random.choice(direction))
    turtle.color(random_color())





