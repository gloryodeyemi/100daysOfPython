import requests
from datetime import datetime
import os

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')

nutritionix_headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY,
}

exercise_params = {
    'query': "I used the stationary bike machine for 6 minutes, leg extension for 10 minutes, leg curl for 10 minutes, "
             "leg press for 10 minutes, and abdominal for 15 minutes.",
    'weight_kg': 53,
    'height_cm': 170.18,
    'age': 24,
    'gender': 'female'
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=nutritionix_headers)
print(response.json())
exercise_details = response.json()['exercises']
durations = [items['duration_min'] for items in exercise_details]
exercises = [items['name'].title() for items in exercise_details]
calories = [items['nf_calories'] for items in exercise_details]
print(f"Durations: {durations}\nExercises: {exercises}\nCalories: {calories}")

# add a row to google sheet using Sheety API
sheety_header = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}

post_date = datetime.now().strftime("%d/%m/%Y")

for idx in range(len(exercise_details)):
    post_time = datetime.now().strftime("%H:%M:%S")

    row_params = {
        'workout': {
            'date': post_date,
            'time': post_time,
            'exercise': exercises[idx],
            'duration': durations[idx],
            'calories': calories[idx]
        }
    }
    sheety_post = requests.post(url=SHEETY_ENDPOINT, json=row_params, headers=sheety_header)
    print(sheety_post.json())

# sheety_get = requests.get(url=SHEETY_ENDPOINT)
# print(sheety_get.json())
