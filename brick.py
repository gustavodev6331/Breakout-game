from turtle import Turtle
import random

brick_color = ["white", "blue", "red", "green", "yellow", "cyan", "magenta"]
brick_size = [(1, 5), (1, 3), (1, 4), (1, 2)]


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color(random.choice(brick_color))
        self.turtlesize(*random.choice(brick_size))
        self.penup()
        self.goto(position)

