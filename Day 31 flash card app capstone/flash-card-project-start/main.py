from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- BUTTON CLICKED ------------------------------- #
try:
    data=pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv("./data/french_words.csv")
new_data=data.to_dict("records")

current_card={}

def clicked_button():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(new_data)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_words,text=current_card["French"],fill="black")
    canvas.itemconfig(canvas_card_colour,image=canvas_img_front)
    flip_timer=window.after(3000,func=flip_cards)
    
# ---------------------------- FLIP CARD ------------------------------- #

def flip_cards():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_words,text=current_card["English"],fill="white")
    canvas.itemconfig(canvas_card_colour,image=canvas_img_back)


# ---------------------------- CARD KNOWN ------------------------------- #

def card_known():
    new_data.remove(current_card)
    data=pandas.DataFrame(new_data)
    data.to_csv("data/words_to_learn.csv",index=False)
    clicked_button()

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
window.minsize(width=800,height=600)

flip_timer=window.after(3000,func=flip_cards)

canvas=Canvas(width=800,height=526)

canvas_img_front=PhotoImage(file=".\images\card_front.png")
canvas_img_back=PhotoImage(file=".\images\card_back.png")
canvas_card_colour=canvas.create_image(400,263,image=canvas_img_front)

card_title=canvas.create_text(400,153,text="Title",font=("Ariel",40,"italic"))
card_words=canvas.create_text(400,303,text="Words",font=("Ariel",40,"bold"))

canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

#BUTTON 
wrong_img=PhotoImage(file=".\images\wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,command=clicked_button)
wrong_button.grid(row=1,column=0,columnspan=1)

correct_img=PhotoImage(file="images/right.png")
correct_button=Button(image=correct_img,highlightthickness=0,command=card_known)
correct_button.grid(row=1,column=1,columnspan=2)

clicked_button()

window.mainloop()
