############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card(hand):
    hand.append(random.choice(cards))
    if sum(hand) > 21:
        if 11 in hand:
            hand[hand.index(11)] = 1
            return False
        else:
            return True
    else:
        return False


def dealer_choice(hand):
    if sum(hand) >= 17:
        return False
    else:
        return True


def gameover():
    players_score = sum(players_hand)
    dealers_score = sum(dealers_hand)
    if player_bust:
        print("You went over 21, you lose!")
    elif dealer_bust:
        print("The dealer went over 21, you win!")
    elif players_score > dealers_score:
        print(f"You won with {players_score}!")
    elif players_score == dealers_score:
        if len(players_hand) == 2 != len(dealers_hand) == 2:
            if len(players_hand) == 2:
                print("You win, your Blackjack beats the tie!")
            else:
                print("You lose, the dealers Blackjack beats the tie!")
        else:
            print(f"It's a Draw with {players_score}.")
    else:
        print(f"The Dealer won with {dealers_score}.\nToo Bad!")


print("Welcome to Blackjack!")

while (input("Do you want to play a round?(y/n)\n")).lower() == 'y':
    dealers_hand = []
    players_hand = []
    players_turn = True
    dealer_bust = False
    player_bust = False
    deal_card(players_hand)
    deal_card(dealers_hand)
    deal_card(players_hand)

    print(f"Dealers cards: {dealers_hand}\n "
          f"Your cards: {players_hand}")

    while players_turn:
        if (input("Do you want another card?(y/n)").lower() == 'y'):
            if deal_card(players_hand):
                player_bust = True
                players_turn = False
            else:
                print(f"Dealers cards: {dealers_hand}\n "
                      f"Your cards: {players_hand}")
        else:
            players_turn = False

    if not player_bust:
        while dealer_choice(dealers_hand):
            if deal_card(dealers_hand):
                dealer_bust = True

    print(f"Dealers cards: {dealers_hand}\n "
          f"Your cards: {players_hand}")

    gameover()

