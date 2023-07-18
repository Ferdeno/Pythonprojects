import turtle as t
import random as r
# colour=["yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue", "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray", "white"]
t.colormode(255)
t.pensize(50)
t.speed(10)
a=[0,90,180,270]
for i in range(300):
    t.pencolor(r.randint(1,255),r.randint(1,255),r.randint(1,255))
    t.forward(10)
    t.setheading(r.choice(a))
t.exitonclick()