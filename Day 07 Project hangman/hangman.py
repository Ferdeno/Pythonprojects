import random
from hangmanwords import word_list
from hangmanart import stages,logo
print(logo)
word=random.choice(word_list)
print(word)
w=["_"]*len(word)
print("A random word is chosen try to guess the word ")
l=len(word)
h=6
while h>0:
    s=input("Guess a letter : ")
    temp=0
    for i in range(l):
        if s==word[i]:
            w[i]=s
            temp=1
    if not temp:
        h-=1
    print(stages[h])
    print(*w)
    if '_' not in w:
        break
if '_' not in w:
    print("You win !!! The word is guessed")
else:
    print("You lose !!! The word is not guessed")
    
