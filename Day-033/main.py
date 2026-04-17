"""
Day 33 - API

Description:
Working with API, using the International Space Station API

"""
import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)