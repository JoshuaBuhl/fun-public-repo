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
dealers_hand = []
players_hand = []
player_stays = False
dealer_stays = False
dealer_bust = False
player_bust = False


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
    if sum(hand) > 17:
        return False


def gameover():
    if player_bust:
        print("You went over 21, you lose!")
        return True
    elif dealer_bust:
        print("The dealer went over 21, you win!")
        return True
    elif player_stays and dealer_stays:
        if sum(players_hand) > sum(dealers_hand):
            print(f"You won with {sum(players_hand)}!")
        elif sum(players_hand) == sum(dealers_hand):
            print(f"It's a Draw with {sum(players_hand)}.")
        else:
            print(f"The Dealer won with {sum(dealers_hand)}.\nToo Bad!")
        return True
    else:
        return False


print("Welcome to Blackjack!")

if (input("Do you want to play a round?(y/n)")).lower() == 'y':
    deal_card(players_hand)
    deal_card(dealers_hand)
    deal_card(players_hand)
    deal_card(dealers_hand)

    print(f"Dealers cards: {[dealers_hand[0], '_']}\n "
          f"Your cards: {players_hand}")

    while not gameover():
        if not player_stays and not player_bust:
            if (input("Do you want another card?(y/n)").lower() == 'y'):
                if deal_card(players_hand):
                    player_bust = True
                else:
                    print(f"Dealers cards: {dealers_hand}\n "
                          f"Your cards: {players_hand}")
            else:
                player_stays = True

        if not dealer_stays and not dealer_bust:
            if dealer_choice(dealers_hand):
                if deal_card(dealers_hand):
                    dealer_bust = True
                else:
                    print(f"Dealers cards: {dealers_hand}\n "
                          f"Your cards: {players_hand}")
            else:
                dealer_stays = True

