import requests
import os
import dotenv
from datetime import datetime

dotenv.load_dotenv()

token = os.getenv("TOKEN")
username = os.getenv("USERNAME")

PIXELA_END_POINT = "https://pixe.la/v1/users"
GRAPH_ID = 'graph1'
user_params = {
    'token': token,
    'username': username,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'

}

# THIS IS CREATING USER NAME

# response = requests.post(PIXELA_END_POINT, json=user_params)
# print(response.text)

graph_config = {
    'id': GRAPH_ID,
    'name': 'coding',
    'unit': 'km',
    'type': 'float',
    'color': 'kuro',
}
headers = {
    'X-USER-TOKEN': token
}
graph_end_point = f"{PIXELA_END_POINT}/{username}/graphs"

# response = requests.post(url=graph_end_point, json=graph_config, headers=headers)
# print(response.text)

# /v1/users/<username>/graphs/<graphID> 

# GETTING TODAYS DATE SO I DONT HAVE TO TYPE IT MANUALLY
today = datetime.now()
today_date = today.strftime("%Y%m%d")


# UPDATE DOT GRAPH
dots_config = {
    'date':today_date,
    'quantity': '1.5'
}

dots_end_point = f"{PIXELA_END_POINT}/{username}/graphs/{GRAPH_ID}"
# response = requests.post(url=dots_end_point, json=dots_config, headers=headers)
# print(response.text)


# /v1/users/<username>/graphs/<graphID>/<yyyyMMdd>

put_config = {
    'quantity': '5.6'
}
put_end_point = f"{PIXELA_END_POINT}/{username}/graphs/{GRAPH_ID}/{today_date}"
response = requests.put(url=put_end_point, json=put_config, headers=headers)
print(response.text)


