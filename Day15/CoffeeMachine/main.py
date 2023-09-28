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

# TODO: 1. Create function to print report
# TODO: 2. Create function to check if resource is sufficient
# TODO: 3. Create function to process coins
# TODO: 4. Create function to check if transaction is successful
# TODO: 5. Create function to make coffee
# TODO: 6. Ask user for their coffee choice
# TODO: 7. Turn coffee machine off


def print_report(resources):
    print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g")



prompt = "on"
user_request = input("What would you like? (espresso/latte/cappuccino): ")

if user_request == "report":
    print_report(resources)