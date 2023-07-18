from tkinter import *

window=Tk()
window.title("Vannakkam")
window.minsize(width=300,height=300)
window.config(padx=30,pady=30)#padding the window
# display data in screen
label=Label(text="vanga sapadhalam",font=("Arial",25))
# label.pack() this will show the data on the output screen
label.grid(column=0,row=0)
label["text"]="ponga"#changes the argument 
label.config(text="vaanga",font=(50))#changes multiple arguments


def button_clicked():
    i=input.get()
    label["text"]=i
    print("Button is pressed")

button1=Button(text="press 1",command=button_clicked)
button1.grid(column=1,row=1)
button2=Button(text="press 2")
button2.grid(column=3,row=0)
input=Entry()
input.grid(column=4,row=3)
 
window.mainloop()

# def singleasterisk(*args):
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# singleasterisk(2,3,4,5,3,3,4,4)

# def doubleasterisk(**kwargs):

#     print(kwargs["a"]+kwargs["b"])

# doubleasterisk(a=4,b=3)