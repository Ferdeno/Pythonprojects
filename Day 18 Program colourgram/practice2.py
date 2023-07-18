import turtle
import turtle as t


def draw(n):
    angle=360/n
    for _ in range(n):
        t.forward(100)
        t.right(angle)
n=3
for i in range(8):
   draw(n)
   n+=1
turtle.exitonclick()