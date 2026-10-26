import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

scoreboard = Scoreboard()

while scoreboard.score < 50:
    answer_state = screen.textinput(
        title="U.S. States Game",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        answer_state = "Exit"
    else:
        answer_state = answer_state.strip().title()

    if answer_state == "Exit":
        missing_states = []

        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states, columns=["state"])
        new_data.to_csv("states_to_learn.csv", index=False)
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)

        scoreboard.increase_score()

screen.mainloop()