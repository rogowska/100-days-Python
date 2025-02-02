from art import logo
from random import randrange

HARD_LEVEL = 5
EASY_LEVEL = 10

def set_difficulty(choice):
    if choice == 'hard':
        return HARD_LEVEL
    else:
        return EASY_LEVEL

def make_a_guess(attempts, number, guessed):
    print("You have ", attempts, " remaining to guess the number.")
    try:
        guess = int(input("Make a guess: "))
    except ValueError:
        print("Provide numeric value!")
    else:
        if guess > number:
            print("Too high.")
        elif guess < number:
            print("Too low.")
        else:
            print("You got it! Answer was ", guess, ".")
            guessed = True
    return guessed

def game():
    number = randrange(100)
    guessed = False

    print(logo)
    print("I'm thinking of a number between 1 and 100")
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ")
    attempts = set_difficulty(choice)

    while attempts > 0 and not guessed:
        guessed = make_a_guess(attempts, number, guessed)
        attempts -= 1
    if not guessed:
        print("You lost.")

game()