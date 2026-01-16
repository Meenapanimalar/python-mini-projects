from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


menu = Menu()
coffeemaker= CoffeeMaker()
moneymachine = MoneyMachine()


machine_is_on = True
while machine_is_on:
    user_input = input(f"What would you like? {menu.get_items()}:")
    if user_input == "off":
        machine_is_on = False
    elif user_input == "report":
        coffeemaker.report()
        moneymachine.report()
    else :
        coffee = menu.find_drink(user_input)
        if coffeemaker.is_resource_sufficient(coffee):
            if moneymachine.make_payment(coffee.cost):
                coffeemaker.make_coffee(coffee)











