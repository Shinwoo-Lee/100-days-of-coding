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


def show_report(money):
    print(f"Water: {resources['water']}ml")
    print(f"Mile: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def take_money(menu):
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    product_price = MENU[menu]["cost"]
    total_insert = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01

    if total_insert < product_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(total_insert - product_price, 2)
        print(f"Here is ${change} in change.")
        return True


def check_requirements(menu):
    require_water = MENU[menu]["ingredients"]["water"]
    require_coffee = MENU[menu]["ingredients"]["coffee"]

    if resources["water"] < require_water:
        print("Sorry there is not enough water.")
        return False
    elif resources["coffee"] < require_coffee:
        print("Sorry there is not enough coffee.")
        return False

    if menu != "espresso":
        # if not "espresso", need to check milk too.
        require_milk = MENU[menu]["ingredients"]["milk"]
        if resources["milk"] < require_milk:
            print("Sorry there is not enough milk.")
            return False
        else:
            return True
    else:
        return True


def make_coffee(menu):
    require_water = MENU[menu]["ingredients"]["water"]
    require_coffee = MENU[menu]["ingredients"]["coffee"]
    check_requirements(menu)

    resources["water"] -= require_water
    resources["coffee"] -= require_coffee

    if menu != "espresso":
        require_milk = MENU[menu]["ingredients"]["milk"]
        resources["milk"] -= require_milk
        print(f"Here is your {menu} ☕️. Enjoy!")
    else:
        print(f"Here is your {menu} ☕️. Enjoy!")


# Machine Starts Here
Money = 0
Rerun = True
while Rerun:
    Menu = input("  What would you like? (espresso/latte/cappuccino): ").lower()
    if Menu == "off":
        Rerun = False
    elif Menu == "report":
        show_report(Money)
    else:
        if check_requirements(Menu):
            if take_money(Menu):
                make_coffee(Menu)
                Money += MENU[Menu]["cost"]
                Rerun = True
