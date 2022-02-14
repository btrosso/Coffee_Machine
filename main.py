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
    "water": 300,     # 300
    "milk": 200,      # 200
    "coffee": 100,    # 100
}


def show_report(coffee_res, money):
    for key in coffee_res:
        if key != 'coffee':
            print(f"{key.title()}: {coffee_res[key]}ml")
        else:
            print(f"{key.title()}: {coffee_res[key]}g")

    print(f"Money: ${money}")


def select_coffee(user_choice, menu):
    return menu[user_choice]


def compare_price(cash_given, item):
    if cash_given >= item["cost"]:
        return True
    else:
        return False


def can_make_coffee(item, coffee_res, user_choice):
    if item["ingredients"]["water"] <= coffee_res["water"]:
        if item["ingredients"]["coffee"] <= coffee_res["coffee"]:
            if user_choice != 'espresso':
                if item["ingredients"]["milk"] <= coffee_res["milk"]:
                    return 1
                else:
                    print("   Sorry, there is not enough milk.")
                    return 0
            else:
                return 1
        else:
            print("   Sorry, there is not enough coffee.")
            return 0
    else:
        print("   Sorry, there is not enough water.")
        return 0


till_amount = 0
can_make = 1

while till_amount != 100:
    # get the users input
    u_choice = input("   What would you like? (espresso/latte/cappuccino): ")
    if u_choice == 'report':
        show_report(coffee_res=resources, money=till_amount)
    elif u_choice == 'exit':
        exit()
    else:

        # save the selected item for later use
        selected_item = select_coffee(user_choice=u_choice, menu=MENU)

        # testing code
        # show_report(coffee_res=resources, money=till_amount)
        # print(f"Selected item: {selected_item}")

        # get the user's money
        print("Please insert coins.")
        quarters = .25 * int(input("How many quarters?: "))
        dimes = .10 * int(input("How many dimes?: "))
        nickels = .05 * int(input("How many nickels?: "))
        pennies = .01 * int(input("How many pennies?: "))
        total_amount_received = quarters + dimes + nickels + pennies

        can_make = can_make_coffee(item=selected_item, coffee_res=resources, user_choice=u_choice)

        if can_make == 1 and compare_price(cash_given=total_amount_received, item=selected_item):
            resources["water"] -= selected_item["ingredients"]["water"]
            resources["coffee"] -= selected_item["ingredients"]["coffee"]
            if u_choice != 'espresso':
                resources["milk"] -= selected_item["ingredients"]["milk"]
            till_amount += selected_item["cost"]
            change = '{:.2f}'.format(total_amount_received - selected_item['cost'])
            print(f"Here is ${change} in change")
            print(f"Here is your {u_choice} ☕. Enjoy!")
        elif can_make == 1 and not compare_price(cash_given=total_amount_received, item=selected_item):
            print("Sorry that's not enough money. Money refunded.")

