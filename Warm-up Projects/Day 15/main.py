from menu import MENU

resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

def print_report(profit):
    print("Water: ", resources["water"], "ml\nMilk: ", resources["milk"], "ml\nCoffee: ", resources["coffee"], "g\nMoney: $", profit)

def check_resources(coffee_type):
    for resource in resources:
        if resources[resource] - MENU[coffee_type]["ingredients"][resource] < 0:
            print("Sorry, there is not enough ", resource, ".", sep='')
            return False
        return True
    
def insert_coins_and_return_value():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total
    
def offer_change(inserted_value, coffee_value):
    print("Here is the $", round(inserted_value-coffee_value, 2), " in change.", sep='')

def make_coffee(coffee_type):
    for resource in resources:
        if resource in MENU[coffee_type]["ingredients"]:
            resources[resource] -= MENU[coffee_type]["ingredients"][resource]
    print("Here is your ", coffee_type, ". Enjoy!", sep='')

def coffee_machine():
    is_turned_on = True
    profit = 0

    while is_turned_on:
        choice = input("What would you like? (espresso/latte/cappuccino)")
        if choice == "off":
            is_turned_on = False
        elif choice == "report":
            print_report(profit)
        elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
            is_sufficient = check_resources(choice)
            if is_sufficient:
                coins_value = insert_coins_and_return_value()
                coffee_value = MENU[choice]["cost"]
                if coins_value >= coffee_value:
                    profit += coffee_value
                    if coins_value > coffee_value:
                        offer_change(coins_value, coffee_value)
                    make_coffee(choice)
                else:
                    print("Sorry, thats not enough money, money refunded.")

coffee_machine()