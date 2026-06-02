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