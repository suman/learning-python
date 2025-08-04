from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# print(my_menu.get_items())


run_coffe_machine = True

while run_coffe_machine:
    chose_coffee_type = input(f"What would you like? {coffee_menu.get_items()}:")
    if chose_coffee_type == 'off':
        run_coffe_machine = False
    elif chose_coffee_type == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        order = coffee_menu.find_drink(chose_coffee_type)
        resource_balance = coffee_maker.is_resource_sufficient(order)
        if resource_balance and money_machine.make_payment(order.cost):
            coffee_maker.make_coffee(order)

