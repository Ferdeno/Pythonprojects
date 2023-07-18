# import random as r
# a=r.choice([1,2,3])
# print(a)

# import heroes
# print(heroes.gen())

import turtle
t=turtle.Turtle()
t.penup()
t.backward(200)
for i in range(15):
    t.forward(15)
    t.penup()
    t.forward(15)
    t.pendown()
turtle.exitonclick()
