from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import art

print(art.logo)  # display the coffee machine logo
print(art.logo_name)  # display the coffee machine logo name

cf_maker = CoffeeMaker()  # create an object of the coffee maker class
money_m = MoneyMachine()  # create an object of the money machine class
coffee_menu = Menu()  # create an object of the menu class
prompt = "on" # set the coffee machine on as default

# keep making coffee as long as machine is on
while prompt == "on":
    user_request = input(f"What would you like? ({coffee_menu.get_items()}): ")  # ask user for input

    if user_request == "report":
        cf_maker.report()  # display machine report
        money_m.report()
    elif user_request == "off":
        prompt = "off"  # set the machine to off - terminate the program
    else:
        order = coffee_menu.find_drink(user_request)  # check if user's request exists

        if order is not None:
            is_sufficient = cf_maker.is_resource_sufficient(order)  # check if resources is sufficient
            # print(is_sufficient)

            if is_sufficient:
                # check if the transaction is successful
                is_transaction_successful = money_m.make_payment(order.cost)
                if is_transaction_successful:
                    cf_maker.make_coffee(order)
                    print("hey")
