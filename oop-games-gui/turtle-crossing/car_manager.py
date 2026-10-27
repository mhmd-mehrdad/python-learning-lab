from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

class Car:
    def __init__(self):
        self.cars = []
        self.pace = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            new = Turtle()
            new.penup()
            new.goto(x=280, y=random.randint(-250, 250))
            new.shape("square")
            new.color(random.choice(COLORS))
            new.shapesize(stretch_wid=1, stretch_len=2)
            self.cars.append(new)


    def move_car(self):
        for car in self.cars:
            car.backward(self.pace)

    def increase_speed_car(self):
        self.pace += MOVE_INCREMENT