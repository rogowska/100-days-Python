from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
nextRound = 'y'

def calculateScore(deck):
    if sum(deck) > 21 and 11 in deck:
        deck.remove(11)
        deck.append(1)
    return sum(deck)

def winCheck(playerScore, dealerScore):
    if playerScore == 0:
        print("You had a blackjack, you won.")
    elif dealerScore == 0:
        print("Your opponent had a blackjack, you lost.")
    elif playerScore > 21:
        print("You went over, you lost.")
    elif dealerScore > 21:
        print("Your opponent went over, you won.")
    elif playerScore > dealerScore:
        print("You won!")
    elif playerScore < dealerScore:
        print("You lost")
    else:
        print("Its a draw!")

def currentScoreDisplay(playerDeck, dealerDeck):
    print("Your cards: ", playerDeck, " current score:", calculateScore(playerDeck) )
    print("Computer's first card: ", dealerDeck[0])

def finalScoreDisplay(playerDeck, dealerDeck):
    print("Your cards: ", playerDeck, " final score:", calculateScore(playerDeck))
    print("Computer's final hand: ", dealerDeck, " final score:", calculateScore(dealerDeck))

while nextRound == 'y':

    # generating decks
    playerDeck = []
    dealerDeck = []
    gameOver = False

    # generating cards
    for i in range(2):
        playerDeck.append(cards[random.randint(0, 12)])
        dealerDeck.append(cards[random.randint(0, 12)])

    print(logo)
    currentScoreDisplay(playerDeck, dealerDeck)

    if calculateScore(playerDeck) == 21 or calculateScore(dealerDeck) == 21:
        gameOver = True
        finalScoreDisplay(playerDeck, dealerDeck)
        if calculateScore(playerDeck) == 21:
            winCheck(0, calculateScore(dealerDeck))
        else:
            winCheck(calculateScore(playerDeck), 0)

    if not gameOver:
        #player hitting more cards
        additionalCard = input("Type 'y' to get another card, type 'n' to pass: ")
        while additionalCard == 'y':
            playerDeck.append(cards[random.randint(0,12)])
            if calculateScore(playerDeck) > 21:
                break
            currentScoreDisplay(playerDeck, dealerDeck)
            additionalCard = input("Type 'y' to get another card, type 'n' to pass: ")

        if calculateScore(playerDeck) < 21:
            #dealer hitting more cards
            while sum(dealerDeck) < 17:
                dealerDeck.append(cards[random.randint(0,12)])

        finalScoreDisplay(playerDeck, dealerDeck)
        winCheck(calculateScore(playerDeck), calculateScore(dealerDeck))

    nextRound = input("Do you want to play another round? y/n ")




