import requests

api_key = "***************"
weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

params = {
    "lat": 23.130280,
    "lon": 113.288879,
    "appid": api_key,
    "cnt": 4
}

# option 2
response = requests.get(weather_endpoint, params=params)

response.raise_for_status()
weather_data = response.json()
print(weather_data)

weather_codes = []

# Option 1: when multiple weather conditions are returned.
# for hour in weather_data["list"]:
#     for cond in hour["weather"]:
#         code = cond["id"]
#         weather_codes.append(code)

# Option 2: for a single weather condition
for hour in weather_data["list"]:
    code = hour["weather"][0]["id"]
    weather_codes.append(code)

print(f"All weather codes: {weather_codes}")

rainy = [cod for cod in weather_codes if cod < 700]
if len(rainy) > 0:
    print("Bring an umbrella")
else:
    print("Clear sky, you're good!")
