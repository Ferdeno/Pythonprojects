# import colorgram
# rgb_colours=[]
# colours=colorgram.extract("IMG_20220227_113239.jpg",20)
# for c in colours:
#     r=c.rgb.r
#     g=c.rgb.g
#     b=c.rgb.b
#     n=(r,g,b)
#     rgb_colours.append(n)
# print(rgb_colours)
#the above code is to extract the rgb colours from the image
rgb=[(207, 217, 226), (247, 227, 190), (203, 161, 117), (141, 176, 202), (242, 196, 125), (126, 94, 76), (246, 242, 245), (219, 224, 222), (78, 88, 105), (43, 50, 64), (97, 79, 84), (161, 144, 71), (164, 113, 100), (60, 50, 54), (54, 61, 78), (59, 52, 41), (166, 146, 151), (225, 180, 163), (166, 194, 219), (74, 78, 33)]
import turtle as t
import random as r
t.shape("turtle")
t.penup()
t.colormode(255)
t.speed(1000)
t.setposition(-180,-170)
for i in range(10):
    for j in range(10):
        t.dot(20,r.choice(rgb))
        t.forward(50)
    t.backward(500)
    t.left(90)
    t.forward(50)
    t.right(90)
t.hideturtle()
t.exitonclick()