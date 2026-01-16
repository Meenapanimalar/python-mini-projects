import random
from multiprocessing.context import set_spawning_popen
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




turtle.speed("fastest")

# for j in range(25):
#     for i in range(15):
#         turtle.forward(25)
#         turtle.right(25)
#     turtle.forward(15)
#     turtle.color(random_color())
print(turtle.heading()+10)
print(turtle.setheading(10))
def spirograp(circle_radius , size_of_gap):
    for i in range(int(360/size_of_gap)):
        turtle.circle(circle_radius)
        turtle.setheading(turtle.heading() + size_of_gap)
        turtle.color(random_color())

spirograp(200,1)


screen.exitonclick()


