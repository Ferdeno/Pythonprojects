from blackjack21art import logo
import random
import os
def dealcard():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculate_scores(card):
    if sum(card)==21 and len(card)==2:
        #this condition is to check the blackjack that is 10+11(Ace)
        return 0
    elif sum(card)>21 and 11 in card:
        card.append(1)
        card.remove(11)
    return sum(card)
def play_game():
    def compare(user_score,computer_score):
        if user_score==0 and computer_score!=0:
            return "User wins...It's a blackjack..."
        elif computer_score==0 and user_score!=0:
            return "Dealer Wins...It's a blackjack..."
        elif (user_score==0 and computer_score==0) or (user_score>21 and computer_score>21 and user_score==computer_score):
            return "Game draw..."
        elif user_score>21 and computer_score>21 and user_score<computer_cards:
            return "User Wins...Dealer lose..."
        elif user_score>21 and computer_score>21 and user_score>computer_cards:
            return "Dealer Wins...User lose..."
        elif user_score>21 and computer_score<=21:
            return "Dealer Wins...User lose..."
        elif computer_score>21 and user_score<=21:
            return "User Wins...Dealer lose..."
        elif user_score>computer_score:
            return "User Wins...Dealer lose..."
        elif user_score==computer_score:
            return "Draw..."
        else:
            return "Dealer Wins...User lose..."
        
    user_cards=[dealcard(),dealcard()]
    computer_cards=[dealcard(),dealcard()]
    is_game_over=False

    while not is_game_over:
        user_score=calculate_scores(user_cards)
        computer_score=calculate_scores(computer_cards)
        print(f"User cards : {user_cards} User score : {sum(user_cards)}")
        print(f"Dealer cards : [{computer_cards[0]}]")

        if user_score==0 and computer_score!=0:
            is_game_over=True
        elif computer_score==0 and user_score!=0:
            is_game_over=True
        elif (user_score==0 and computer_score==0) or (user_score>21 and computer_score>21 and user_score==computer_score):
            is_game_over=True
        elif user_score>21 and computer_score>21 and user_score<computer_cards:
            is_game_over=True
        elif user_score>21 and computer_score>21 and user_score>computer_cards:
            is_game_over=True
        elif user_score>21 and computer_score<=21:
            is_game_over=True
        elif computer_score>21 and user_score<=21:
            is_game_over=True
        else:
            user_deal=int(input("Type 1 for another card (HIT) type 0 to pass (HAND) : "))
            if user_deal:
                user_cards.append(dealcard())
            else:
                is_game_over=True


    while sum(computer_cards)<17:
        computer_cards.append(dealcard())
    print(f"Final\nUser cards {user_cards} User score : {user_score}\nDealer cards {computer_cards} Dealer score : {computer_score}")
    print(compare(user_score,computer_score))


while int(input("Type 1 to play blackjack game else type 0 : ")):
    os.system('cls')
    print(logo)
    play_game()