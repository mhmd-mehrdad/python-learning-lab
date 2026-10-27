import random
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=500, height=400)
the_bet = screen.textinput(title="Make a bet", prompt="Which turtle do you want to bet on ? ")

colors = ["purple", "blue", "green", "yellow", "orange", "red"]
all_turtles = []
is_race_on = False

x_position = -230
y_position = -130
for contestor_index in range(0, 6):
    mamad = Turtle(shape="turtle")
    mamad.color(colors[contestor_index])
    mamad.penup()
    mamad.goto(x=x_position, y=y_position)
    all_turtles.append(mamad)
    y_position+=50

if the_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            print(winning_color)
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
