import requests


api_key = "4f470ad1b201fb99dfa85ccd9a976f82"
lat = 42.314079
lon = -83.036858

params = {
    "lat": 42.314079,
    "lon": -83.036858,
    "appid": api_key,
}

# option 1
response1 = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}")

# option 2
response2 = requests.get(f"https://api.openweathermap.org/data/2.5/forecast", params=params)

response2.raise_for_status()
weather_data = response2.json()
print(weather_data)
