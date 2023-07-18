from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 5


class CarManager(Turtle):
    def __init__(self):
        self.all_cars=[]
        self.move_increment=5




    def create_car(self):
        chance=random.randint(1,6)#this is to reduce the no of car
        if chance==3:
            new_car=Turtle('square')
            new_car.shapesize(stretch_wid=0.8,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            rand_y=random.randint(-280,240)
            new_car.goto(440,rand_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.forward(self.move_increment)