
import requests
import dotenv
import os

dotenv.load_dotenv()

URL = "https://api.openweathermap.org/data/2.5/forecast"

lat = os.getenv("LAT")
lon = os.getenv("LONG")
api_key = os.getenv("API_KEY")
params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    'cnt': 4
}


response = requests.get(URL, params=params)
# response = requests.get(URL)
response.raise_for_status()
data = response.json()
list_days = data["list"]
first_id = list_days[0]["weather"]
weather_id = first_id[0]['id']
weather_description = first_id[0]['description']


print(f"ID: {weather_id}, Description:{weather_description}")

forecast = {}
for i in list_days:
    id_weather = i['weather'][0]['id']
    description_weather = i['weather'][0]['description']
    print(f"ID: {id_weather}, Description: {description_weather}")




