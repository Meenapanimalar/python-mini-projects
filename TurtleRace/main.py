import turtle
from turtle import Turtle,Screen

tom = Turtle()
screen = Screen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def move_left():

    turtle.right(10)
def move_right():
    turtle.left(10)

def clear_screen():
    turtle.reset()

screen.listen()
screen.onkey(fun=move_forward , key= "w")
screen.onkey(fun=move_backward , key= "s")
screen.onkey(fun=move_left , key= "a")
screen.onkey(fun=move_right, key= "d")
screen.onkey(fun=clear_screen, key= "c")
screen.exitonclick()
