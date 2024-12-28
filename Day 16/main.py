from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

class CoffeeMachine():

    def __init__(self):
        self.coffee_maker = CoffeeMaker()
        self.money_machine = MoneyMachine()
        self.menu = Menu()
        self.is_on = True

    def run(self):
        while self.is_on:
            choice = input("What would you like? (" + self.menu.get_items() + ") ")
            if choice == "off":
                self.is_on = False
            elif choice == "report":
                self.coffee_maker.report()
                self.money_machine.report() 
            else:
                drink = self.menu.find_drink(choice)
                if self.coffee_maker.is_resource_sufficient(drink) and self.money_machine.make_payment(drink.cost):
                        self.coffee_maker.make_coffee(drink)

machine = CoffeeMachine()
machine.run()