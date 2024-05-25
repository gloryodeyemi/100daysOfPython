import requests
from datetime import datetime
import os

APP_ID = os.environ.get('APP_ID')
API_KEY = os.environ.get('API_KEY')
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = os.environ.get('SHEETY_ENDPOINT')
SHEETY_TOKEN = os.environ.get('SHEETY_TOKEN')


def get_exercise():
    nutritionix_headers = {
        'x-app-id': APP_ID,
        'x-app-key': API_KEY,
    }

    exercise_params = {
        'query': input("Enter the exercises you did today: "),
        'weight_kg': input("Enter your weight (kg): "),
        'height_cm': input("Enter your height (cm): "),
        'age': input("Enter your age: "),
        'gender': input("Enter your gender (male or female): ")
    }

    response = requests.post(url=NUTRITIONIX_ENDPOINT, json=exercise_params, headers=nutritionix_headers)
    exercise_details = response.json()['exercises']
    durations = [items['duration_min'] for items in exercise_details]
    exercises = [items['name'].title() for items in exercise_details]
    calories = [items['nf_calories'] for items in exercise_details]
    print(f"\nDurations: {durations}\nExercises: {exercises}\nCalories: {calories}\n"
          f"********************************************************")
    return durations, exercises, calories


def add_row():
    post_date = datetime.now().strftime("%d/%m/%Y")
    durations, exercises, calories = get_exercise()
    # add a row to google sheet using Sheety API
    sheety_header = {
        "Authorization": f"Bearer {SHEETY_TOKEN}"
    }

    for idx in range(len(exercises)):
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


if __name__ == "__main__":
    print("""
____    __    ____  ______   .______       __  ___   ______    __    __  .___________.   .___________..______          ___       ______  __  ___  _______ .______      
\   \  /  \  /   / /  __  \  |   _  \     |  |/  /  /  __  \  |  |  |  | |           |   |           ||   _  \        /   \     /      ||  |/  / |   ____||   _  \     
 \   \/    \/   / |  |  |  | |  |_)  |    |  '  /  |  |  |  | |  |  |  | `---|  |----`   `---|  |----`|  |_)  |      /  ^  \   |  ,----'|  '  /  |  |__   |  |_)  |    
  \            /  |  |  |  | |      /     |    <   |  |  |  | |  |  |  |     |  |            |  |     |      /      /  /_\  \  |  |     |    <   |   __|  |      /     
   \    /\    /   |  `--'  | |  |\  \----.|  .  \  |  `--'  | |  `--'  |     |  |            |  |     |  |\  \----./  _____  \ |  `----.|  .  \  |  |____ |  |\  \----.
    \__/  \__/     \______/  | _| `._____||__|\__\  \______/   \______/      |__|            |__|     | _| `._____/__/     \__\ \______||__|\__\ |_______|| _| `._____|                                                                                                                                                                     
    """)
print("********************************************************")
print("You sweat it, I track it! Log your exercise stats now!!!")
print("********************************************************")
exit_loop = False
while not exit_loop:
    add_row()
    print("********************************************************\n")
    done = input("All done? (yes or no): ")
    if done == "yes":
        exit_loop = True

print("Got all your stats in! Go take a nice long bath🛀 or shower🚿 and have yourself a swell day!")
print("********************************************************")
