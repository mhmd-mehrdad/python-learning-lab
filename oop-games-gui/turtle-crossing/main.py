import time
from turtle import Screen
from player import Player
from car_manager import Car
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = Car()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.player_move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()

    #Detect collision with the cars
    for c in car.cars:
        if c.distance(player) < 20:
            print("RIDI")
            scoreboard.game_over_scoreboard()
            game_is_on = False

    if player.ycor() > 280:
        print("won")
        player.reposition()
        car.increase_speed_car()
        scoreboard.level += 1
        scoreboard.update_scoreboard()

screen.exitonclick()
