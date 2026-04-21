"""
Day 33 - API

Description:
Working with API, using the International Space Station API

"""
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
lon = data["iss_position"]['longitude']
lat = data["iss_position"]['latitude']
position = (lon,lat)
print(position)

