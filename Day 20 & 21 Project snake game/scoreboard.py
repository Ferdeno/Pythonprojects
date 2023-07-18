from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align="center", font=("Arial", 24, "normal"))
