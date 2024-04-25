import requests

api_key = "**************"
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": 42.314079,
    "lon": -83.036858,
    "appid": api_key,
}

# option 2
response = requests.get(weather_endpoint, params=params)

response.raise_for_status()
weather_data = response.json()
print(weather_data)
