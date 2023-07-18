from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time


s=Screen()
s.screensize(bg='black')
s.setup(width=640,height=480)
s.title("Pong Game")
s.tracer(0)


r_paddle=Paddle(290,0)
l_paddle=Paddle(-295,0)
ball=Ball()
game=True


s.onkey(r_paddle.up,'Up')
s.onkey(r_paddle.down,'Down')
s.onkey(l_paddle.up,'w')
s.onkey(l_paddle.down,'s')

s.listen()

score=Score()
while game:
    time.sleep(0.1)
    s.update()
    ball.move()
    # collision with the wall
    if ball.ycor()>220 or ball.ycor()<-220:
        ball.bounce_y()


    # collision with the paddle
    if ball.distance(r_paddle)<40 and ball.xcor()>90 or ball.distance(l_paddle)<40 and ball.xcor()<-90:
        ball.bounce_x()

    # collision with the right wall
    if ball.xcor()>300 :
        ball.reset_position()
        score.l_score+=1


    # collision with left wall
    if ball.xcor()<-300:
        ball.reset_position()
        score.r_score+=1
    score.update()


s.exitonclick()

