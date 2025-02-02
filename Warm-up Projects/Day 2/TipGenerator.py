print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage bill would you like to give? 10, 12, 15 "))
people = float(input("How many people to split the bill? "))
total = (bill + tip / 100 * bill) / people
total = round(total, 2)
print(f"Each person should pay: ${total}")
