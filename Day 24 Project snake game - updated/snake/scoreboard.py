from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("highscore.txt") as highscore_text:
            self.highscore=int(highscore_text.read())
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.color("white")
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score : {self.score} HighScore : {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def update_highscore(self):
        if self.score>self.highscore:
            self.highscore=self.score
            with open("highscore.txt",mode="w") as highsocre_text:
                highsocre_text.write(str(self.highscore))
        self.score=0
        self.update_score()




