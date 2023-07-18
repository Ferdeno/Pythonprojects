from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-390,280)
        self.hideturtle()
        self.SCORE = 1
        self.update_scoreboard()
    def update_scoreboard(self):
        self.write(f"LEVEL : {self.SCORE}", align="left", font=FONT)

    def write_score(self):
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(-50,280)
        self.write("GAME OVER ", align="left", font=FONT)

