#Eric Hurchey
#Programming Assignment 6
#04/28/2022
#

import random
SUITS=u'\u2660'+u'\u2665'+u'\u2666'+u'\u2663'

def NEWDECK(): #to call a function that shuffles all of the cards after you make a bet
    shuffled_cards = []
    for x in range(1, 14):
        for i in range(1, 5):
            z = .1 * i + x
            shuffled_cards.append(z)
    random.shuffle(shuffled_cards)
    return shuffled_cards

def deal(deck): #to call a function that draws a card out of 5 random cards
    return deck.pop(0) 

def Printhand(hand): #to call a function that prints the cards in the player's hand
    for x in range(len(hand)):
        if hand[x] > 0:
            printcard(hand[x])
        else:
            print("  ",end="") 
            
def select(hand): #to call a function that gets to decide to keep or throw out one of their 1-5 cards 
    pick_number = input("Enter 1 thru 5 to discard (or recover) a card, 0 to draw!")
    if pick_number != "":
        pick_number = int(pick_number)
        while pick_number != 0:
            if pick_number != 0 and pick_number <= 5: #if the player picks a number 1-5
                hand[pick_number - 1]= - hand[pick_number - 1]
                Printhand(hand) #a subfunction of a subfunction that is being asked in the directions
                pick_number = int(input("Enter 1 thru 5 to discard (or recover) a card, 0 to draw!"))
    return hand

def Getbet(inital_balance, prevbet): #to call get bet function which inputs how much money the player wants to invest in
    print("You have $", inital_balance, ".", " What is your bet (Enter 0 to quit)? ", sep="", end="")
    bet = input()
    if bet == "":
        bet = prevbet
    elif int(bet) == inital_balance: #if the player decides to gamble all of their money
        print("Risky!")
    elif int(bet) > inital_balance or int(bet) < 0: #if the player wants to bet more than he has or gives a value thats in the negative
        print("You don't have that much!")
        print("You have ", inital_balance, ".", " Whats your bet?", sep="",end="")
        bet = input()
    prevbet = bet
    return bet

def draw(deck, hand): #to call a function that draws cards for you
    for x in range(len(hand)):
        if hand[x] < 0: 
            hand[x] = deal(deck)
    Printhand(hand)

def printcard(card): #given code
    return print('A23456789TJQK'[int(card)-1],SUITS[frac(card)-1],sep='',end=' ')

def frac(card): #given code
    return round(card %1 * 10)

def rate(hand): #given code 
    shand = sorted(hand)
    i,j,prod = 0,1,1
    while j < 5:
        if int(shand[i]) == int(shand[j]):
            prod = prod * 2 ** (j - i)
            c = int(shand[j]) 
        else: 
            i = j
        j += 1
    if prod == 1: 
        d,f,e = 9,10,11
        for i in range(1,5):
            d = 1 if int(shand[i]) != int(shand[i-1])+1 else d
            e = 1 if int(shand[i]) != 8+i+int(shand[0]) else e
            f = 1 if frac(shand[0]) != frac(shand[i]) else f
        prod=d*e*f
    prod = 9 if prod == 11 else prod 
    prod = 1 if prod == 2 and 1 < c < 11 else prod 
    return prod

def main(): #to call the main function
    inital_balance = 100 #money to start off with
    prevbet = 0
    possible_outcomes = {1:'Busted',2:'Jacks or Better Pair',4:'Two Pair',8:'Three of a kind',9:'Straight',10:'Flush',16:'Full House',64:'Four of a Kind',90:'Straight Flush',110:'Royal Flush'}
    values = {1:-1,2:1,4:2,8:4,9:6, 10:8, 16:15,64:25, 90:40, 110:50} 
    while inital_balance > 0:
        bet = Getbet(inital_balance, prevbet)
        if int(bet) == 0: #if the player wants to quit the game
            print("Thanks for playing! You are exiting with $", inital_balance, sep='')
            break
        prevbet = int(bet)
        deck = NEWDECK()
        hand = []
        for i in range(5):
            hand.append(deal(deck))
        Printhand(hand)
        draw(deck,select(hand))
        print("Your hand is", possible_outcomes[rate(hand)])
        money_earned = values[rate(hand)]*int(bet)
        print("You win $",money_earned, sep="")
        inital_balance += money_earned
    if inital_balance <= 0: #if the player losses all of their money
        print("Thanks for playing. You are exiting with $0")
        
main()