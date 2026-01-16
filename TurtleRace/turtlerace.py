import random

from turtle import Turtle,Screen


colors = ["red", "blue", "green", "purple", "orange"]
y_positions = [100,50,0,-50,-100]
is_race_on = True

turtle_objects= []
for name in colors:
    t = Turtle()
    t.name = name
    t.penup()
    turtle_objects.append(t)


for index, turt in enumerate(turtle_objects):
    turt.color(colors[index])

screen = Screen()
screen.setup(width=500,height=400)
user_color = screen.textinput(title="Welcome to turtle race!!",prompt="select your turtle")

for i in range(len(turtle_objects)):
    turtle_objects[i].goto(x=-230,y=y_positions[i])



right_wall = screen.window_width() / 2

found_winner = False

while is_race_on:
    for turt in turtle_objects:
        turt.forward(random.randint(0,10))

        if turt.xcor() > right_wall - 10:
            winner_color = turt.color()[0]
            if user_color == winner_color:
                print(f"{winner_color} won the race")
            else:
                print(f"you lose! {winner_color} is the winner")
            found_winner = True
            is_race_on = False
            break

    if found_winner:
        break

screen.bye()
