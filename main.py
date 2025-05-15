import requests
from datetime import datetime

GENDER = 'female'
HEIGHT_CM = 153
WEIGHT_KG = 56
AGE = 20
APP_ID = '845ff560'
API_KEY = '0d573069faee4f478ee72a809240d6eb'

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = "https://api.sheety.co/c58b2793e0d305cd26080ce60ac2cc5c/copyOfMyWorkouts/workouts"

exercise_text = input("Enter the exercise: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
response.raise_for_status()
result = response.json()
print(result)


today_date=datetime.now().strftime("%m%d%y")
now_time=datetime.now().strftime("%X")
for exercise in result["exercises"]:
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
        url=sheet_endpoint,
        json=sheet_inputs,
        auth=('sathvika', 'sathvika@12345')
    )



    print(sheet_response.text)
