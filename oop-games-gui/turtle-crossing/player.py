from turtle import Turtle

import car_manager
from car_manager import Car

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reposition()
        self.setheading(90)

    def player_move(self):
        self.forward(MOVE_DISTANCE)

    def reposition(self):
        self.goto(STARTING_POSITION)