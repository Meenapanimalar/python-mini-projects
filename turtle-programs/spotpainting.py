import random
import colorgram
from turtle import Turtle, Screen

# --- Setup ---
screen = Screen()
screen.colormode(255)
t = Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

# --- Extract colors ---
colors = colorgram.extract('hirst_painting.jpeg', 25)
hirst_colours = [tuple(c.rgb) for c in colors]

# --- Move turtle to starting point ---
t.setheading(225)
t.forward(300)
t.setheading(0)

# --- Draw 10x10 dots ---
for row in range(10):
    for col in range(10):
        t.dot(20, random.choice(hirst_colours))
        t.forward(50)
    # Move to next row
    t.setheading(90)
    t.forward(50)
    t.setheading(180)
    t.forward(500)
    t.setheading(0)

screen.exitonclick()
