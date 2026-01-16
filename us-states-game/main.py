import turtle
import pandas as pd

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_is_on = True

while game_is_on:
    answer_state = screen.textinput(title="USA states",prompt="Enter the US states")
    answer_state = answer_state.title()
    states_data = pd.read_csv("50_states.csv")

    if answer_state in states_data["state"].values:
        correct_row = states_data[states_data["state"] == answer_state]
        t1 = turtle.Turtle()
        t1.penup()
        t1.hideturtle()
        t1.goto(correct_row["x"].item(), correct_row["y"].item())
        t1.write(answer_state)

    else:
        game_is_on = False
        screen.bye()


print(correct_row)


# if answer_state in states_data["state"].values:
#     state = turtle.Turtle()
#     state.goto(states_data["state"])


screen.exitonclick()