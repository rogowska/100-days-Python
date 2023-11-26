import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

myList = [rock, paper, scissors]

choice = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors.\n"))
if choice > 3 or choice < 0:
    print("Provide correct input.")
    exit()
print("Your choice:", myList[choice])
computer_choice = random.choice([0, 1, 2])
print("Computers choice:", myList[computer_choice])
if choice == computer_choice:
    print("Draw.")
elif choice == 2 and computer_choice == 0 or choice > computer_choice:
    print("You won!")
else:
    print("You lost.")
