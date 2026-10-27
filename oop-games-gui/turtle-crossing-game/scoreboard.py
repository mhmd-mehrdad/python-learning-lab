from turtle import Turtle

FONT = ("Aerial", 20, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-220, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"LEVEL = {self.level}", align="center", font=FONT)

    def game_over_scoreboard(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)