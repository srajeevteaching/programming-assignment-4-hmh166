# Hannah Hodges
# CS 151, Dr. Rajeev
# Programming Assignment 4
# 11/10/2021
# defining the variables
import random

suit = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
value = {'2', '3', '4', '5', '6', '7', '8', '9', '10', '10',
         '10', '10', '11'}
player1 = input
play = True


def card():
    card = suit + rank
    return card


# function for player1 shuffle
def shuffle(suit, rank):
    deck = []
    for suit in suit:
        for rank in rank:
            deck.append(suit, rank)


# function for deck for the dealer
def deck(dealer):
    deckDealer = ''
    for card in deck:
        deckDealer +=  card
        return deckDealer


# function for shuffle of card deck
def shuffle():
    random.shuffle(deck)


def deal():
    card1 = deck()
    return card1


def hand():
    cards = []  # empty list to store cards
    value = 0
    aces = 0  # to keep track of number of aces


def add_card(value, rank):
    card.append(card)
    value += value[card.rank]
    if card.rank == 'Ace':
        aces += 1


def ace():
    while value > 21:
        value -= 10
        aces -= 1


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.ace()


# function for the hit or stand

def hit_or_stand(deck, hand):
    while True:
        x = input("Would you like to Hit or Stand? Enter 'hit' or 'stand'")
        if x == 'hit':
            hit(deck, hand)
        elif == 'stand':
            print("Player stands. Dealer is now playing.")
            play = False
        else:
            print("Try again.")


# function to display cards

def show_card(player1, dealer):
    print("Dealer's Hand")
    print("hidden")
    print(' ', dealer.card[1])
    print("Player's Hand: ", player1.card)


def show_all(player, dealer):
    print("Dealer's Hand:", dealer.card)
    print("Dealer's Hand =", dealer.value)
    print("Player's Hand: ", player1.card)
    print("Player's Hand = ", player1.value)


# to drive the program
def main():
    print("Blackjack!")
    deck = deck()
    deck.shuffle()
    player1_hand = hand()
    player1_hand.add_card(deck.deal())
    player1_hand.add_card(deck.deal())
    dealer_hand = hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    show_card(player1_hand, dealer_hand)

    while play == True:
        hit_or_stand(deck, player1_hand)
    show_card(player1_hand, dealer_hand)

    # if had is over 21, break will stop the loop of hit or stand
    if player1_hand.value > 21:
        break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

    show_all(player1_hand, dealer_hand)

    if dealer_hand.value > 21:
        break

    if dealer_hand.value > player1_hand.value:
        dealer_wins(player1_hand, dealer_hand)

    if dealer_hand.value < player1_hand.value:
        player1_wins(player1_hand, dealer_hand)

    new_game = input("Do you want to play again? 'Yes' or 'No'")
    if new_game == 'Yes':
        play = True
    else:
        print('Game Over')


main()



