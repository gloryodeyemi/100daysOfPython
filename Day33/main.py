import time
import requests
import datetime as dt
import email_sender

MY_LAT = 42.314079
MY_LONG = -83.036858


def is_iss_close():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    # print(response.status_code)  # to get the response status code
    iss_response.raise_for_status()  # to raise an exception is request fails
    iss_data = iss_response.json()  # to get the json data

    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])

    iss_position = (longitude, latitude)
    print(f"ISS position: {iss_position}")

    return MY_LONG-5 <= longitude <= MY_LONG+5 and MY_LAT-5 <= latitude <= MY_LAT+5


# Sunrise and Sunset times
def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    print(f"Sunrise: {sunrise}\nSunset: {sunset}")

    time_now = dt.datetime.now()
    current_hour = time_now.hour
    print(current_hour)
    return current_hour >= sunset or current_hour <= sunrise


while True:
    time.sleep(60)
    if is_iss_close() and is_dark():
        email_sender.send_using_gmail("Look up!", "The ISS is close to your current position, so look up.")
