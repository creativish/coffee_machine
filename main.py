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
profit = 0

def is_resource_sufficient(order_ingredients):
    """returns true when order can be made and false if ingredients are insufficient """
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True



def process_coin():
    """returns total calculated from coins inserted"""
    print("Pleaes insert coins.")
    total = int(input("how many quaters?:")) * 0.25
    total += int(input("how many dimes?:")) * 0.1
    total += int(input("how many nickles?:")) * 0.05
    total += int(input("how many pennies?:")) * 0.01
    return total

def is_transaction_successfull(money_received, drink_cost):
    """return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,  2)
        print(f"Here is your change $ {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money, Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your ☕ {drink_name}")







is_on = True

while is_on:
    choice = input("what would you like? (espresso/latte/cappuccino):")
    if choice == "off":
         is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}mg")
        print(f"money: {profit}$")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coin()
            if is_transaction_successfull(payment,drink["cost"]):
                make_coffee(choice, drink["ingredients"])




