import requests

MY_LAT = 42.314079
MY_LONG = -83.036858

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response.status_code)  # to get the response status code
response.raise_for_status()  # to raise an exception is request fails
data = response.json()  # to get the json data

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(f"ISS position: {iss_position}")

# Sunrise and Sunset times
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(f"Sunrise: {sunrise}\nSunset: {sunset}")
