from turtle import Turtle,Screen

t=Turtle()
s=Screen()

def forward():
    t.forward(10)
def backward():
    t.backward(10)
def left():
    t.left(10)
def right():
    t.right(10)
def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()
s.listen()
s.onkey(key="w",fun=forward)
s.onkey(key="s",fun=backward)
s.onkey(key="a",fun=left)
s.onkey(key="d",fun=right)
s.onkey(key="c",fun=clear)
s.exitonclick()