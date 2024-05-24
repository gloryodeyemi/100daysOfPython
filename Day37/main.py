import os
import requests

TOKEN = os.environ.get('TOKEN')

pixela_endpoint = "https://pixe.la/v1/users"

# create pixela user
user_params = {
    "token": TOKEN,
    "username": "glowcodes",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# user_response = requests.post(url=pixela_endpoint, json=user_params)
# print(user_response.text)
