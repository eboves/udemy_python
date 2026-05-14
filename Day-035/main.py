
import requests
import dotenv
import os
from twilio.rest import Client

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
# auth_token = '[AuthToken]'
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")

response = requests.get(URL, params=params)
# response = requests.get(URL)
response.raise_for_status()
data = response.json()
list_days = data["list"]
first_id = list_days[0]["weather"]
weather_id = first_id[0]['id']
weather_description = first_id[0]['description']


# print(f"ID: {weather_id}, Description:{weather_description}")

will_rain = False
for i in list_days:
    id_weather = i['weather'][0]['id']
    if id_weather < 700: 
        will_rain = True
    description_weather = i['weather'][0]['description']
    print(f"ID: {id_weather}, DESCRIPTION: {description_weather}")
if will_rain:
    # client = Client(account_sid, auth_token)
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        to=os.getenv("PERSONAL_NUMBER"),
        from_=os.getenv("TWILIO_NUMBER"),
        body="Klk papa desde TWILIO",
    )
    print(message.status)

