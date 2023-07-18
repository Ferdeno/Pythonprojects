from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def clicked_generate_password():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password=password_letters+password_symbols+password_numbers
    shuffle(password)
    password="".join(password)
    print(password)
    password_label_input.delete(0,END)
    password_label_input.insert(0,password)
    #this pyperclip.paste will automatically copy the passed parameter to the clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def clicked_add():
    website_input=website_label_input.get()
    email_input=email_label_input.get()
    password_input=password_label_input.get()
    if len(website_input)!=0 and len(password_input)!=0 and len(email_input)!=0:
        is_ok=messagebox.askokcancel(title=website_input,message=f"Email : {email_input}\nPassword : {password_input}\nSave?")
        if is_ok:
            with open("data.txt",'a') as file:
                file.writelines(f"{website_input} | {email_input} | {password_input}\n")
                website_label_input.delete(0,END)
                email_label_input.delete(0,END)
                email_label_input.insert(0,"@gmail.com")
                password_label_input.delete(0,END)
    else:
        messagebox.showerror(title="Error",message="Fields are missing!!!")

      
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
window.minsize(width=700,height=500)


canvas=Canvas(width=200,height=200)
canvas_img=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=canvas_img)
canvas.grid(row=0,column=1)


#LABELS
website_label=Label(text="Website : ")
website_label.grid(row=1,column=0)

email_label=Label(text="Email/Username : ")
email_label.grid(row=2,column=0)

password_label=Label(text="Password : ")
password_label.grid(row=3,column=0)


#INPUTS
website_label_input=Entry(width=35)
website_label_input.grid(row=1,column=1,columnspan=2)
website_label_input.focus()

email_label_input=Entry(width=35)
email_label_input.grid(row=2,column=1,columnspan=2)
email_label_input.insert(0,"@gmail.com")

password_label_input=Entry(width=25)
password_label_input.grid(row=3,column=1)


#BUTTONS
generate_password=Button(text="Generate Password",command=clicked_generate_password)
generate_password.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=clicked_add)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()


