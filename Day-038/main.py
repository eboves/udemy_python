import requests
import dotenv 
import os
import datetime

dotenv.load_dotenv()


BASED_URL_NUTRITION = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
# BASED_URL = "https://app.100daysofpython.dev/healthz"
BASED_URL_SHEETS = "https://api.sheety.co/89ec0ccd5c5132abb47011e3c56c278d/ebWorkouts/workouts"

x_app_id = os.getenv("XAPPID")
x_app_key = os.getenv("XAPPKEY")


exercise = input("What excercises you did? ")

headers = {
    "x-app-id": x_app_id,
    "x-app-key": x_app_key,
    "Content-Type": "application/json",
}
data = {
  "query": exercise,
}

date = datetime.datetime.now()
today_date = date.strftime("%x")
today_time = date.strftime("%X")

# print(today_date, today_time)

response_nutrition = requests.post(BASED_URL_NUTRITION, headers=headers, json=data)
result_nutrition = response_nutrition.json()
nutrition_info = result_nutrition["exercises"][0]

duration = nutrition_info['duration_min']
calories = nutrition_info['nf_calories']
activity = nutrition_info['name']
print(activity, duration, calories)






response_sheets = requests.get(BASED_URL_SHEETS)
result_sheets = response_sheets.json()

# print(result_nutrition)
# print(result_sheets)




