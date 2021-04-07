import requests
import os
import datetime as dt

APP_ID = os.environ["NUTRITIONX_APP_ID"]
API_KEY = os.environ["NUTRITIONX_APP_KEY"]
GENDER = "female"
WEIGHT = 56
HEIGHT = 100
AGE = 25

workout = input("Tell me which exercises you did: ")
nutritionx_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionx_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

exercise_params = {
    "query": workout,
    "gender": GENDER,
    "age": AGE
}

response = requests.post(nutritionx_endpoint, json=exercise_params, headers=nutritionx_headers)
response.raise_for_status()
print(response.json())


# Add a row
sheety_url = "https://api.sheety.co/5aa6890581e708af7e77fc8268b09aa8/myWorkouts/workouts"

today_date = dt.datetime.now().strftime("%d/%m/%Y")
now_time = dt.datetime.now().strftime("%X")

for exercise in response.json()["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(
        sheety_url,
        json=sheet_inputs,
        auth=(os.environ["USERNAME"],
            os.environ["PASSWORD"],)
    )

    print(sheet_response.text)
