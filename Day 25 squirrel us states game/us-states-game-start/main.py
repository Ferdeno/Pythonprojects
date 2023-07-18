# turtle works only on gif format not in jpg

import turtle
import pandas

s=turtle.Screen()

s.title("Find US States")
s.addshape("blank_states_img.gif")# this will add the image in the turtle
turtle.shape("blank_states_img.gif")
# turtle.penup()
def mark_place(text,x,y):
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x,y)
    t.write(text.item())

data=pandas.read_csv("50_states.csv")
US_States=data.state.to_list()

guess_count=0
game =50
while guess_count<game :
    guess_state=s.textinput(title=f"{guess_count}/{game} USA",prompt="Guess the state : ")
    guess_state=guess_state.title()
    if guess_state=="Exit":
        break
    if guess_state in US_States:
        guess_count+=1
        temp=data[data.state==guess_state]
        mark_place(temp.state,int(temp.x),int(temp.y))
        US_States.remove(guess_state)

print("Missing states : ",US_States)


# def xy(x,y):
#     print(x,y)
#
# turtle.onscreenclick(xy)

# turtle.mainloop()
# turtle.mainloop() is used instead of s.exitonclick()
# s.exitonclick()