
#TODO 1, ask for the coffee type
#TODO 5, check if resource is enough to make the selected coffe
#TODO 2, ask to insert the different kind of coins
#TODO 3, calculat how much dollar it makes by summing coins
#TODO 4, check if the sum dolor is sufficent to purchase the selected coffee
#TODO 5, deliver the coffe if the sum amount is enough
#TODO 6, if not ask again user to select the coffe type


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def enough_resource_for_coffee(coffee_type):
    enough_resource = {'water': True, 'coffee': True, 'milk': True}

    if MENU[coffee_type]['ingredients']['water'] > resources['water']:
        enough_resource['water'] = False

    if MENU[coffee_type]['ingredients']['coffee'] > resources['coffee']:
        enough_resource['coffee'] = False

    if not coffee_type == 'espresso' and MENU[coffee_type]['ingredients']['milk'] > resources['milk']:
        enough_resource['milk'] = False

    return enough_resource

def convert_cents_to_dollar(user_provided_money):
    total_cents = user_provided_money['quarter'] * 25
    total_cents += user_provided_money['dime'] * 10
    total_cents += user_provided_money['nickel'] * 5
    total_cents += user_provided_money['penny']
    total_dollar = total_cents / 100
    return total_dollar

def enough_money_for_coffee(coffee_cost, user_provided_money):
    total_dollar = convert_cents_to_dollar(user_provided_money)
    return total_dollar >= coffee_cost

def display_report(remaining_resources):
    print(f"Water: {remaining_resources['water']}")
    print(f"Milk: {remaining_resources['milk']}")
    print(f"Coffee: {remaining_resources['coffee']}")
    if 'money' in remaining_resources:
        print(f"Money: ${remaining_resources['money']}")
    else:
        print(f"Money: $0")


def insert_coins():
    quarter = int(input("how many quarters? "))
    dime = int(input("how many dimes? "))
    nickel = int(input("how many nickles? "))
    penny = int(input("how many pennies? "))

    return {"quarter" : quarter, "dime" : dime, "nickel" : nickel, "penny": penny}

def serve_coffee(serve_coffee_type):
    print(f"Here is your {serve_coffee_type} ☕️.Enjoy!")

def get_balance(received_coins, coffee_type):
    total_dollar = convert_cents_to_dollar(received_coins)
    consumed_dollar = MENU[coffee_type]['cost']
    if total_dollar > consumed_dollar:
        print(f"Here is ${total_dollar  - consumed_dollar} in change.")


def adjust_resource(coffee_type):
    resources["water"] -= MENU[coffee_type]['ingredients']['water']
    resources["coffee"] -= MENU[coffee_type]['ingredients']['coffee']
    if not coffee_type == 'espresso':
        resources["milk"] -= MENU[coffee_type]['ingredients']['milk']
    if 'money' in  resources:
        resources["money"] +=  MENU[coffee_type]['cost']
    else:
        resources["money"] = MENU[coffee_type]['cost']
run_coffe_machine = True

while run_coffe_machine:
    chose_coffee_type = input("What would you like? (espresso/latte/cappuccino):")
    if chose_coffee_type == 'off':
        run_coffe_machine = False
    elif chose_coffee_type == 'report':
        display_report(resources)
    else:
        resource_balance = enough_resource_for_coffee(chose_coffee_type)
        if ((resource_balance['water'] and resource_balance['coffee']) or
                (not chose_coffee_type == 'espresso' and resource_balance['water'] and resource_balance['coffee'] and resource_balance['milk'])):

            all_received_coins = insert_coins()
            if enough_money_for_coffee(MENU[chose_coffee_type]['cost'], all_received_coins):
                serve_coffee(chose_coffee_type)
                get_balance(all_received_coins, chose_coffee_type)
                adjust_resource(chose_coffee_type)
            else:
                print("Sorry the money you provided is not enough. Money Refunded.")
        else:
            print("Sorry there is no enough resource to make coffee")