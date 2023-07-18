from higherorlowergameart import logo
from higherorlowergameart import vs
from higherorlowergamedata import data
import random,os

def display(dic):
    print(f"Name : {dic['name']} \nDescription : {dic['description']}\nCountry : {dic['country']}\n")

def check(dic1,dic2,option):
    if option==1 and dic1['follower_count'] > dic2['follower_count']:
        return True
    if option==2 and dic1['follower_count'] < dic2['follower_count']:
        return True
    return False

game_status=True
score=0
number1=random.randint(0,49)
number2=random.randint(0,49)
while game_status:
    print(f"{logo}\n")
    if score:
        print(f"\nYou're right!!! Current score : {score}\n")
    while number1==number2:
        number2=random.randint(0,49)
    print(f"Compare 1\n")
    display(data[number1])
    print(vs)
    print("Against 2\n")
    display(data[number2])
    option=int(input("\nGuess who has more followers 1 or 2 : "))
    if check(data[number1],data[number2],option):
        score+=1
        number1=number2
        os.system('cls')
    else:
        print(f"Sorry,that's wrong,Final score : {score}")
        game_status=False


    
