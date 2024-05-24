import os
import requests
from datetime import datetime

TOKEN = os.environ.get('TOKEN')
USERNAME = "glowcodes"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
GRAPH_ID = "graph1"

# create pixela user
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# user_response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(user_response.text)

# create a new graph
graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": "100 Days of Python Graph",
    "unit": "views",
    "type": "int",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(graph_response.text)

# posting a pixel
today_date = datetime.now().strftime("%Y%m%d")
yesterday_date = datetime(year=2024, month=5, day=23).strftime("%Y%m%d")
print(f"Today's date formatted: {today_date}\nYesterday's date formatted: {yesterday_date}")

pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
pixel_config = {
    "date": today_date,
    "quantity": "6",
    "optionalData": '{"day": 37}'
}

# pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(pixel_response.text)
