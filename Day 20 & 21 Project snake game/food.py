from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.color("blue")
        self.speed("fastest")
        self.reset_food()

    def reset_food(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))