import art  # import the coffee machine art

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
# TODO: 1. Create function to print report
# TODO: 2. Create function to check if resource is sufficient
# TODO: 3. Create function to process coins
# TODO: 4. Create function to check if transaction is successful
# TODO: 5. Create function to make coffee
# TODO: 6. Ask user for their coffee choice
# TODO: 7. Turn coffee machine off


def print_report(available_resources, money):
    """
    :param available_resources: dictionary containing the resources available
    :param money: the money made
    :return: displays all the resources in the dictionary and the money made
    """
    print(f"Water: {available_resources['water']}ml\nMilk: {available_resources['milk']}ml\n"
          f"Coffee: {available_resources['coffee']}g\nMoney: ${money}\n")


def check_resources(available_resources, menu_item, user_choice):
    """
    :param available_resources: dictionary containing the resources available
    :param menu_item: dictionary containing the coffee menu
    :param user_choice: the coffee the user wants to buy
    :return: True if the available resources are sufficient to make the coffee, or False if otherwise.
    """
    user_option = menu_item[user_choice]['ingredients']
    insufficient_items = ""
    for item in user_option:
        if available_resources[item] < user_option[item]:
            insufficient_items += f"{item}, "
    if insufficient_items == "":
        return True
    else:
        print(f"Sorry, the {insufficient_items}is not enough to make your coffee.\n")
        return False


def process_coins(quarters_, dimes_, nickles_, pennies_):
    """
    :param quarters_: number of quarters user entered.
    :param dimes_: number of dimes user entered.
    :param nickles_: number of nickles user entered.
    :param pennies_: number of pennies user entered.
    :return: the total amount.
    """
    money_paid = round((0.25 * quarters_) + (0.10 * dimes_) + (0.05 * nickles_) + (0.01 * pennies_), 2)
    return money_paid


def transaction_successful(amount, menu_item, user_choice):
    """
    :param amount: the total amount user paid
    :param menu_item: dictionary containing the coffee menu
    :param user_choice: the coffee the user wants to buy
    :return: the coffee cost if the amount is sufficient, or 0 if otherwise.
    """
    coffee_cost = menu_item[user_choice]['cost']
    if amount > coffee_cost:
        change = amount - coffee_cost
        print(f"\nHere is ${change:.2f} in change.\n")
        return coffee_cost
    elif amount == coffee_cost:
        return coffee_cost
    else:
        print(f"\nSorry, that's not enough money. ${amount:.2f} refunded.\n")
        return 0


def make_coffee(available_resources, menu_item, user_choice):
    """
    :param available_resources: dictionary containing the resources available
    :param menu_item: dictionary containing the coffee menu
    :param user_choice: the coffee the user wants to buy
    :return: the available resources after making the coffee
    """
    user_option = menu_item[user_choice]['ingredients']
    for item in user_option:
        available_resources[item] = available_resources[item] - user_option[item]
    print(f"Here's your {user_choice}☕. Enjoy!\n")
    return available_resources


def coffee_machine():
    """
    Perform coffee machine operations.
    """
    print(art.logo)  # display the coffee machine logo
    print(art.logo_name)  # display the coffee machine logo name

    # define the initial resources available
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    prompt = "on"  # set the coffee machine on as default
    money_made = 0.0  # set the money made by the coffee machine to $0.0 as default

    # keep making coffee as long as machine is on
    while prompt == "on":
        user_request = input("What would you like? (espresso/latte/cappuccino): ")  # ask user for input

        if user_request == "report":
            print_report(resources, money_made)  # display machine report
        elif user_request == "off":
            prompt = "off"  # set the machine to off - terminate the program
        else:
            is_sufficient = check_resources(resources, MENU, user_request)  # check if resources is sufficient

            if is_sufficient:  # continue if resources are sufficient
                print("\nPlease insert coins.")
                quarters = int(input("How many quarters?: "))
                dimes = int(input("How many dimes?: "))
                nickles = int(input("How many nickles?: "))
                pennies = int(input("How many pennies?: "))
                amount_paid = process_coins(quarters, dimes, nickles, pennies)  # calculate the total amount user paid

                # check if the amount user paid is sufficient
                coffee_price = transaction_successful(amount_paid, MENU, user_request)

                if coffee_price > 0:  # continue if amount is sufficient
                    money_made += coffee_price  # add the coffee price to the money made by the machine
                    # deduct the resources used from the available resources
                    resources = make_coffee(resources, MENU, user_request)


coffee_machine()  # call the coffee machine
