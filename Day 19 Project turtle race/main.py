from turtle import Turtle,Screen
from random import randint

s=Screen()

user_input=s.textinput(title="Make your bet ",prompt="Enter a color of the turtle : ")

color=["red","orange","yellow","green","blue","violet"]
all_t=[]
x=-300
y=150
for i in range(0,6):
    t=Turtle(shape="turtle")
    t.penup()
    t.color(color[i])
    t.goto(x,y)
    y-=50
    all_t.append(t)
game=False
if user_input in color:
    game=True
else:
    print("Invalid color")

while game:
    for i in all_t:
        if i.xcor()>280:#xcor returns the x coordinates
            game=False
            winner=i.pencolor()
            if winner==user_input:
                print(f"Your guess {user_input} is correct ")
            else:
                print(f"your guess {user_input} is wrong and the winner is {winner}")
        r=randint(0,10)
        i.forward(r)
    # def position_turtle(x,y,c):
    # red_t=Turtle(shape="turtle")
    # red_t.color('red')
    # red_t.penup()
    # red_t.goto(x=-300,y=150)
    #
    # orange_t=Turtle(shape="turtle")
    # orange_t.color('orange')
    # orange_t.penup()
    # orange_t.goto(x=-300,y=100)
    #
    # yellow_t=Turtle(shape='turtle')
    # yellow_t.color('yellow')
    # yellow_t.penup()
    # yellow_t.goto(x=-300,y=50)
    #
    # green_t=Turtle(shape='turtle')
    # green_t.color('green')
    # green_t.penup()
    # green_t.goto(x=-300,y=0)
    #
    # blue_t=Turtle(shape='turtle')
    # blue_t.color('blue')
    # blue_t.penup()
    # blue_t.goto(x=-300,y=-50)
    #
    # violet_t=Turtle(shape='turtle')
    # violet_t.color('violet')
    # violet_t.penup()
    # violet_t.goto(x=-300,y=-100)

s.exitonclick()