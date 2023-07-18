from turtle import Screen,Turtle

class Paddle(Turtle):
    def __init__(self,a,b):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape('square')
        self.setheading(90)
        self.shapesize(1, 5)
        self.goto(a, b)

    def up(self):
        self.forward(20)
    def down(self):
        self.backward(20)


