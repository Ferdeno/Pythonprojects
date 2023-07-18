from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class Quizinterface:
    
    def __init__(self,quiz_brain : QuizBrain):
        self.quiz=quiz_brain
        
    
        self.window=Tk()
        self.window.title("Quiz")
        self.window.minsize(width=350,height=600)
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.score_board=Label(text="Score : 0",fg="white",bg=THEME_COLOR)
        self.score_board.grid(row=0,column=2)

        self.canvas=Canvas(width=300,height=250,bg="white")
        self.text_area=self.canvas.create_text(150,125,text="Start",width=270,fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)

        #pady is used for the canvas padding
        true_img=PhotoImage(file="./images/true.png")
        self.true_button=Button(image=true_img,highlightthickness=0,command=self.correct_check)
        self.true_button.grid(row=2,column=1)

        false_img=PhotoImage(file="./images/false.png")
        self.wrong_button=Button(image=false_img,highlightthickness=0,command=self.wrong_check)
        self.wrong_button.grid(row=2,column=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_board.config(text=f"Score : {self.quiz.score}")
            q_text=self.quiz.next_question()
            self.canvas.itemconfig(self.text_area,text=q_text)
        else:
            self.canvas.itemconfig(self.text_area,text="End of the Question!!!")
            self.true_button.config(state="disabled")
            self.wrong_button.config(state="disabled")


    def correct_check(self):
        is_right=self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def wrong_check(self):
        self.give_feedback(self.quiz.check_answer("false"))

    
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)
