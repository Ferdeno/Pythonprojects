class QuizBrain:
    def __init__(self,question_list,question_number,current_score):
        self.question_list=question_list
        self.question_number=question_number
        self.current_score=current_score
    def game(self):
        a=input(f"Q{self.question_number}): {self.question_list.text} True or False : ")
        if a!=self.question_list.ans:
            print(f"It's a wrong answer \nThe correct answer is {self.question_list.ans} \nYour current score is {self.current_score}/{self.question_number}")
            return False
        else:
            self.current_score+=1
            print(f"You got it right!\nThe correct answer is {self.question_list.ans} \nYour current score is {self.current_score}/{self.question_number}")
            return True