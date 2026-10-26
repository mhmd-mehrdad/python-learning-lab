from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color("red")
        self.goto(0, 200)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"{self.score}/50 States Correct",
            align="center",
            font=("Arial", 18, "bold")
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()