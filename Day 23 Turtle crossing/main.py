import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=850, height=700)
screen.tracer(0)

c=CarManager()

p=Player()

screen.onkey(p.move,'Up')
screen.listen()

score=Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    c.create_car()
    c.move_car()

    #turtle crosses the road
    if p.ycor()>280:
        p.restart()
        c.move_increment+=1
        score.SCORE+=1
        score.write_score()

    # collide with the car
    for car in c.all_cars:
        if car.distance(p)<20:
            game_is_on=False
            score.game_over()


    screen.update()


screen.exitonclick()