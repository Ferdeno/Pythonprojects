# update is adding the highscore in this project

from turtle import Screen,Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

s=Screen()
s.setup(width=600,height=600)
s.bgcolor('black')
s.title("snake game")
s.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()
s.listen()
s.onkey(snake.up, 'Up')
s.onkey(snake.down, 'Down')
s.onkey(snake.left, 'Left')
s.onkey(snake.right, 'Right')

game=True
while game:
    s.update()
    time.sleep(0.1)

    snake.move()

    #collision with the food
    if snake.head.distance(food)<15:
        food.reset_food()
        snake.extend()
        scoreboard.score+=1
        scoreboard.update_score()

    #collision with the wall

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        # game=False
        scoreboard.update_highscore()
        snake.reset()

    #collision with the body method 1
    # flag=0
    # for box in snake.boxes:
    #     # if snake.head==box:#check for the first time when the game is on
    #     #     pass
    #     if snake.head.distance(box)<10 :
    #         if flag:
    #             game=False
    #         flag=1

    #collision with the body method 2

    for box in snake.boxes[1:]:#this eliminates the head of the box
        if snake.head.distance(box) < 10:
            # game = False
            snake.reset()
            scoreboard.update_highscore()


# t=Turtle()
# t.color("white")
# t.write(f"Game Over",align="center",font=("Arial", 24, "normal"))








# # box_1=Turtle(shape='square')
# # box_1.color('white')
# #
# # box_2=Turtle(shape='square')
# # box_2.color('white')
# # box_2.goto(-20,0)
# #
# # box_3=Turtle(shape='square')
# # box_3.color('white')
# # box_3.goto(-40,0)

s.exitonclick()