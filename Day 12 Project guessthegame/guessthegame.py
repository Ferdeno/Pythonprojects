from guessthenumberlogo import logo
import os
import random

while "yes" == input("""Do you want to play guess the game type "yes" or "no" """):
    os.system("cls")
    print(logo)
    condition = input(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nChoose a difficulty. Type 'easy' or 'hard': ")
    n = 10 if condition == "easy" else 5
    number = random.randint(1, 100)
    # print(number)
    while n:
        print(f"You have {n} attempts remaining to guess the number.")
        guess = int(input("Make a guess : "))
        if guess == number:
            print(f"You got it! The answer was {number}.")
            break
        elif guess > number:
            print("Guess number is high")
            n -= 1
        else:
            print("Guess number is low")
            n -= 1
        if n:
            print("Guess again")
    if (n == 0):
        print(
            f"You've run out of guesses, you lose and the number is {number}")
