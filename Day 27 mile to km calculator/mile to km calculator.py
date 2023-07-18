from tkinter import *

window=Tk()
window.title("Mile to km conventer")
window.minsize(width=400,height=300)
window.config(padx=30,pady=30)

entry_miles_number=Entry(width=5)
entry_miles_number.grid(column=1,row=1)
label_miles=Label(text="Miles")
label_miles.grid(column=2,row=1)

label_km_number=Label(text=0.0)
label_km_number.grid(column=1,row=3)

label_km=Label(text="KM")
label_km.grid(column=2,row=3)

def convert():
    label_km_number["text"]=1.60934*float(entry_miles_number.get())


calculate_button=Button(text="convert",command=convert)
calculate_button.grid(column=1,row=2)

window.mainloop()