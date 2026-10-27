import requests
from datetime import datetime
import os

GENDER = os.environ["PROFILE_GENDER"]
WEIGHT_KG = float(os.environ["PROFILE_WEIGHT_KG"])
HEIGHT_CM = float(os.environ["PROFILE_HEIGHT_CM"])
AGE = int(os.environ["PROFILE_AGE"])

API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]

exercise_api_endpoint = os.environ["EXERCISE_API_ENDPOINT"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_api_endpoint, json=params, headers=headers)
result = response.json()
# print(result)


SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]

USERNAME = os.environ["SHEET_USERNAME"]
PASSWORD = os.environ["SHEET_PASSWORD"]

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs =  {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs, auth=(USERNAME, PASSWORD))
    print(sheet_response.text)

