from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True


while is_on:
    order = menu.get_items()
    choice = input(f"What would you like? {order}: ")
    if choice == "off":
        is_on = False
# TODO 1 Print report
    elif choice == "report":
        coffee_report = coffee_maker.report()
        profit_report = money_machine.report()
    else:
        drink = menu.find_drink(choice)
        # TODO 2 Check resources
        if coffee_maker.is_resource_sufficient(drink):
            # TODO 3 Process coins
            # TODO 4 Check transaction
            if money_machine.make_payment(drink.cost):
                # TODO 5 Make coffee
                serve_drink = coffee_maker.make_coffee(drink)

