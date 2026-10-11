from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def left(self):
        self.setx(self.xcor() - 20)

    def right(self):
        self.setx(self.xcor() + 20)