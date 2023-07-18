from turtle import Turtle

START_POSITION=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
class Snake():
    def __init__(self):
        self.boxes=[]
        self.create_snake()
        self.head=self.boxes[0]
    def create_snake(self):
        for positon in START_POSITION:
            self.add_boxes(positon)

    def add_boxes(self,position):
        new_box = Turtle(shape='square')
        new_box.color('white')
        new_box.penup()
        new_box.goto(position)
        self.boxes.append(new_box)

    def extend(self):#add new box when snake eats the food
        self.add_boxes(self.boxes[-1].position())

    def move(self):
        for i in range(len(self.boxes) - 1, 0, -1):
            x = self.boxes[i - 1].xcor()
            y = self.boxes[i - 1].ycor()
            self.boxes[i].goto(x, y)
        self.boxes[0].forward(MOVE_DISTANCE)


    def up(self):
        # head=self.boxes[0].heading()
        if self.head.heading()==0:
            self.boxes[0].left(90)
        elif self.head.heading()==180:
            self.boxes[0].right(90)

    def down(self):
        # head=self.boxes[0].heading()
        if self.head.heading()==0:
            self.boxes[0].right(90)
        elif self.head.heading()==180:
            self.boxes[0].left(90)

    def left(self):
        # head = self.boxes[0].heading()
        if self.head.heading() == 90:
            self.boxes[0].left(90)
        elif self.head.heading() == 270:
            self.boxes[0].right(90)

    def right(self):
        # head = self.boxes[0].heading()
        if self.head.heading() == 90:
            self.boxes[0].right(90)
        elif self.head.heading() == 270:
            self.boxes[0].left(90)


