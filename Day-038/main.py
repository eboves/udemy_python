import requests
import dotenv 
import os

dotenv.load_dotenv()
x_app_id = os.getenv("XAPPID")
x_app_key = os.getenv("XAPPKEY")

BASED_URL_NUTRITION = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
# BASED_URL = "https://app.100daysofpython.dev/healthz"
exercise = input("What excercises you did? ")
headers = {
    "x-app-id": x_app_id,
    "x-app-key": x_app_key,
    "Content-Type": "application/json",
}
data = {
  "query": exercise,
}

BASED_URL_SHEETS = "https://api.sheety.co/89ec0ccd5c5132abb47011e3c56c278d/ebWorkouts/workouts"



# print(exercise)

# response = requests.get(BASED_URL)
# result = response.json()
# response = requests.post(BASED_URL_NUTRITION, headers=headers, json=data)
# result = response.json()
response = requests.get(BASED_URL_SHEETS)
result = response.json()

print(result)




