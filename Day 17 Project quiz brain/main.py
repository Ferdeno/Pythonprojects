from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[Question(question_data[i]['text'],question_data[i]['answer']) for i in range(len(question_data))]
question_number=1
current_score=0
for i in question_bank:
    obj=QuizBrain(i,question_number,current_score)
    if obj.game():
        current_score+=1
    question_number+=1

print(f"\nYour Quiz is completed... Your final score is {current_score}/{question_number-1}")