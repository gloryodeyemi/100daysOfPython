import os
import requests

TOKEN = os.environ.get('TOKEN')
USERNAME = "glowcodes"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"

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
    "id": "graph1",
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
pixel_endpoint = f"{graph_endpoint}/graph1"
pixel_config = {
    "date": "20240524",
    "quantity": "6",
    "optionalData": '{"day": 37}'
}

pixel_response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(pixel_response.text)
