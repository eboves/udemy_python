import requests
import os
import dotenv

dotenv.load_dotenv()

token = os.getenv("TOKEN")
username = os.getenv("USERNAME")

PIXELA_END_POINT = "https://pixe.la/v1/users"
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
    'id': 'graph1',
    'name': 'coding',
    'unit': 'km',
    'type': 'float',
    'color': 'kuro',
}
headers = {
    'X-USER-TOKEN': token
}
graph_end_point = f"{PIXELA_END_POINT}/{username}/graphs"

response = requests.post(url=graph_end_point, json=graph_config, headers=headers)
print(response.text)

