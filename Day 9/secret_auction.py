from replit import clear
from art import logo

players = {}
continue_ask = "Y"

print(logo)
print("Welcome to the secret auction program.")

while continue_ask == "Y":
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    players[name] = bid
    continue_ask = input("Are there any other bidders? Y/n ")
    clear()

highest_bid = max(players.values())
print("The winner is", list(players.keys())[list(players.values()).index(highest_bid)],
      "with highest bid", highest_bid)
