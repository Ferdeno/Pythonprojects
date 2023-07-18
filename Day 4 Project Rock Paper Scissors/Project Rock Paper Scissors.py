rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
n=int(input("1.Stone\n2.Paper\n3.Scissors\nEnter your choice : "))
c=random.randint(1,3)
if n==1 and c==3:
    print("\nYour choice \n",rock,"\nComputer choice \n",scissors,"\nYou Win...")
elif(n==2 and c==1):
    print("\nYour choice \n",paper,"\nComputer choice \n",rock,"\nYou Win...")
elif n==3 and c==2:
    print("\nYour choice \n",scissors,"\nComputer choice \n",paper,"\nYou Win...")
elif n==1 and c==1:
    print("\nYour choice \n",rock,"\nComputer choice \n",rock,"\nMatch Draw...")
elif n==2 and c==2:
    print("\nYour choice \n",paper,"\nComputer choice \n",paper,"\nMatch Draw...")
elif n==3 and c==3:
    print("\nYour choice \n",scissors,"\nComputer choice \n",scissors,"\nMatch Draw...")
elif n==1 and c==2:
    print("\nYour choice \n",rock,"\nComputer choice \n",paper,"\nYou lose...")
elif n==2 and c==3:
    print("\nYour choice \n",paper,"\nComputer choice \n",scissors,"\nYou lose...")
elif n==3 and c==1:
    print("\nYour choice \n",scissors,"\nComputer choice \n",rock,"\nYou lose...")