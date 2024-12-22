from art import logo, vs
from game_data import data
import random

def a_print(data):
    print("Compare A: ", data['name'], ",", data['description'], ", from ", data['country'], '.' )

def b_print(data):
    print("Against B: ", data['name'], ",", data['description'], ", from ", data['country'], '.' )

def compare(data_a, data_b, choice):
    if choice == "A":
        if data_a["follower_count"] > data_b["follower_count"]:
            return True
        else:
            return False
    elif choice == "B":
        if data_a["follower_count"] < data_b["follower_count"]:
            return True
        else:
            return False
        
def guess(data_a, data_b, vs):
    a_print(data_a)
    print(vs)
    b_print(data_b)

    choice = input("Who has more followers? Type 'A' or 'B': ")
    if choice != "A":
        choice = "B"

    return choice

def game():
    print(logo)
    score = 0

    choice_a = random.randint(0, len(data)-1)
    choice_b = random.randint(0, len(data)-1)

    data_a = data[choice_a]
    data_b = data[choice_b]

    choice = guess(data_a, data_b, vs)
        
    while compare(data_a, data_b, choice):
        score += 1
        print("You're right! Current score: ", score)

        data_a = data_b
        data_b = data[random.randint(0, len(data)-1)]

        choice = guess(data_a, data_b, vs)

    print("Sorry, thats wrong. Final score: ", score)

game()