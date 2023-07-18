import turtle as t
import random as r
t.speed(1000)
t.colormode(255)
def draw_spirograph(size):
    for _ in range(int(360/size)):
        t.color(r.randint(1,255),r.randint(1,255),r.randint(1,255))
        t.circle(100)
        t.setheading(t.heading()+size)
draw_spirograph(12)
t.exitonclick()