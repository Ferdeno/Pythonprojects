from tkinter import *


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=1
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def clicked_reset():
    global reps
    reps=1
    head_label.config(text="Timer")
    checkbox_label.config(text="")
    canvas.itemconfig(timer_count,text=f"00:00")
    window.after_cancel(timer)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def clicked_start():
    global reps
    if reps==1 or reps==3 or reps==5 or reps==7:
        head_label.config(text="Work")
        count_down(WORK_MIN*60)
    elif reps==2 or reps==4 or reps==6:
        head_label.config(text="Break")
        count_down(SHORT_BREAK_MIN*60)
    elif reps==8:
        head_label.config(text="F-Break")
        count_down(temp=LONG_BREAK_MIN*60)
    else:
        pass
    reps+=1
        

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    minute=count//60
    seconds=count%60
    if len(str(seconds))==1:
        seconds="0"+str(seconds)
    if len(str(minute))==1:
        minute="0"+str(minute)
    canvas.itemconfig(timer_count,text=f"{minute}:{seconds}")
    if count>0: 
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        
        if reps==3:
            checkbox_label.config(text="✔")
        elif reps==5:
            checkbox_label.config(text="✔✔")
        elif reps==7:
            checkbox_label.config(text="✔✔✔")
        clicked_start()

        
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("pomodora timer")#pomodoro is tomato in italian 
window.config(padx=100,pady=50,bg=GREEN)
window.minsize(width=500,height=500)



head_label=Label(text="Timer",font=(FONT_NAME,35,"bold"),fg=RED,bg=GREEN)
head_label.grid(column=1,row=1)


canvas=Canvas(width=200,height=224,bg=GREEN,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_count=canvas.create_text(100,127,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=2)


start=Button(text="START",command=clicked_start)
start.grid(column=0,row=3)

checkbox_label=Label(bg=GREEN,fg=RED,font=(FONT_NAME,25,"bold"))
checkbox_label.grid(column=1,row=4)

reset=Button(text="RESET",command=clicked_reset)
reset.grid(column=3,row=3)


window.mainloop()