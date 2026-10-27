import turtle

import colorgram
import random
from turtle import Turtle, Screen




turtle.colormode(255)
rgb_colors = [(219, 173, 124), (159, 180, 190), (134, 73, 53), (49, 102, 153), (118, 82, 93), (179, 140, 150), (41, 46, 65), (162, 104, 151), (126, 173, 114), (83, 96, 183), (67, 9, 27), (81, 133, 107), (231, 188, 138), (52, 62, 79), (195, 90, 72), (116, 43, 58), (60, 41, 28), (92, 144, 117), (70, 67, 52), (182, 187, 207), (211, 181, 189)]

mamad = Turtle()
mamad.shape("turtle")
mamad.speed(0)
mamad.color("green")


def draw_the_damn_dot():
    mamad.color(random.choice(rgb_colors))
    mamad.pendown()
    mamad.dot(20)
    mamad.penup()
    mamad.forward(50)

print(mamad.pos())
for _ in range(2):
    draw_the_damn_dot()


sc = Screen()
sc.exitonclick()