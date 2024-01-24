import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)  # to get the response status code
response.raise_for_status()  # to raise an exception is request fails
data = response.json()  # to get the json data

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(f"ISS position: {iss_position}")
