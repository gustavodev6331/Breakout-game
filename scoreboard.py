from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 300)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Points:{self.score}", align="center", font=("Courier", 26, "normal"))

    def increase_score(self):
        self.score += 10
        self.update()