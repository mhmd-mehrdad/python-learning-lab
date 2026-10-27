import os
# RAIN ALERT PROJECT
import requests

OWM_endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = os.environ["WEATHER_API_KEY"]

weather_params = {
    "lat" : float(os.environ["WEATHER_LATITUDE"]),
    "lon" : float(os.environ["WEATHER_LONGITUDE"]),
    "appid" : api_key,
    "cnt" : 4,
}

response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# print(weather_data["list"][0]["weahter"][0]["id"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("bring an umbrella")



