import os
import requests
from datetime import datetime

TOKEN = os.environ.get('TOKEN')
USERNAME = "glowcodes"
HEADERS = {
    "X-USER-TOKEN": TOKEN
}
PIXELA_ENDPOINT = "https://pixe.la/v1/users"


def create_user():
    # create pixela user
    user_params = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes",
    }

    user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(user_response.text)


def create_graph():
    # create a new graph
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    graph_config = {
        "id": input("Enter the graph id: "),
        "name": input("Enter the graph name: "),
        "unit": input("Enter the unit of measure (e.g., km, kg, etc.): "),
        "type": input("Enter the graph type: (int or float): "),
        "color": input("Enter the color: (shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) "
                       "and kuro (black)): "),
    }

    graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=HEADERS)
    print(graph_response.text)


def collect_date():
    date = input("Are you entering a data for today? (yes or no): ")
    if date == "yes":
        post_date = datetime.now().strftime("%Y%m%d")
    else:
        post_year = int(input("Enter the year (eg., 2024): "))
        post_month = int(input("Enter the month (eg., 5): "))
        post_day = int(input("Enter the day (eg., 24): "))
        post_date = datetime(year=post_year, month=post_month, day=post_day).strftime("%Y%m%d")
    return post_date


def collect_params():
    graph_id = input("Enter the graph id: ")
    quantity = input("Enter the quantity? ")

    return graph_id, quantity


def post_pixel():
    # posting a pixel
    post_date = collect_date()
    graph_id, quantity = collect_params()

    pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}"
    pixel_config = {
        "date": post_date,
        "quantity": quantity,
        # "optionalData": '{"optional": input("Enter the optional value: ")}'
    }

    pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=HEADERS)
    print(pixel_response.text)


def update_and_delete_pixel(choice):
    # update a pixel
    date = collect_date()
    graph_id, quantity = collect_params()

    endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{graph_id}/{date}"
    if choice == "update":
        update_config = {
            "quantity": quantity,
            # "optionalData": '"optional": input("Enter the optional value: ")'
        }

        response = requests.put(url=endpoint, json=update_config, headers=HEADERS)
    else:
        response = requests.delete(url=endpoint, headers=HEADERS)

    print(response.text)


print("******************\nPIXEL GRAPH API!!!\n******************")
option = input("Good day! What would you like to do today? (create user, create graph, post, update, or delete): ")
exit_loop = False
while not exit_loop:
    if option == "create user":
        create_user()
        exit_loop = True
    elif option == "create graph":
        create_graph()
        exit_loop = True
    elif option == "post":
        post_pixel()
        exit_loop = True
    elif option == "update" or option == "delete":
        update_and_delete_pixel(option)
        exit_loop = True
    else:
        option = input("Invalid option, please choose again (create user, create graph, post, update, or delete): ")
